"""finalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from fapp.views import addproject_form,addproject_database,addproject_table,home_view,\
    loginAuth,registerAuth,profile_user,comment,add_comment,donate_form,add_donnate,donateprojects,remove_projects
urlpatterns = [
    path('admin/', admin.site.urls),
    path('addproject_form/',addproject_form,name='project_form'),
    path('addproject_database/',addproject_database,name='addproject_database'),
    path('addproject_home/',addproject_table,name='homepage'),
    #path('register_form/',register_form),
    path('register/',registerAuth,name='register'),
    #path('login_form/',login_form),
    #path('login_user/',log_user,name='login_user'),
    path('', home_view, name="home"),
    path('signup/', loginAuth, name="signup"),
path('profile/', profile_user, name="profile"),
path('pcomment/<int:id>', comment, name="pcomment"),
path('addcomment/<int:id>', add_comment, name="addcomment"),
path('donnate_form/<int:id>', donate_form, name="donnate_form"),
path('add_donnate/<int:id>', add_donnate, name="add_donnate"),
path('donnate_projects/<int:id>', donateprojects, name="donnate_projects"),
path('delete_projects/<int:id>/<int:totaldonnates>', remove_projects, name="remove_projects"),
]
