from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=128)
    created_date = models.DateField(auto_now=False, auto_now_add=True)
    completed_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title

    def __repr__(self):
        return '{i}:{t}'.format(i=self.id, t=self.title)

    class Meta:
        db_table = 'Items'


class Comment(models.Model):
    text = models.TextField()
    created_date = models.DateField(auto_now=False, auto_now_add=True)
    item = models.ForeignKey(Item, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    def __repr__(self):
        return self.id

    class Meta:
        db_table = 'Comments'
