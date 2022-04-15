from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username


# MODELS FOR INDEX.HTML TABLE
class Human(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Social(models.Model):
    human = models.ForeignKey(Human, on_delete=models.CASCADE)
    social_name = models.CharField(max_length=255, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.social_name


class AccessRecord(models.Model):
    name = models.ForeignKey(Social, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.date)


# MODELS FOR INDEX.HTML FORM
class MetaUser(models.Model):
    """Need for models form example: name, email"""
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, unique=True)
    
    def __str__(self):
        return str(self.name)
