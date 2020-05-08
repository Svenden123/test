from django.db import models
from django.utils.timezone import now


class Post(models.Model):
    title = models.CharField(max_length=512)
    content = models.TextField()
    photo = models.ImageField(upload_to='static/blog/uploads/')
    pub_date = models.DateTimeField(default=now, editable=False)
