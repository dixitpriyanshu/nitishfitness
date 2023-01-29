from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from authapp.models import Contact, MembershipPlan, Trainer, Enrollment, Gallery,Attendance
# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def team(request):
    return render(request, 'team.html')


def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
    user_phone=request.user
    posts=Enrollment.objects.filter(phoneNumber=user_phone)
    attendance=Attendance.objects.filter(phonenumber=user_phone)
    print(posts)
    context={"posts":posts,"attendance":attendance}
    return render(request,"profile.html", context)

def gallery(request):
    posts=Gallery.objects.all()
    context={"posts":posts}
    return render(request,"gallery.html",context)


def attendance(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
    selectTrainer = Trainer.objects.all()
    context = {"selectTrainer":selectTrainer}
    if request.method == "POST":
        phonenumber = request.POST.get('phonenumber')
        login = request.POST.get('loginTime')
        logout = request.POST.get('logoutTime')
        selectWorkout = request.POST.get('workout')
        trainedBy = request.POST.get('trainer')
        query = Attendance(phonenumber=phonenumber,login=login,logout=logout,selectWorkout=selectWorkout,trainedBy=trainedBy)
        query.save()
        messages.warning(request,"Attendace Applied Successfully")
        return redirect('/attendance')
    return render(request,"attendance.html",context)



def signup(request):
    if request.method=="POST":
        username=request.POST.get('usernumber')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
      
        if len(username)>10 or len(username)<10:
            messages.info(request,"Phone Number Must be 10 Digits")
            return redirect('/signup')

        if pass1!=pass2:
            messages.info(request,"Password is not Matching")
            return redirect('/signup')
       
        try:
            if User.objects.get(username=username):
                messages.warning(request,"Phone Number is Taken")
                return redirect('/signup')
           
        except Exception as identifier:
            pass
        
        
        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email is Taken")
                return redirect('/signup')
           
        except Exception as identifier:
            pass
        
        
        
        myuser=User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request,"User is Created Please Login")
        return redirect('/login')
        
        
    return render(request,"signup.html")

def handlelogin(request):
    if request.method=="POST":        
        username=request.POST.get('usernumber')
        pass1=request.POST.get('pass1')
        myuser=authenticate(username=username,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Successful")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/login')
            
    return render(request, 'handlelogin.html')

def handlelogout(request):
    logout(request)
    messages.success(request,"Logout Success")    
    return redirect('/login')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('fullname')
        email=request.POST.get('email')
        number=request.POST.get('num')
        desc=request.POST.get('desc')
        myquery=Contact(name=name,email=email,phonenumber=number,description=desc)
        myquery.save()       
        messages.info(request,"Thanks for Contacting us we will get back you soon")
        return redirect('/contact')
        
    return render(request,"contact.html")

def enroll(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')

    membership=MembershipPlan.objects.all()
    selectTrainer=Trainer.objects.all()
    context={"membership":membership,"selectTrainer":selectTrainer}
    if request.method=="POST":
        fullName=request.POST.get('fullName')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        phoneNumber=request.POST.get('phoneNumber')
        dob=request.POST.get('dob')
        member=request.POST.get('member')
        trainer=request.POST.get('trainer')
        reference=request.POST.get('reference')
        address=request.POST.get('address')
        query=Enrollment(fullName=fullName,email=email,gender=gender,phoneNumber=phoneNumber,dob=dob,selectMembershipPlan=member,selectTrainer=trainer,reference=reference,address=address)
        query.save()
        messages.success(request,"Thanks For Enrollment")
        return redirect('/join')

    return render(request,"enroll.html",context)

def change_pass(request):
    if request.method == 'POST':
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 != pass2:
            messages.info(request, 'Possaword does not match.')
            return render(request,"change_password.html")
        user = User.objects.get(username = request.user)
        user.set_password(pass1)
        user.save()
        return redirect('/login')
    return render(request, 'change_password.html')