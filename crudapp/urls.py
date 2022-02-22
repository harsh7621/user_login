from django.contrib import admin
from django.urls import path,include
from crudapp import views

urlpatterns = [
	
    path('registration',views.user_registration),
    path('login',views.user_login),
    path('logout',views.user_logout),
    
    
    
  
    
    

]