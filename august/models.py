from django.db import models

# Create your models here.

class Student (models.Model):
    first_name = models.CharField('Adı', max_length=50)
    last_name = models.CharField('Soyadı', max_length=50)
    age = models.IntegerField('Yas')
    number = models.IntegerField('Numara')
    section = models.CharField('Sınıfı', max_length=10)
    registered_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['number']
        verbose_name_plural = 'Öğrenciler'


class Teacher (models.Model):
    first_name = models.CharField('Adı', max_length=50)
    last_name = models.CharField('Soyadı', max_length=50)
    age = models.IntegerField('Yas')
    sicili = models.IntegerField('Sicili')
    field = models.CharField('Uzmanlık Alanı', max_length=10)
    registered_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.field} - {self.first_name} {self.last_name}"

    class Meta:
        ordering = ['sicili']
        verbose_name_plural = 'Öğretmenler'