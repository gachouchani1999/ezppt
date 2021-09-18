import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from string import punctuation


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
    
    print(word_frequencies)


a = """
This case explores the growth strategies of Teva, an Israel-based company which is now the world’s largest
‘generic’ pharmaceuticals producer. Under the direction of CEO Shlomo Yanai, Teva followed an aggressive
inorganic growth programme until 2010, becoming a more diversified pharmaceutical company with markets
all over the world. However, the resulting complexity led to a period of reduced profitability and failure to
achieve the bold revenue growth targets, creating boardroom tensions and investor unease. A series of top
management changes followed, each associated with a new strategy but with disappointing performance. By
2015, those strategies were being discarded in favour of a return to the principles that had served Teva so
well in the past: growth through M&A and strategic partnerships, with rapid integration and rationalisation
of production capacity."""
summarize_heading(a)




