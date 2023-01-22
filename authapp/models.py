from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length= 25)
    email = models.EmailField()
    phonenumber = models.CharField(max_length= 12)
    description = models.TextField()

    def __str__(self) -> str:
        return self.email

class Enrollment(models.Model):
    fullName = models.CharField(max_length=25)
    email = models.EmailField()
    gender = models.CharField(max_length=25)
    phoneNumber = models.CharField(max_length=12)
    dob = models.CharField(max_length=50)
    selectMembershipPlan = models.CharField(max_length=200)
    selectTrainer = models.CharField(max_length=55)
    reference = models.CharField(max_length=55)
    address = models.TextField()
    paymentStatus=models.CharField(max_length=55,blank=True,null=True)
    price=models.IntegerField(blank=True,null=True)
    dueDate=models.DateTimeField(blank=True,null=True)
    timeStamp = models.DateTimeField(auto_now_add= True, blank= True)

    def __str__(self) -> str:
        return self.fullName

class Trainer(models.Model):
    name = models.CharField(max_length=55)
    gender = models.CharField(max_length=25)
    phone = models.CharField(max_length=12)
    salary = models.IntegerField()
    timeStamp = models.DateTimeField(auto_now_add= True, blank= True)

    def __str__(self) -> str:
        return self.name

class MembershipPlan(models.Model):
    plan=models.CharField(max_length=185)
    price=models.IntegerField()

    def __int__(self):
        return self.id

class Gallery(models.Model):
    title=models.CharField(max_length=100)
    img=models.ImageField(upload_to='gallery')
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)
    def __int__(self):
        return self.id

class Attendance(models.Model):
    selectdate=models.DateTimeField(auto_now_add=True)
    phonenumber=models.CharField(max_length=15)
    login=models.CharField(max_length=200)
    logout=models.CharField(max_length=200)
    selectWorkout=models.CharField(max_length=200)
    trainedBy=models.CharField(max_length=200)
    def __int__(self):
        return self.id