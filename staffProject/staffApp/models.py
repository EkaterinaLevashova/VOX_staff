from django.db import models


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


class MetaUser(models.Model):
    """Need for models form example: name, email"""
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, unique=True)
    
    def __str__(self):
        return str(self.name)
