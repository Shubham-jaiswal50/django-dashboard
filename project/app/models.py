from django.db import models

class EmpDatabase(models.Model):

    employe_name = models.CharField(max_length=50)
    employe_email = models.EmailField()
    department = models.CharField(max_length=50)
    contact_number = models.IntegerField()
    employe_password = models.CharField(max_length=50)
    your_work = models.TextField(max_length=100)

    


class AdminDatabase(models.Model):
    admin_name = models.CharField(max_length=50)
    
    admin_email = models.EmailField()

    contact_number = models.IntegerField()
    admin_password = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.admin_name*