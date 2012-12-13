from django.db import models

# Create your models here.

class Drink(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    available = models.BooleanField(default=True)

    def __unicode__(self):
        return unicode(self.name)

class DrinkOrder(models.Model):
    drink = models.ForeignKey(Drink)
    person = models.CharField(max_length=50)
    notes = models.TextField(null=True)

    def __unicode__(self):
        return u'%s ordered a %s' % (self.person, self.drink)