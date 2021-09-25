from lmaoRater.models import WhiteCard, BlackCard, score

whiteCards = open('C:/Users/obo10/Desktop/School/Docs/white_cards.csv')
blackCards = open('C:/Users/obo10/Desktop/School/Docs/black_cards.csv')


whiteCardLine = whiteCards.readline()
newWhiteCard = WhiteCard()

blackCardLine = blackCards.readline()
newBlackCard = BlackCard()

while whiteCardLine != '':
    whiteCardLine = whiteCardLine.strip()
    numberThenText = whiteCardLine.split(',')
    newWhiteCard = WhiteCard(CardText=numberThenText[1], CardNo=numberThenText[0])
    newWhiteCard.save()
    print(numberThenText)
    whiteCardLine = whiteCards.readline()

while blackCardLine != '':
    blackCardLine = blackCardLine.strip()
    numberThenText = blackCardLine.split(',')
    newBlackCard = BlackCard(CardText=numberThenText[1], CardNo=numberThenText[0])
    newBlackCard.save()
    print(numberThenText)
    blackCardLine = blackCards.readline()


for whiteCard in WhiteCard.objects.all():
    for blackCard in BlackCard.objects.all():
        newscore = score(WhiteCard=whiteCard, BlackCard=blackCard, rating=0, timesAppeared=0)
        newscore.save()
