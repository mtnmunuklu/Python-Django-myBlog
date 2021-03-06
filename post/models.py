from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120, verbose_name="Başlık")
    content = models.TextField(verbose_name="İçerik")
    publishing_date = models.DateField(verbose_name="Yayınlanma Tarihi",auto_now_add=True)

    def __str__(self):
        return  self.title


    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'id': self.id})
    def get_create_url(self):
        return reverse('post:create')
    def get_update_url(self):
        return reverse('post:update', kwargs={'id': self.id})
    def get_delete_url(self):
        return reverse('post:delete', kwargs={'id': self.id})