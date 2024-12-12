# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin , BaseUserManager , User
from django.utils import timezone

################################################
# 1 - Categoria
################################################
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField('Puesto de Trabajo',max_length=30,
                                        null=True, blank=True)

    class Meta:
        verbose_name = 'Categoria' #puede ser otro nombre
        verbose_name_plural = 'Categorias'
        ordering = ['nombre_categoria']

    def __str__(self):
        return "%s,%s" % (self.id,self.nombre_categoria)

################################################
# 2 - Experiencias
################################################
class Experiencia(models.Model):
    id = models.AutoField(primary_key=True)
    empresa = models.CharField('Empresa',max_length=50,null=True, blank=True)
    fecha_inicio= models.DateField('Fecha de Inicio',null=True, blank=True)
    fecha_fin = models.DateField('Fecha de Finalización', null=True, blank=True)
    observaciones = models.CharField('Funciones', max_length=50, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, related_name='expe_categoria', null=True, blank=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Experiencia' #puede ser otro nombre
        verbose_name_plural = 'Experiencias'
        ordering = ['empresa']

    def __str__(self):
        return "%s,%s,%s,%s,%s,%s % (self.id,self.empresa.self.fecha_inicio,self.fecha_fin,self.observaciones,self.categoria)"
        
################################################
# Los Entrevistadores
################################################
class Entrevistador(models.Model):
    id = models.AutoField(primary_key=True)
    avatar= models.ImageField('Avatar', blank=True, null = True, upload_to="media/")
    empresa = models.CharField('Empresa',max_length=30,null=True, blank=True)
    fecha_entrevista= models.DateField('Fecha Entrevista',null=True, blank=True)
    conectado = models.BooleanField('Conectado',null=True, blank=True) 
    seleccionado = models.BooleanField('Seleccionado',null=True, blank=True) 
    # forteigns keys requerido desde django 2.0
    user = models.ForeignKey(User, related_name='entrevistados_usuario', 
    null=True, blank=True, on_delete=models.PROTECT)  

    class Meta:
        verbose_name = 'Entrevistador'  
        verbose_name_plural = 'Entrevistadores'
        ordering = ['empresa']

    def __str__(self):
        return "%s,%s,%s,%s,%s,%s" % (self.id, self.empresa, self.fecha_entrevista, 
        self.conectado, self.seleccionado, self.user)        

################################################
# Imagenes
################################################
class Imagen(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.ImageField("Imagen", blank=True, null=True, upload_to="imagenes/")
    comentario = models.CharField('Comentario',max_length=100,null=True, blank=True)

    class Meta:
        verbose_name = 'Imagen' 
        verbose_name_plural = 'Imagenes'
        ordering = ['id']

    def __str__(self):
        return "%s,%s,%s" % (self.id,self.imagen,self.comentario)
        
################################################
# Videos
################################################
class Video(models.Model):
    id = models.AutoField(primary_key=True)
    video = models.FileField("Video", blank=True, null=True, upload_to="videos/")
    comentario = models.CharField('Comentario',max_length=100,null=True, blank=True)

    class Meta:
        verbose_name = 'Video' 
        verbose_name_plural = 'Videos'
        ordering = ['id']

    def __str__(self):
        return "%s,%s,%s" % (self.id,self.video,self.comentario)    

#nuevas

class Estudio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Curriculum(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    ap1 = models.CharField(max_length=100)
    ap2 = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.ap1} {self.ap2}"


class DetalleCurriculumEstudio(models.Model):
    id = models.AutoField(primary_key=True)
    estudio = models.ForeignKey(Estudio, on_delete=models.CASCADE)
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.estudio.nombre} para {self.curriculum.nombre}"


class DetalleCurriculumExperiencia(models.Model):
    id = models.AutoField(primary_key=True)
    experiencia = models.ForeignKey(Experiencia, on_delete=models.CASCADE)
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.experiencia.empresa} para {self.curriculum.nombre}"
        
class Noticia(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    imagen= models.ImageField('Imagen', blank=True, null = True, upload_to="media/")

    def __str__(self):
        return self.titulo        
        
'''
class Valoracion(models.Model):
    id = models.AutoField(primary_key=True)
    votos_entrevista = models.IntegerField("votos_entrevista", null=True, blank=True) #son las estrellas
    votos_empresa = models.IntegerField("votos_empresa", null=True, blank=True) #son las estrellas
    media_aspectos = models.IntegerField("Media Aspectos", null=True, blank=True)  # media estrellas total
    entrevista = models.CharField('Descripción Entrevista', max_length=200, null=True, blank=True)
    empresa = models.CharField('Descripción Empresa', max_length=200, null=True, blank=True)
    numvaloraciones = models.IntegerField('Num Valoraciones',null=True, blank=True)  
    timestamp = models.DateTimeField("Fecha", default=timezone.now)
    entrevistador = models.ForeignKey(Entrevistador, related_name='entrevistadores',null=True, blank=True, on_delete=models.PROTECT)  
    class Meta:
        verbose_name = "Valoracion"  
        verbose_name_plural = "Valoraciones"
        ordering = ['id']
    def __str__(self):
        return '%s,%s,%s,%s,%s,%s' % (self.id, self.votos_entrevista, self.votos_empresa, self.media_aspectos,self.entrevista,self.timestamp)
'''

class Valoracion(models.Model):
    id = models.AutoField(primary_key=True)
    votos_entrevista = models.DecimalField("Votos Entrevista", max_digits=3, decimal_places=1, null=True, blank=True) 
    votos_empresa = models.DecimalField("Votos Empresa", max_digits=3, decimal_places=1, null=True, blank=True)  
    media_aspectos = models.DecimalField("Media Aspectos", max_digits=3, decimal_places=1, null=True, blank=True)  
    entrevista = models.CharField('Descripción Entrevista', max_length=200, null=True, blank=True)
    empresa = models.CharField('Descripción Empresa', max_length=200, null=True, blank=True)
    numvaloraciones = models.IntegerField('Num Valoraciones', null=True, blank=True)
    timestamp = models.DateTimeField("Fecha", default=timezone.now)

    def __str__(self):
        return f"{self.id}, {self.votos_entrevista}, {self.votos_empresa}, {self.media_aspectos}, {self.entrevista}, {self.timestamp}"
        
class Mensaje(models.Model):
    remitente = models.ForeignKey(User, related_name='mensajes_enviados', on_delete=models.CASCADE)
    destinatario = models.ForeignKey(User, related_name='mensajes_recibidos', on_delete=models.CASCADE)
    contenido = models.TextField('Contenido del mensaje')
    fecha_envio = models.DateTimeField('Fecha de envío', auto_now_add=True)
    leido = models.BooleanField('Leído', default=False)

    class Meta:
        ordering = ['fecha_envio']

    def __str__(self):
        return f"De: {self.remitente.username} Para: {self.destinatario.username} - {self.contenido[:30]}"
        
        