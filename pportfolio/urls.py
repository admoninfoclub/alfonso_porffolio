# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.urls import path,include,re_path
from appportfolio import views
from appportfolio.views import *

# servicio de ficheros estáticos durante el desarrollo
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
# servicio de ficheros estáticos durante el servidor
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.home,name='home'),
    #re_path('',views.home,name='home'),
    path('sobremi/',views.sobremi,name='sobremi'),
    re_path('experiencias/',views.experiencias,name='experiencias'),
    re_path('estudios/',views.estudios,name='estudios'),
    re_path('habilidades/',views.habilidades,name='habilidades'),
    re_path('diplomas',views.diplomas,name='diplomas'),
    re_path('certificados/',views.certificados,name='certificados'),  #para home.html
    re_path('enlaces/',views.enlaces,name='enlaces'), 
    #re_path('cerrar/',views.cerrar,name='cerrar'),
    #re_path('Login/', views.Login,name='Login'),
    #re_path('ver_experiencia/<int:id>/', views.ver_experiencia,name='ver_experiencia'),
    re_path(r'^(?P<id>\d+)/ver_experiencia$', views.ver_experiencia,name='ver_experiencia'),

    re_path(r'^cerrar/$', views.cerrar, name='cerrar'),
    path('accounts/', include('allauth.urls')),
    #re_path(r'^login/$', auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    #re_path(r'^logout/$', auth_views.LogoutView.as_view(), name="logout"),  # cerrar sistema
    #path('signup/', views.signup, name='signup'), # acceso al sistema
    path('Login/', views.Login, name='Login'),
    #path('Register/', views.Register, name='Register'),
    #path('Signup/', views.Signup, name='Signup'),
    
    #re_path(r'^login/$',auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),  #acceso al sistema
    
    path('eliminarExperiencia/<int:pk>/', views.eliminarExperiencia, name='eliminarExperiencia'),
    #path('crear/', views.crear_empleado, name='crear_empleado'),
    #path('actualizar/<int:pk>/', views.actualizar_empleado, name='actualizar_empleado'),
    
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('subir_imagenes/', subir_imagenes, name='subir_imagenes'),
    path('subir_videos/', subir_videos, name='subir_videos'),
    
    path('imagen/editar/<int:imagen_id>/', views.editar_imagen, name='editar_imagen'),
    path('imagen/eliminar/<int:imagen_id>/', views.eliminar_imagen, name='eliminar_imagen'),
    
    path('video/editar/<int:video_id>/', views.editar_video, name='editar_video'),
    path('video/eliminar/<int:video_id>/', views.eliminar_video, name='eliminar_video'),
    path('contacto/', views.contacto, name='contacto'),
    
    path('agregar/', views.agregar_curriculum, name='agregar_curriculum'),
    path('ver/<int:pk>/', views.ver_curriculum, name='ver_curriculum'),
    path('generar-pdf/<int:pk>/', views.generar_pdf, name='generar_pdf'),
    
    path('lista_noticias/', views.lista_noticias, name='lista_noticias'),
    path('crear_noticia/', views.crear_noticia, name='crear_noticia'),
    
    path('listar_valoraciones/', views.listar_valoraciones, name='listar_valoraciones'),
    path('actualizar_valoracion/<int:pk>/edit/', views.actualizar_valoracion, name='actualizar_valoracion'),
    path('añadir_valoracion/add/', añadir_valoracion, name='añadir_valoracion'),
    
    path('chat_view/<int:entrevistador_id>/', views.chat_view, name='chat_view'),
    path('chat/enviar/', views.enviar_mensaje, name='enviar_mensaje'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$',serve,{
       'document_root': settings.MEDIA_ROOT,
    })
]           
