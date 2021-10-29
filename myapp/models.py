from django.db import models

# Create your models here.


class advisor(models.Model):
    name = models.CharField(max_length=70, blank=False)
    photourl = models.URLField()
    bookingtime = models.charField(max_length=70,null=True)
    booking_id=models.IntegerField(null=True)

    def __str__(self):
        return self.name
class user(models.Model):
    name = models.CharField(max_length=70, blank=False)
    password=models.CharField(max_length=70, blank=False)
    email=models.EmailField()
    login= models.BooleanField(default=False)
    def __str__(self):
        return self.name
class bookingreq(models.Model):
    user_id=models.IntegerField(null=True)
    advisor_id=models.IntegerField(null=True)




