from django.db import models

class Table(models.Model):
	name=models.CharField(max_length=64, verbose_name='이름')
	registered=models.DateTimeField(auto_now_add=True, verbose_name='등록')