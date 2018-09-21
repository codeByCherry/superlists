from django.db import models


class List(models.Model):

    def __str__(self):
        return f'{self.pk}'


class Item(models.Model):
    text = models.CharField(max_length=255)
    list = models.ForeignKey('List', default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
