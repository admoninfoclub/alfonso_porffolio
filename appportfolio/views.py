# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from django.http  import HttpResponse
from appportfolio.models import *
#from .models import *

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger	#paginacion
from django.contrib.auth import authenticate, get_user_model, login,logout  #todas son por defecto
from django.contrib.auth.decorators import login_required
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth.models import User
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

#email
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages

#curriculum con reportlab
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
import os

#para el chat
from django.http import JsonResponse



################################################
# 1 - home
################################################

def home(request):
    print("hola estoy en home") 
    nombre='Alfonso'
    context = {'nombre': nombre}
    return render(request, 'home.html', context=context)

################################################
# 2 - experiencias
################################################

def experiencias(request):
    lista_experiencias = Experiencia.objects.all()  # select * from Experiencias;
    page = request.GET.get('page')
    paginator = Paginator(lista_experiencias, 2)  # 2 registros por página
    if page == None:
        print(" page recibe fuera de get o post NONE=" + str(page))
        page = paginator.num_pages
        request.session["pagina"] = page
    else:
        print(" page recibe esle del none de geo o post=" + str(page))
        request.session["pagina"] = page

    if request.method == 'GET':
        pagina = request.session["pagina"]
        print(" page recibe en GET=" + str(pagina))
    if request.method == 'POST':
        pagina = request.session["pagina"]
        print(" page recibe en POST=" + str(pagina))

    if "pagina" in request.session:
        page = request.session["pagina"]
        print(" page recibe de sesion=" + str(page))

    try:
        lista_experiencias = paginator.get_page(page)
    except PageNotAnInteger:
        lista_experiencias = paginator.page(1)
    except EmptyPage:
        lista_experiencias = paginator.page(paginator.num_pages)

    context = {'lista_experiencias': lista_experiencias}
    return render(request, 'experiencias.html', context=context)

################################################
# 3 -  estudios
################################################

def estudios(request):
    lista_estudios = ''
    context = {'lista_estudios': lista_estudios}
    return render(request, 'estudios.html', context=context)

################################################
# 4 -  habilidades
################################################

def habilidades(request):
    #lista_habilidades = Habilidad.objects.all()
    lista_habilidades =""
    context = {'lista_habilidades': lista_habilidades}
    return render(request, 'estudios.html', context=context)

################################################
# 5 -  sobremi
################################################

def sobremi(request):
    print("hola estoy en sobremi") 
    nombre='ALFONSO'
    edad=59
    telefono='674834567'
    cargo='PEON CAMINERO'
    #select * from Categoria
    listaCategorias=Categoria.objects.all().order_by('-nombre_categoria')
    for r in listaCategorias:
        print(str(r.nombre_categoria))
    context = {'nombre':nombre, 'edad':edad, 'telefono':telefono,
               'cargo':cargo,'listaCategorias':listaCategorias}
    return render(request, 'sobremi.html', context=context)

################################################
# 6 -  diplomas
################################################

def diplomas(request):
    lista_diplomas = ''
    context = {'lista_diplomas': lista_diplomas}
    return render(request, 'diplomas.html', context=context)

################################################
# 7 -  certificados
################################################

def certificados(request):
    lista_certificados = ''
    context = {'lista_certificados': lista_certificados}
    return render(request, 'certificados.html', context=context)

################################################
# 8 -  enlaces
################################################

def enlaces(request):
    lista_urls = ''
    context = {'lista_urls': lista_urls}
    return render(request, 'enlaces.html', context=context)

'''
def formacion(request):
    formaciones = Formacion.objects.all().order_by('id')
    for f in formaciones:
        print(str(f.id) + " " + str(f.estudio) + str(f.anyo))
    context = {'formaciones': formaciones}
    return render(request, 'formacion.html', context=context)
'''

def ver_experiencia(request,id):
    expe_id=id
    experiencia = Experiencia.objects.get(id=expe_id)
    context = {'experiencia': experiencia}
    return render(request, 'ver_experiencia.html',context=context)

# ####################### NUEVAS ######################################################

def Login(request):
    print("Login")
    request.user.username = nombre
    request.user.password = clave
    
    idUsuario=0
    cUsuario=""
    cUsuario=str(request.user)
    entrevistador=User.objects.get(username=cUsuario)
    nombreusuario=cUsuario
    idUsuario=entrevistador.id
    print("\nUSUARIO ACTIVO = "+str(request.user)+"\nID USUARIO ACTIVO = "+str(idUsuario))
    context = {'nombre': nombre, 'clave': clave,'entrevistador':entrevistador}
    return render(request, 'home.html', context=context)

def eliminarExperiencia(request, pk):
    print("ELIMINAR")
    expe_id=pk
    experiencia = Experiencia.objects.get(id=expe_id)
    if request.method == 'POST':
        experiencia.delete()
        return redirect('home')
    return render(request, 'eliminar_experiencia.html', {'experiencia': experiencia}) 
    
def login_view(request):
    print("Logi_view")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            actual=request.user   #usuario actual
            idusuario=0
            idusuario=actual.id 
            request.session['idusuario']=idusuario
            print("idusuario="+str(idusuario))
            entrevistador=Entrevistador.objects.get(user=idusuario)
            idEntrevistador=entrevistador.id
            print("idEntrevistador="+str(idEntrevistador))
            print("FOTO="+str(entrevistador.avatar))
            fotoperfil = settings.MEDIA_URL + str(entrevistador.avatar) if entrevistador.avatar else settings.MEDIA_URL +"MONEDA3.jpg"
            print("avatar=" + str(fotoperfil))
            context = {'fotoperfil':fotoperfil}
            return render(request, 'home.html', context=context)
            #return redirect('home')  
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'login.html')
    
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('login')  # Redirige al login una vez registrado
    return render(request, 'register.html')    
    
#CERRAR LA SESION DEL USUARIO
def cerrar(request):
    username = request.user.username
    password = request.user.password
    idusuario = request.user.id
    print("logout.................. " + username + "clave=" + str(password) + "id=" + str(idusuario))
    user = authenticate(request, username=username, password=password)
    # desconectamos al usuario
    logout(request)
    return redirect('/')    

@csrf_exempt    
def subir_imagenes(request):
    if request.method == 'POST':
        imagenes = request.FILES.getlist('imagenes')
        comentario = request.POST.get('comentario')
        for imagen in imagenes:
            if imagen.name.endswith(('.png', '.jpg', '.jpeg', '.gif','.jfif')):
                img=Imagen() 
                img.imagen=imagen
                img.comentario=comentario
                img.save()
        return redirect('subir_imagenes')

    imagenes = Imagen.objects.all()
    return render(request, 'subir_imagenes.html', {'imagenes': imagenes})
    
def subir_videos(request):
    if request.method == 'POST' and request.FILES['videos']:
        videos = request.FILES.getlist('videos')
        
        for video in videos:
            if video.name.endswith(('.mp3','.mp4', '.mov', '.avi', '.mkv')):
                v=Video() 
                v.video=video
                v.save()
        return redirect('subir_videos')

    videos = Video.objects.all()
    return render(request, 'subir_videos.html', {'videos': videos})    

def eliminar_imagen(request, imagen_id):
    imagen = get_object_or_404(Imagen, id=imagen_id)
    if request.method == 'POST':
        imagen.delete()
        return redirect('subir_imagenes')  # Redirige a la galería de imágenes   
    return redirect('subir_imagenes')  # Redirige a la galería de imágenes   
          
@csrf_exempt          
def editar_imagen(request, imagen_id):
    imagen = get_object_or_404(Imagen, id=imagen_id)
    nuevo_comentario = request.POST.get('nuevo_comentario')
    
    if request.method == 'POST' and request.FILES.get('nueva_imagen'):
        # Actualizamos la imagen
        imagen.imagen = request.FILES['nueva_imagen']
        imagen.comentario=nuevo_comentario
        imagen.save()
        return redirect('subir_imagenes')  # Redirige a la galería de imágenes

    return redirect('subir_imagenes')        
            
def eliminar_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    if request.method == 'POST':
        video.delete()
        return redirect('subir_videos')   
    return redirect('subir_videos')  
            
def editar_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    
    if request.method == 'POST' and request.FILES.get('nuevo_video'):
        # Actualizamos la imagen
        video.video = request.FILES['nuevo_video']
        video.save()
        return redirect('subir_videos')  

    return redirect('subir_videos')        

def contacto(request):
    if request.method =="POST":
        nombre= request.POST.get('nombre')
        email= request.POST.get("email")
        asunto= request.POST.get("asunto")
        mensaje= request.POST.get("mensaje")
        
        context={'nombre':nombre,'email':email,'asunto':asunto,'mensaje':mensaje}
        template = render_to_string('email_template.html',context=context)
        
        email= EmailMessage(asunto,template,
        settings.EMAIL_HOST_USER,['infoclub3000@gmail.com'])
        
        email.fail_silenty=False #que no marque error en gmail
        email.send()
        
        messages.success(request,'Se ha enviado tu email')
        return redirect('home')
    return render(request, 'correo.html')        
        
        
#nuevos controladores 14/11/2024

# Vista para agregar un curriculum (solo teléfono y email)
def agregar_curriculum(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        ap1 = request.POST.get('ap1')
        ap2 = request.POST.get('ap2')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        
        curriculum = Curriculum(nombre=nombre, ap1=ap1, ap2=ap2, email=email, telefono=telefono)
        curriculum.save()
        
        return redirect('ver_curriculum', pk=curriculum.pk)

    return render(request, 'agregar_curriculum.html')


# Vista para ver un curriculum
def ver_curriculum(request, pk):
    curriculum = get_object_or_404(Curriculum, pk=pk)
    estudios = DetalleCurriculumEstudio.objects.filter(curriculum=curriculum)
    experiencias = DetalleCurriculumExperiencia.objects.filter(curriculum=curriculum)
    context= {'curriculum': curriculum,'estudios': estudios,'experiencias': experiencias,}
    return render(request, 'ver_curriculum.html', context=context)

def generar_pdf(request, pk):
    curriculum = get_object_or_404(Curriculum, pk=pk)
    estudios = DetalleCurriculumEstudio.objects.filter(curriculum=curriculum)
    experiencias = DetalleCurriculumExperiencia.objects.filter(curriculum=curriculum)

    # Crear la respuesta HttpResponse con tipo de contenido PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="curriculum_{curriculum.nombre}_{curriculum.ap1}.pdf"'

    # Crear un objeto canvas de ReportLab para generar el PDF
    c = canvas.Canvas(response, pagesize=letter)
    width, height = letter  # Tamaño de la página

    # Cargar imagen de avatar
    try:
        #avatar_path = "C:/vportfolio/pportfolio/media/MEDIA/moneda3.jpg"  
        avatar_path = os.path.join(settings.MEDIA_ROOT, "MEDIA/moneda3.jpg")
        avatar = ImageReader(avatar_path)
        c.drawImage(avatar, width - 150, height - 150, width=100, height=100)
    except Exception as e:
        print(f"No se pudo cargar la imagen: {e}")   
        pass  # Si no se encuentra la imagen, el PDF se generará sin ella

    # Título del currículum en color
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(colors.HexColor("#4B8BBE"))  # Cambia a cualquier color hex que prefieras
    c.drawString(100, height - 100, f"Currículum de {curriculum.nombre} {curriculum.ap1}")

    # Información de contacto en color diferente
    c.setFont("Helvetica", 12)
    c.setFillColor(colors.HexColor("#306998"))  # Otro color para variar
    c.drawString(100, height - 130, f"Email: {curriculum.email}")
    c.drawString(100, height - 150, f"Teléfono: {curriculum.telefono}")

    # Sección de estudios en otro color
    y_position = height - 200
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(colors.HexColor("#FFD43B"))
    c.drawString(100, y_position, "Estudios:")

    # Mostrar cada estudio con detalles
    c.setFont("Helvetica", 12)
    y_position -= 20
    for estudio in estudios:
        c.setFillColor(colors.black)
        c.drawString(100, y_position, f"{estudio.titulo} en {estudio.institucion} ({estudio.fecha_inicio} - {estudio.fecha_fin})")
        y_position -= 20

    # Sección de experiencia laboral
    y_position -= 40
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(colors.HexColor("#306998"))
    c.drawString(100, y_position, "Experiencia laboral:")

    y_position -= 20
    c.setFont("Helvetica", 12)
    for experiencia in experiencias:
        c.setFillColor(colors.black)
        c.drawString(100, y_position, f"{experiencia.puesto} en {experiencia.empresa} ({experiencia.fecha_inicio} - {experiencia.fecha_fin})")
        y_position -= 20

    # Finalizar el PDF
    c.showPage()  # Si tienes más páginas
    c.save()

    return response
    
                
# Vista para ver las noticias
def lista_noticias(request):
    noticias = Noticia.objects.all().order_by('-fecha_creacion')
    return render(request, 'lista_noticias.html', {'noticias': noticias})

# Vista para crear una nueva noticia
def crear_noticia(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        contenido = request.POST.get('contenido')
        imagen = request.FILES.get('imagen')
        
        if titulo and contenido:
            noticia = Noticia.objects.create(titulo=titulo, contenido=contenido,imagen=imagen)
            return redirect('lista_noticias')
        else:
            return HttpResponse("Error: El título y el contenido son obligatorios.", status=400)
    
    return render(request, 'crear_noticia.html')                    
    
def listar_valoraciones(request):
    valoraciones = Valoracion.objects.all()
    return render(request, 'list.html', {'valoraciones': valoraciones})

'''
def actualizar_valoracion(request, pk):
    valoracion = get_object_or_404(Valoracion, pk=pk)
    if request.method == 'POST':
        votos_entrevista = int(request.POST.get('votos_entrevista', valoracion.votos_entrevista))
        votos_empresa = int(request.POST.get('votos_empresa', valoracion.votos_empresa))

        # Actualizar los votos y recalcular la media
        valoracion.votos_entrevista = votos_entrevista
        valoracion.votos_empresa = votos_empresa
        valoracion.media_aspectos = (votos_entrevista + votos_empresa) / 2
        valoracion.save()

        return redirect('listar_valoraciones')

    return render(request, 'update.html', {'valoracion': valoracion})
'''    
def actualizar_valoracion(request, pk):
    valoracion = get_object_or_404(Valoracion, pk=pk)
    if request.method == 'POST':
        votos_entrevista = int(request.POST.get('votos_entrevista', valoracion.votos_entrevista))
        votos_empresa = int(request.POST.get('votos_empresa', valoracion.votos_empresa))

        # Actualizar los votos y recalcular la media
        valoracion.votos_entrevista = votos_entrevista
        valoracion.votos_empresa = votos_empresa
        valoracion.media_aspectos = (votos_entrevista + votos_empresa) / 2
        valoracion.save()

        return redirect('listar_valoraciones')

    return render(request, 'update.html', {'valoracion': valoracion})    
    
def añadir_valoracion(request):
    if request.method == 'POST':
        entrevista = request.POST.get('entrevista')
        empresa = request.POST.get('empresa')
        votos_entrevista = int(request.POST.get('votos_entrevista', 0))
        votos_empresa = int(request.POST.get('votos_empresa', 0))
        
        # Calcular la media de los aspectos
        media_aspectos = (votos_entrevista + votos_empresa) / 2
        
        # Crear y guardar la nueva valoración
        nueva_valoracion = Valoracion.objects.create(
            entrevista=entrevista,
            empresa=empresa,
            votos_entrevista=votos_entrevista,
            votos_empresa=votos_empresa,
            media_aspectos=media_aspectos
        )
        return redirect('listar_valoraciones')

    return render(request, 'add.html')    
    
@login_required
def chat_view(request, entrevistador_id):
    entrevistador = get_object_or_404(Entrevistador, id=entrevistador_id)
    mensajes = Mensaje.objects.filter(
        (models.Q(remitente=request.user) & models.Q(destinatario=entrevistador.user)) |
        (models.Q(remitente=entrevistador.user) & models.Q(destinatario=request.user))
    )
    # Agregar la propiedad 'clase' para usarla en el template
    for mensaje in mensajes:
        mensaje.clase = 'enviado' if mensaje.remitente == request.user else 'recibido'
    
    # Renderizar solo el chat para la respuesta AJAX
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'mensajesHtml': render_to_string('chat_mensajes.html',
                                             {'mensajes': mensajes}),
        })

    return render(request, 'chat.html', {'entrevistador': entrevistador,
                                         'mensajes': mensajes})
 

@login_required
def enviar_mensaje(request):
    if request.method == 'POST':
        contenido = request.POST.get('contenido')
        destinatario_id = request.POST.get('destinatario_id')
        destinatario = get_object_or_404(User, id=destinatario_id)

        mensaje = Mensaje.objects.create(
            remitente=request.user,
            destinatario=destinatario,
            contenido=contenido
        )
        return JsonResponse({'status': 'success', 'mensaje': mensaje.contenido,
                             'fecha_envio': mensaje.fecha_envio})
    return JsonResponse({'status': 'error', 'message': 'Método no permitido'})


