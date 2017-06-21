from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    post_content = models.TextField()

    def __str__(self):
        return self.title
