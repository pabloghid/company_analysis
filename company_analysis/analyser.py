from textblob import TextBlob
import matplotlib.pyplot as plt
from langdetect import detect
from google_trans_new import google_translator

def percentage(parte, total):
    return 100*float(parte)/float(total)

def analyser(content):
    positive = 0
    negative = 0
    neutral = 0
    polarity = 0

    contents = []
    for sentence in content:
        if detect(sentence) != 'en':
            sentence = translate(sentence)
        contents.append(TextBlob(sentence))

    for item in contents:
        polarity += item.sentiment.polarity
        print(item, "\n", item.sentiment)

        if(0 <= item.sentiment.polarity < 0.09):
            neutral += 1
            print("neutro")
        elif(item.sentiment.polarity < 0):
            negative += 1
            print("negativo")
        elif(item.sentiment.polarity > 0):
            positive += 1
            print("positivo")

    positive = format(percentage(positive, len(contents)), '.2f')
    negative = format(percentage(negative, len(contents)), '.2f')
    neutral = format(percentage(neutral, len(contents)), '.2f')

    return {
        "positive": positive, "negative": negative, "neutral": neutral
    }

    ## TODO: Refazer para plotar no navegador
"""     labels = ['Positivo ['+str(positive)+'%]', 'Neutro ['+str(neutral)+'%]', 'Negativo ['+str(negative)+'%]']
    sizes = [positive, neutral, negative]
    colors = ['green', 'lightgray', 'red']
    patches,texts = plt.pie(sizes, colors=colors, startangle=90)

    plt.legend(patches, labels, loc="best")
    plt.axis('equal')
    plt.tight_layout()
    plt.show() """

def translate(sentence):
    translator = google_translator(url_suffix="com")
    translate_text = translator.translate(sentence,lang_tgt='en') 
    return translate_text