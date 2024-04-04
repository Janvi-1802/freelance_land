from django.shortcuts import render,redirect
from app1.models import *
from django.contrib import messages
from freelancer.models import *
from client.models import *
from project_management.models import *
from django.db.models import F

# Create your views here.
def project_management(request,id):
    obj=client.objects.get(id=id)
    id=obj.id
    return render(request,'index_project.html',context={"id":id})

def upload_projectPost(request,id):
    obj=client.objects.get(id=id)
    id=obj.id

    if request.method=="POST":
        title=request.POST.get('title')
        discription=request.POST.get('dis')
       
        amount=request.POST.get('amount')


        project_post.objects.create(
       client_id=obj,
       title=title,
       Project_discription=discription,
     
       amount=amount
       )
        messages.info(request,'project uploaded successfully')
        
        # all_project=project_post.objects.get(id=7)
        return render(request,'client_dashboard.html')
       
       # title=all_project.title
       # video_link=all_project.discription_video
       # image_link=all_project.discription_image
       

    return render(request,'upload_project.html',context={"id":id})


def show_all_project(request,id):
    obj=client.objects.get(id=id)
    id=obj.id
    all_project=project_post.objects.filter(client_id=id)
    return render(request,'show_all_post.html',context={"all_project":all_project})
    
def delete_post(request,id):

    obj=project_post.objects.get(id=id)
    client_id=obj.client_id
    obj.delete()
    return render(request,'dashboard_client.html')
    #return redirect('/show_all_project/<client_id>/')

def update_post(request,id):
    obj=project_post.objects.get(id=id)
    if request.method=="POST":
        title=request.POST.get('title')
        discription=request.POST.get('dis')
        amount=request.POST.get('amount')

        obj.title=title
        obj.Project_discription=discription
        obj.amount=amount
        obj.save()
        return render(request,'dashboard_client.html')

    return render(request,'edit_project.html')   


def hire_manage(request,id):
    # his_all_projects=project_post.objects.filter(client_id=id)

    
    # for p in his_all_projects:
        
    #     project_request_obj=projects_request.objects.filter(project_id=p.id)
    #     print(project_request_obj)

    #  queryset = project_post.objects.select_related('project').filter(project__project_id=F('project_id'))


    #  queryset = project_post.objects.select_related('project').filter(project__project_id=F('project_id'))
    # Add the ProjectRequest table explicitly
    #  queryset = queryset | projects_request.objects.select_related('project').filter(project__project_id=F('project_id'))
    # You can now use the queryset to display the data in your template or return it as JSON, etc.
    # Example: render a template with the queryset
    # obj=.objects.raw("SELECT* FROM auth_user WHERE password==password")

    # queryset = project_post.objects.filter(id__in=projects_request.objects.values('project_id'))
     queryset=projects_request.objects.filter(client_id=id)

     return render(request,'hiring.html',context= {'queryset': queryset})
