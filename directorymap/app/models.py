from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class CallNumber(models.Model):
    call_number = models.CharField(max_length=50)

    def __str__(self):
        return self.call_number

class Title(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

class Book(models.Model):
    author = models.ForeignKey(Author)
    call_number = models.ForeignKey(CallNumber)
    title = models.ForeignKey(Title)

    def __str__(self):
        return "%s - %s [%s]" % (self.author, self.title, self.call_number)

class Location(models.Model):
    location = models.CharField(max_length=50)
    filename = models.ImageField(upload_to="locationmaps")

    def __str__(self):
        return self.location

class Item(models.Model):
    accession_number = models.CharField(max_length=25)
    book = models.ForeignKey(Book)
    location = models.ForeignKey(Location)

    def __str__(self):
        return "%s %s %s" % (self.accession_number, self.book, self.location)

