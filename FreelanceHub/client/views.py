from django.shortcuts import render,redirect
from django.contrib.auth import login
from app1.models import *
from django.contrib import messages
from django.contrib.auth import login
from django.db.models.query import RawQuerySet
from django.contrib.auth import login,authenticate,logout

# Create your views here.

def cli_page(request):

    name=request.user
    Client_obj=client.objects.filter(user_name=request.user)

    client_o=list(Client_obj)
    client_name=client_o[0].client_name
    client_id=client_o[0].id
    client_website=client_o[0].website_link
    client_email=client_o[0].email
    CEO=client_o[0].CEO
    phone=client_o[0].phone
    location=client_o[0].address
    pincode=client_o[0].pincode
    headquarter=client_o[0].headquarter

    return render(request,'dashboard_client.html',context={'client_name':client_name,'client_id':client_id,'client_website':client_website,'client_email':client_email,'CEO':CEO,'phone':phone,'location':location,'pincode':pincode,'headquarter':headquarter})

   
def edit_client_details(request):
    name=request.user
    Client_obj=client.objects.filter(user_name=request.user)

    client_o=list(Client_obj)
    client_id=client_o[0].id
    client_name=client_o[0].client_name
    client_website=client_o[0].website_link
    client_email=client_o[0].email
    CEO=client_o[0].CEO
    phone=client_o[0].phone
    location=client_o[0].address
    pincode=client_o[0].pincode
    headquarter=client_o[0].headquarter


    

    return render(request,'edit_client.html',context={'client_name':client_name,'client_website':client_website,'client_email':client_email,'CEO':CEO,'phone':phone,'location':location,'pincode':pincode,'headquarter':headquarter,'client_id':client_id})

def update_client(request,id):
    print("in update function")

    name=request.user
    client_o=client.objects.get(id=id)

    
    client_id=client_o.id
    client_name=client_o.client_name
    client_website=client_o.website_link
    client_email=client_o.email
    CEO=client_o.CEO
    phone=client_o.phone
    location=client_o.address
    pincode=client_o.pincode
    headquarter=client_o.headquarter

    if request.method == "POST":
        print("in update client fnction")
        data=request.POST
        obj=client.objects.get(id=id)
       
        client_name=data.get('cname')
        CEO=data.get('ceo')
        address=data.get('address')
        pincode=data.get('pincode')
        phone=data.get('phone')
        email=data.get('email')
        headquarter=data.get('hq')
        website_link=data.get('wblink')
        comany_certificate=request.FILES.get('cc')

        obj.client_name=client_name
        obj.CEO=CEO
        obj.address=address
        obj.pincode=pincode
        obj.phone=phone
        obj.email=email
        obj.headquarter=headquarter
        obj.website_link=website_link
        obj.comany_certificate=comany_certificate
        obj.save()
        return redirect('/client_page/')

    return render(request,'edit_client.html',context={'client_name':client_name,'client_website':client_website,'client_email':client_email,'CEO':CEO,'phone':phone,'location':location,'pincode':pincode,'headquarter':headquarter,'client_id':client_id})

def deleteclient(request,id):

    obj=client.objects.get(id=id)
    obj.delete()
    logout(request)
    return redirect('/app1/')
    
    return render(request,'edit_client.html')