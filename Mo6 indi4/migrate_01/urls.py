from django.urls import path
from . import views
from django.contrib.auth import views as sessions

app_name = 'migrate_01'
urlpatterns = [
   # path('asignatura/', views.asignaturax , name = 'asignatura'),
    path('profesor/', views.profesorx , name = 'profesor' ),
    path('alumno/', views.mostrar_alumnos, name = 'alumno'),
    #path('adm_asig/', views.adm_asig, name = 'admasig'),
    #path('adm_profe/', views.adm_profe, name = 'admprofe'),
    path('login/', sessions.LoginView.as_view(template_name= 'migrate_01/login.html'), name = 'login'),
    path('asignatura/', views.Asignatura1.as_view(), name = 'asignature'),
    
]