from django.db import models

# Create your models here.

class school(models.Model):
    # id: 学校ID
    # name: 名称
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)