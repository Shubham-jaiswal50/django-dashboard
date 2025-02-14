from django.shortcuts import render
from .models import AdminDatabase,EmpDatabase

# Create your views here.
def index(request):

    return render(request,'index.html')


def register(request):
    return render(request,'register.html')



def adminlogin(request):
   

    if(request.method=='POST'):
        admin_email=request.POST.get('email')
        password=request.POST.get('pass')
        data=AdminDatabase.objects.filter(admin_email=admin_email)
        if(data):
            user=AdminDatabase.objects.get(admin_email=admin_email)
            print (user)
            mypass=user.admin_password
            if(mypass==password):
                return render(request,'admindashboard.html')

        
    return render(request,'adminlogin.html')



from django.shortcuts import render, redirect
from .models import AdminDatabase, EmpDatabase

def admindashboard(request):
    
    return render(request, 'admindashboard.html')
        


def userdashboard(request):
  return render(request,'admindashboard.html')


def adduser(request):
    if request.method == 'POST':  # Fixed 'POSt' typo
        name = request.POST.get('name')
        email = request.POST.get('email')
        dob = request.POST.get('dob')  # Get Date of Birth
        doj = request.POST.get('joining')
        contact = request.POST.get('contact')
        dep = request.POST.get('department')
        passw = request.POST.get('passw1')
        cnfpass = request.POST.get('passw2')
        work = request.POST.get('work')  # Get work description
        
        if passw == cnfpass:  # Check if passwords match
            EmpDatabase.objects.create(
                employe_name=name,
                employe_email=email,
                employe_dob=dob,  # Include Date of Birth
                date_of_joining=doj,
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
    # mydata1=EmpDatabase.objects.get(id=pk)
    # mydata1.delete()
    myans=EmpDatabase.objects.all()
    return render(request,'delete.html',{'data3':myans.values})

def remove(request,pk):
    data=EmpDatabase.objects.get(id=pk)
    data.delete()
    stu=EmpDatabase.objects.all()
    return render(request,'delete.html',{'data3':stu.values})





