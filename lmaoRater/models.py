from django.db import models

class WhiteCard(models.Model):
    CardNo = models.IntegerField()
    CardText = models.CharField(max_length=50)

class BlackCard(models.Model):
    CardNo = models.IntegerField()
    CardText = models.CharField(max_length=50)

class score(models.Model):
    #Uses two foreign keys to define the relationship
    WhiteCard = models.ForeignKey(WhiteCard, models.CASCADE)
    BlackCard = models.ForeignKey(BlackCard, models.CASCADE)
    rating = models.DecimalField(max_digits=4,decimal_places=2)
    timesAppeared = models.IntegerField(default=0)


