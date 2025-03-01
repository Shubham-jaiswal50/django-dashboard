
from django.urls import path
from app import views

urlpatterns = [
   path('',views.index,name='index'),
  

#    path('admindashboard/',views.admindashboard,name='admindashboard'),
#    path('userdashboard/',views.userdashboard,name='userdashboard'),
   path('adduser/',views.adduser,name='adduser'),
   path('displayuser/',views.displayuser,name='displayuser'),
   path('edituser/',views.edituser,name='edituser'),
    path('delete/',views.delete,name='delete'),
    path('remove/<int:pk>',views.remove,name='remove'),
    path('update/<int:pk>',views.update,name='update'),
    path('updatedata/<int:pk>',views.updatedata,name='updatedata'),
    path('logout/',views.logout,name='logout'),
    path('logout2/',views.logout2,name='logout2'),
    path('profile/<int:pk>/',views.profile, name='profile'), 
    path('task1/',views.task1, name='task1'),
    path('givetask/<int:pk>',views.givetask,name='givetask'),
    path('reset/<int:pk>',views.reset, name='reset'),
    path('showtask/<int:pk>',views.showtask, name='showtask'),
    


   




]
