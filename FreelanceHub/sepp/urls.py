"""
URL configuration for sepp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static 
from app1.views import *
from client.views import *
from freelancer.views import *
from project_management.views import *

from static import *

urlpatterns = [
    path('admin/', admin.site.urls),

    #app1 all urls 
    #----------------------------------------------
    path('',app1,name="app1"),
    path('sign_up/',sign_up,name="sign_up"),
    path('sign-up_client/',signup1,name="signup1"),
    path('option-page/',option,name="option1"),
    path('login/',login_page,name="login1"),
    path('logout/',log_out,name="logout1"),
    #path('clientDashboard/',cli_page,name="dashboardClient"),

    #-----------------------------------------------

    #client app all urls 
   path('client_page/',cli_page,name="client1"),

   path('edit_client/',edit_client_details,name="editclient"),

   path('update_client/<id>/',update_client,name="updateclient"),

   path('delete_client/<id>/',deleteclient,name="deleteclient"),


   #--------------------------------------------------
   #project_management app all urls 

   path('project/<id>/',project_management,name="project_management"),
   path('uploadProjectPost/<id>/',upload_projectPost,name="upload_projectPost"),
    path('show_all_project/<id>/',show_all_project,name="show_all_project"),
    path('deletePost/<id>/',delete_post,name="delete_post"),
    path('update_post/<id>/',update_post,name="update_post"),
    path('hire_manage/<id>/',hire_manage,name="hire_manage"),


    #-----------------------------------------------------
    #freelancer app all urls 

    path('ApplyForProject/',apply_project,name="apply_project"),
    path('freelancer_page/',view_freelancer,name="view_freelancer"),
    path('select_freelancer/<id>/',select_freelancer,name="select_freelancer"),
    path('reject_freelancer/<id>/',reject_freelancer,name="reject_freelancer"),
    path('edit_freelancer/<id>/',edit_freelancer,name="edit_freelancer"),
    path('freelancer_page1/<id>/',freelancer1,name="freelancer1"),
    path('/delete_freelancer/<id>/',deletefreelancer,name="deletefreelancer")



] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
