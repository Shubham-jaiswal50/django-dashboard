
from django.urls import path
from app import views

urlpatterns = [
   path('',views.index,name='index'),
   path('register/',views.register,name='register'),
   path('adminlogin/',views.adminlogin,name='adminlogin'),
   path('admindashboard/',views.admindashboard,name='admindashboard'),
   path('userdashboard/',views.userdashboard,name='userdashboard'),
   path('adduser/',views.adduser,name='adduser'),
   path('displayuser/',views.displayuser,name='displayuser'),
   path('edituser/',views.edituser,name='edituser'),
    path('delete/',views.delete,name='delete'),
    path('remove/<int:pk>',views.remove,name='remove'),
   




]
