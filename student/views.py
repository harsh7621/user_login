from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib import auth
from .models import student
from django.http import JsonResponse
# Create your views here.



def form(request):
	if request.method == 'POST':
		student_name = request.POST['studentname']
		enrollment_no = request.POST['enumber']
		gender = request.POST['gender']
		hobby = request.POST['hobby']
		country = request.POST['country']
		city = request.POST['state']
		state = request.POST['city']

		image = request.FILES['image']
		fs = FileSystemStorage()
		filename = fs.save(image.name, image)
		url1 = fs.url(filename)

		student_information=student(student_name=student_name,enrollment_no=enrollment_no,gender=gender,hobby=hobby,country=country,city=city,state=state,student_img=url1)
		student_information.save()
		return redirect('/student/form')
	else:
		all_student_data = student.objects.all()
		return render(request,'form.html',{'all_student_data':all_student_data})
	