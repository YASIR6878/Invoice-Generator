from django.db import models

class Cosmetic(models.Model):
    item=models.CharField(max_length=100)
    itemid=models.CharField(max_length=100)
    itemprice=models.IntegerField(default=1)
class Groceries(models.Model):
    item=models.CharField(max_length=100)
    itemid=models.CharField(max_length=100)
    itemprice=models.IntegerField(default=1)
class Cold(models.Model):
    item=models.CharField(max_length=100)
    itemid=models.CharField(max_length=100)
    itemprice=models.IntegerField(default=1)
class Ice(models.Model):
    item=models.CharField(max_length=100)
    itemid=models.CharField(max_length=100)
    itemprice=models.IntegerField(default=1)
class Seller(models.Model):
    name=models.CharField(max_length=100)
    add=models.CharField(max_length=100)
    call=models.CharField(max_length=10)
class Buyer(models.Model):
    namebuyer=models.CharField(max_length=100)
    addbuyer=models.CharField(max_length=100)
    callbuyer=models.CharField(max_length=10)

