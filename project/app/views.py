from django.shortcuts import render,redirect
from .models import AdminDatabase,EmpDatabase
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def index(request):
    adminemail = "jaiswalshubham0698@gmail.com"
    adminpass = "shubham@123"
    
    if request.method == 'POST':
        user_email = request.POST.get('email')
        password = request.POST.get('password')
        user = EmpDatabase.objects.filter(employe_email=user_email)

        if user_email == adminemail and password == adminpass:
            return render(request,'admindashboard.html')

        if user.exists():
            data = EmpDatabase.objects.get(employe_email=user_email)
            pass1 = data.employe_password

            if pass1 == password:
                return render(request, 'userdashboard.html', {'name': data.employe_name, 'email': data.employe_email, 'user_id': data.id})
            else:
                message = "Email and password do not match"
                return render(request, 'index.html', {'message': message})
        else:
            message2 = "Email ID does not exist"
            return render(request, 'index.html', {'message2': message2})

    return render(request, 'index.html')
 
        
# def admindashboard(request):
    
#     return render(request, 'admindashboard.html')
        


# def userdashboard(request):
#   return render(request,'admindashboard.html')


def adduser(request):
    if request.method == 'POST':  
        name = request.POST.get('name')
        email = request.POST.get('email')
        # dob = request.POST.get('dob')  
        # doj = request.POST.get('joining')
        contact = request.POST.get('contact')
        dep = request.POST.get('department')
        passw = request.POST.get('passw1')
        cnfpass = request.POST.get('passw2')
        work = request.POST.get('work')  
        
        if passw == cnfpass:  
            EmpDatabase.objects.create(
                employe_name=name,
                employe_email=email,
               
                department=dep,
                contact_number=contact,
                employe_password=passw,
                your_work=work  # Include work description
            )
            return render(request, 'adduser.html', {'msg2': "Registration successful"})
        else:
            return render(request, 'adduser.html', {'msg': "Passwords do not match"})
    

    
    return render(request,'adduser.html')

def edituser(request):
     myans1=EmpDatabase.objects.all()
     return render(request,'edituser.html',{'data2':myans1.values})

def displayuser(request):
    mydata=EmpDatabase.objects.all()
    return render(request,'displayuser.html',{'data':mydata.values})

def delete(request):
    
    myans=EmpDatabase.objects.all()
    return render(request,'delete.html',{'data3':myans.values()})

def remove(request,pk):
    data=EmpDatabase.objects.get(id=pk)
    data.delete()
    stu=EmpDatabase.objects.all()
    return render(request,'delete.html',{'data3':stu.values})
def update(request,pk):
    x=EmpDatabase.objects.get(id=pk)
    emp=EmpDatabase.objects.all()
    
    return render(request,'edituser.html',{'data2':emp,'data4':x})

def updatedata(request,pk):

    if request.method=="POST":
          x =EmpDatabase.objects.get(id=pk)
          name = request.POST.get('name')
          email = request.POST.get('email')
       
          contact = request.POST.get('contact')
          dep = request.POST.get('dep')
          work = request.POST.get('work') 
         

          x.employe_name=name
          x.employe_email=email
        
          x.contact_number=contact
          x.department=dep
          x.your_work=work
          x.save()
          stu=EmpDatabase.objects.all()
          return render(request,'edituser.html',{'data2':stu})
    
def logout(request):
    return render(request,'index.html')

def logout2(request):
    return render(request,'index.html')

def profile(request, pk):  
    user = EmpDatabase.objects.filter(id=pk).first()   # Get the user by primary key  
    print(user)  # Debugging to see if user exists
    
    if user:  
        return render(request, 'profile.html', {
            'name': user.employe_name,
            'email': user.employe_email,
            'department': user.department,
            'contact': user.contact_number,
            'work': user.your_work,
            'user_id': user.id   # Ensure user.id exists
        })
    
    return render(request, 'profile.html', {'error': 'User not found'})  




# def reset(request, pk):
#     print(pk)
#     data = EmpDatabase.objects.get(id=pk)
#     if request.method == "POST":
#         oldpass = request.POST.get('old')
#         newpass = request.POST.get('new')

#         if data and data.employe_password == oldpass:
#             data.employe_password = newpass
#             data.save()
#             return render(request, 'reset.html', {'data': data, 'msg': "Password reset successfully!"})
#         else:
#             return render(request, 'reset.html', {'data': data, 'msg2': "Old password does not match!"})

#     return render(request, 'reset.html', {'data': data})

def reset(request, pk):
    print(pk)
    data = EmpDatabase.objects.get(id=pk)

    if request.method == "POST":
        oldpass = request.POST.get('old')
        newpass = request.POST.get('new')

        if data and data.employe_password == oldpass:
            data.employe_password = newpass
            data.save()
            
            # Show a success message
            messages.success(request, "Password reset successfully!")
            
            # Redirect to the previous page
            previous_url = request.META.get('HTTP_REFERER', reverse('index'))  # Default to 'index' if no referrer
            return redirect(previous_url)

        else:
            messages.error(request, "Old password does not match!")

    return render(request, 'reset.html', {'data': data})




def task1(request):
    myans2=EmpDatabase.objects.all()
    return render(request,'task1.html',{'data2':myans2.values})



def changes(request, pk):
    
    if request.method == "POST":
        oldpass = request.POST.get('old')
        newpass = request.POST.get('new')
        user = EmpDatabase.objects.filter(id=pk).first()

        if user and user.employe_password == oldpass:
            user.employe_password = newpass
            userid=user.id
           
            user.save()
            return render(request, 'reset.html', {'msg': "Password reset successfully",'data11':userid})

    return render(request, 'reset.html', {'msg': "Incorrect old password"})

def givetask(request,pk):
    
    data=EmpDatabase.objects.get(id=pk)
    myans2=EmpDatabase.objects.all()
    if request.method == "POST":
        newtask=request.POST.get('text')
        if data:
            data.your_work=newtask
            data.save()


    return render(request,'task1.html',{'data2':myans2.values,'mydata':data})


def showtask(request,pk):
    task=EmpDatabase.objects.get(id=pk)
    mytask=task.your_work
    return render(request,'showtask.html',{'taskdata':task,'mytsk':mytask})





    

    

    

    




