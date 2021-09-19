import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from string import punctuation
from heapq import nlargest

nltk.download('punkt')
nltk.download("stopwords")
stop_words = stopwords.words('english')
punctuation = punctuation + '/n'

def summarize_heading(heading_text):
    tokens = word_tokenize(heading_text)
    word_frequencies = {}
    for word in tokens :
        if word.lower() not in stop_words and word.lower() not in punctuation:
            if word not in word_frequencies.keys():
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
    select_length = 2
    summary = nlargest(select_length, sentence_weight, key= sentence_weight.get)
    
    return summary









