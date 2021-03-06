from django.db import models

# Create your models here.


class Articles(models.Model):
    # title
    title = models.CharField(max_length=300, default='Title has not been set')
    # date
    date = models.DateField(default="Date has not been set")
    # topic(s)  --> go for ListCharField or JSONField?
    topics = models.CharField(
        max_length=100, default='Topics have not been set')
    # tags
    tags = models.CharField(max_length=400, default='Tags have not been set')
    # type
    articleType = models.CharField(
        max_length=50, default='Article Type has not been set')
    # summary
    summary = models.CharField(max_length=(
        60*20), default='Summary has not been set')
    # author(s)
    authors = models.CharField(
        max_length=100, default='Authors have not been set')
    # link-type
    linkType = models.CharField(max_length=20, default='A')
    # link
    documentLink = models.CharField(
        max_length=200, default='Document link has not been set')
    # image 1 link
    image1Link = models.CharField(
        max_length=200, default="Image link 1 has not been set")
    # image 2 link
    image2Link = models.CharField(
        max_length=200, default="Image link 2 has not been set")


def __str__(self):
    return self.title
