from django.db import models

# Create your models here.

class student(models.Model):
	id = models.AutoField
	student_img = models.ImageField()
	student_name = models.TextField(default="", max_length=20)
	enrollment_no = models.IntegerField(default=0)
	gender = models.TextField(default="", max_length=10)
	hobby = models.CharField(default="", max_length=50)
	country = models.TextField(default="", max_length=10)
	city = models.TextField(default="", max_length=10)
	state = models.TextField(default="", max_length=10)
	