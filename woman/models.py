from django.db import models

# Create your models here.
class Women(models.Model):
    title = models.CharField(max_length=200,blank=True, null=True)
    content = models.TextField(null=True, blank=True)
    time_create = models.DateField(auto_now_add=True)
    time_update = models.DateField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Женщина'
        verbose_name_plural = 'Женщины'

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
