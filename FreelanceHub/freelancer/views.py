from django.shortcuts import render,redirect
from app1.models import *
from freelancer.models import *
from django.contrib import messages
# Create your views here.

def apply_project(request):

    if request.method=="POST":
        data=request.POST
        client_id=data.get('cId')
        project_id=data.get('Id')
        username=data.get('username')

        free_obj=freelancer.objects.filter(user_name=username)
        print(free_obj)
        obj=list(free_obj)
        freelancer_id=obj[0].id

        projects_request.objects.create(
            client_id=client_id,
            freelancer_id=freelancer_id,
            project_id=project_id,
            
        )
        messages.info(request,'request sent')
    return render(request,'freelancer_project_apply_page.html')


#tithal code
def edit_freelancer(request,id):
    print("in update function")

    name=request.user
    freelancer_o=freelancer.objects.get(id=id)


    freelancer_id=freelancer_o.id
    freelancer_name=freelancer_o.freelancer_name  
    # freelancer_profession=freelancer_o.profession
    freelancer_email=freelancer_o.email
    city=freelancer_o.birthplace
    # experience=freelancer_o.experience
    # totalproject=freelancer_o.totalproject
    # averagerate=freelancer_o.averagerate
    # availabilitystaus=freelancer_o.availabilitystatus

    if request.method == "POST":
        print("in update client fnction")
        data=request.POST
        obj=freelancer.objects.get(id=id)

        freelancer_name=data.get('fname')
        # profession=data.get('profession')
        city=data.get('city')
        # experience=data.get('experience')
        # totalprojects=data.get('totalproject')
        email=data.get('email')
        # averagerate=data.get('averagerate')
        # availabilitystatus=data.get('availabilitystatus')

        obj.freelancer_name=freelancer_name
        # obj.profession=profession
        obj.cityt=city
        # obj.experience=experience
        # obj.totalprojects=totalproject
        obj.email=email
        # obj.averagerate=averagerate
        # obj.availabilitystatus=availabilitystatus
        obj.save()
        return redirect('/freelancer_page/')

    return render(request,'edit_freelancer.html',context={'freelancer_name':freelancer_name,'freelancer_email':freelancer_email,'city':city,'freelancer_id':freelancer_id})


     
def deletefreelancer(request,id):

    obj=freelancer.objects.get(id=id)
    obj.delete()
    logout(request)
    return redirect('/app1/')
    
    return render(request,'edit_freelancer.html')

def view_freelancer(request):

    name=request.user
    print(name)
    free_obj=freelancer.objects.filter(user_name=request.user)

    free_o=list(free_obj)
    free_name=free_o[0].freelancer_name
    freelancer_username=free_o[0].user_name
    free_id=free_o[0].id
    # free_website=free_o[0].website_link
    free_email=free_o[0].email
    city=free_o[0].birthplace
    phone=free_o[0].phone
    age=free_o[0].age
    gender=free_o[0].gender
    # location=free_o[0].address
    # pincode=free_o[0].pincode
   
    return render(request,'dashboard_Free.html',context={"free_name":free_name,"free_id":free_id,"freelancer_username":freelancer_username,"free_email":free_email,"city":city,"phone":phone,"age":age,"gender":gender})

def select_freelancer(request,id):

    obj=projects_request.objects.get(id=id)
    obj.status="Select"
    obj.save()
    

    return render(request,'dashboard_client.html')

def reject_freelancer(request,id):

    obj=projects_request.objects.get(id=id)
    obj.status="Reject"
    obj.save()
    

    return render(request,'dashboard_client.html')

def freelancer1(request,id):

    obj=freelancer.objects.get(id=id)
    free_name=obj.freelancer_name
    freelancer_username=obj.user_name
    free_id=obj.id
    # free_website=free_o[0].website_link
    free_email=obj.email
    city=obj.birthplace
    phone=obj.phone
    age=obj.age
    gender=obj.gender

    return render(request,'dashboard_Free.html',context={"free_name":free_name,"free_id":free_id,"freelancer_username":freelancer_username,"free_email":free_email,"city":city,"phone":phone,"age":age,"gender":gender})
