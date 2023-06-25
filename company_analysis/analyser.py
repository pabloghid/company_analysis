from textblob import TextBlob
import matplotlib.pyplot as plt

def percentage(parte, total):
    return 100*float(parte)/float(total)

def analyser():
    positive = 0
    negative = 0
    neutral = 0
    polarity = 0

    ## Verificar idioma, traduzir para inglês se precisar
    contents = []
    contents.append(TextBlob("They just cloned my credit card @nubank, Lucky I was chatting with a friend and I saw the verification notification arrive, as I thought it was weird I already went and blocked the card. 2 minutes saved me from taking a loss."))
    contents.append(TextBlob("It all seems very suspect if what Microsoft said is true. Why look at the established market first where Microsoft is a *distant* 3rd instead of focusing on a “market” you say you want to protect where you’ve allocated roughly only 1 month to look at. We shall see."))
    contents.append(TextBlob("Brazil is an amazing country!"))
    contents.append(TextBlob("Microsoft President Brad Smith wants it to be ILLEGAL to remove AI watermarks Microsoft and others are developing."))

    for item in contents:
        polarity += item.sentiment.polarity
        print(item, "\n", item.sentiment)

        if(item.sentiment.polarity == 0):
            neutral += 1
        elif(item.sentiment.polarity < 0):
            negative += 1
        elif(item.sentiment.polarity > 0):
            positive += 1

    positive = format(percentage(positive, len(contents)), '.2f')
    negative = format(percentage(negative, len(contents)), '.2f')
    neutral = format(percentage(neutral, len(contents)), '.2f')

    ## TODO: Refazer para plotar no navegador
    labels = ['Positivo ['+str(positive)+'%]', 'Neutro ['+str(neutral)+'%]', 'Negativo ['+str(negative)+'%]']
    sizes = [positive, neutral, negative]
    colors = ['green', 'lightgray', 'red']
    patches,texts = plt.pie(sizes, colors=colors, startangle=90)

    plt.legend(patches, labels, loc="best")
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

def translator(text):
    ## TODO: Traduzir para inglês e retornar o texto