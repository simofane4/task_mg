from django.contrib import admin
from django.urls import path
from home.views import home ,event,pers,project,task,login,forgotpass,register, project_view,profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('event',event,name="event"),
    path('pers',pers , name='pers'),
    path('project',project ,name='project'),
    path('task',task,name='task'),
    path('login',login,name='login'),
    path("register",register, name="register"),
    path("forgotpass",forgotpass, name="forgotpass"),
    path("project-view", project_view, name="project_view"),
    path("profile", profile, name='profile')
]
