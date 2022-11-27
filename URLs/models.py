from datetime import datetime
from django.db import models

# Create your models here.
class URLs(models.Model):
    url = models.TextField()
    short_url = models.TextField()
    createTime = models.DateTimeField(default = datetime.now)
    

