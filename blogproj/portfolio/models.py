from django.db import models
#admin/portfolio에서 추가를 눌렀을때 보여질 목록

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title