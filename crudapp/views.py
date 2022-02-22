from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def user_registration(request):
	if request.method == 'POST':
		user_name = request.POST['username']
		first_name = request.POST['fname']
		last_name = request.POST['lname']
		email = request.POST['email']
		password = request.POST['password']

		try:
			user = User.objects.get(username=user_name)
			return render(request,'registration.html',{'username_error':'Username Already Exists.'})
		except User.DoesNotExist:
			user = User.objects.create_user(username=user_name,first_name=first_name,last_name=last_name,email=email,password=password)
			return redirect('/crudapp/login')

	else:

		return render(request,'registration.html')

def user_login(request):
	if request.method == 'POST':
		user_name = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(request, username=user_name, password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('/student/form')
	else:
		return render(request,'login.html')

def user_logout(request):
	auth.logout(request)
	return redirect('/crudapp/login')


	
