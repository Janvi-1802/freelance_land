from django.shortcuts import render,redirect
from .models import *
from project_management.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.db.models.query import RawQuerySet

# Create your views here.
def app1(request):
    
    obj_of_all_project=project_post.objects.all()


    
    return render(request,"index.html",context={"obj_of_all_project":obj_of_all_project})

def signup1(request):
    if request.method=="POST":
        data=request.POST
        client_name=data.get('client_name')
        user_name=data.get('client_user_name')
        password=data.get('password')
        CEO=data.get('CEO')
        address=data.get('address')
        pincode=data.get('pincode')
        phone=data.get('phone')
        email=data.get('email')
        headquarter=data.get('Headquarter')
        website_link=data.get('website_link')

        #for user table 
        username=data.get('client_user_name')
        password1=data.get('password')
       
        
        user=User.objects.filter(username=username)
        if user.exists():
            messages.error(request,'username already taken. ')
            return render(request,'signup1.html')
          
        client.objects.create(
            client_name=client_name,
            user_name=user_name,
            password=password,
            address=address,
            CEO=CEO,
            pincode=pincode,
            phone=phone,
            email=email,
            headquarter=headquarter,
            website_link=website_link
        ) 

        user=User.objects.create(
            username=username,
            password=password1
        )
       # user.set_password(password1)
        #user.save()
     
        messages.info(request,'account created successfully')
        return redirect('/app1/')

    return render(request,'signup1.html')

def sign_up(request):
  
    if request.method=="POST":
        data=request.POST
        freelancer_name=data.get('freelancer_name')
        user_name=data.get('user_name')
        password=data.get('password')
        age=data.get('age')
        gender=data.get('gender')
        email=data.get('email')
        phone=data.get('phone')
        birthplace=data.get('birthplace')
        profile_pic=request.FILES.get('profile_pic')
        
        #for user table 
        username=data.get('user_name')
        password1=data.get('password')
      

        user=User.objects.filter(username=username)
        if user.exists():
            messages.error(request,'username already taken. ')
            return render(request,'sign_up.html')

        user=User.objects.create(
            username=username,
            password=password1    
        )
      #  user.set_password(password1)
      #  user.save()

        freelancer.objects.create(
            freelancer_name=freelancer_name,
            user_name=user_name,
            password=password,
            age=age,
            gender=gender,
            email=email,
            phone=phone,
            birthplace=birthplace,
            profile_pic=profile_pic
        )

        messages.info(request,'account created successfully')
        return redirect("app1")
    return render(request,"sign_up.html")

def option(request):

   # name=request.user
    #Client_obj=client.objects.filter(user_name=request.user)
    return render(request,'option.html')

def login_page(request):

    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username=username).exists():
             messages.error(request,'invalid username')
             return render(request,'login.html')

        print(password)
        user=authenticate(username=username,password=password)
       # user=User.objects.raw("SELECT* FROM auth_user WHERE password==password")
        
        user=User.objects.filter(username=username)
        print(user)
      #  if user is None:
       #     messages.error(request,'invalid password')
        #    return render(request,'login.html')
       # else:
        for o in user:
            if(o.password==password):
                print("login succesfully")
                login(request,o)
                return render(request,'index.html')
            else: 
                messages.error(request,'invalid password')
                return render(request,'login.html')
        # if password==user.password:
        #     print("login succesfully")
        #     login(request,user)
        #     return render(request,'index.html')
        # else:
        #     messages.error(request,'invalid password')
        #     return render(request,'login.html')

    return render(request,'login.html')


def log_out(request):
    
    logout(request)
    return render(request,'login.html')