import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from string import punctuation
from heapq import nlargest

nltk.download("stopwords")
stop_words = stopwords.words('english')
punctuation = punctuation + '/n'

def summarize_heading(heading_text):
    tokens = word_tokenize(heading_text)
    word_frequencies = {}
    for word in tokens :
        if word.lower() not in stop_words and word.lower() not in punctuation:
            if word.lower() not in word_frequencies.keys():
                word_frequencies[word] =1
            else:
                word_frequencies[word] += 1
    max_freq = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word]/max_freq
    sentences = sent_tokenize(heading_text)
    sentence_weight = {}
    for sentence in sentences:
        sentence_wordcount = (len(word_tokenize(sentence)))
        sentence_worcount_no_stopwords = 0
        for word_weight in word_frequencies:
            if word_weight in sentence.lower():
                sentence_worcount_no_stopwords +=1
                if sentence in sentence_weight:
                    sentence_weight[sentence] += word_frequencies[word_weight]
                else:
                    sentence_weight[sentence] = word_frequencies[word_weight]
        sentence_weight[sentence] = sentence_weight[sentence]
    select_length = int(len(sentence_weight)*0.4)
    summary = nlargest(select_length, sentence_weight, key= sentence_weight.get)
    final_summary = [word for word in summary]
    summary = ''.join(final_summary)
    print(summary)


    


a = """
After less than 18 tumultuous months as the head of
Teva, the world‘s largest generic pharmaceuticals
company, in October 2013 Jeremy Levin stepped down
as CEO. He had been brought into the company in
January 2012 to change Teva’s strategy from that of the
outgoing CEO and President Shlomo Yanai, a former
high-ranking army officer, when it seemed clear that the
target of achieving global sales of US$D 33bn 1 by 2015
was no longer achievable, and the share price had subse-
quently collapsed. Its third CEO within two years was
appointed in 2014: Erez Vigodman, a company insider,
who announced that Teva would introduce its third new
global strategy in three years with a focus on product
rationalisation, organic growth and cost saving."""
summarize_heading(a)




