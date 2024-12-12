# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from appportfolio.models import *
from django.contrib.auth.models import User

admin.site.site_header = "SITIO DE ADMINISTRACIÓN DE PORTFOLIO"  #este es el título
admin.site.site_title = "SITIO DE ADMINISTRACIÓN DE PORTFOLIO"
admin.site.index_title = "Bienvenidos al portal de Administración"

class CategoriaAdmin(admin.ModelAdmin):
	#list_display = [c.name for c in Categoria._meta.get_fields()]
	list_display = ['id','nombre_categoria']
	search_fields = ('id','nombre_categoria')
	list_filter   = ('id','nombre_categoria')
admin.site.register(Categoria, CategoriaAdmin)

class ExperienciaAdmin(admin.ModelAdmin):
	#list_display = [c.name for c in Experiencia._meta.get_fields()]
	list_display = ['id', 'empresa']
	search_fields = ('id','empresa')
	list_filter   = ('id','empresa')
admin.site.register(Experiencia, ExperienciaAdmin)

class EntrevistadorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Entrevistador._meta.get_fields() if hasattr(field, 'verbose_name')]
    search_fields = ('id','empresa')
admin.site.register(Entrevistador, EntrevistadorAdmin)

class ImagenAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Imagen._meta.get_fields() if hasattr(field, 'verbose_name')]
    search_fields = ('id','imagen')
admin.site.register(Imagen, ImagenAdmin)

class VideoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Video._meta.get_fields() if hasattr(field, 'verbose_name')]
    search_fields = ('id','video')
admin.site.register(Video, VideoAdmin)

admin.site.register(Curriculum)
admin.site.register(Estudio)
admin.site.register(DetalleCurriculumEstudio)
admin.site.register(DetalleCurriculumExperiencia)

class NoticiaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Noticia._meta.get_fields() if hasattr(field, 'verbose_name')]
    search_fields = ('id','titulo')
admin.site.register(Noticia, NoticiaAdmin)

@admin.register(Valoracion)
class ValoracionAdmin(admin.ModelAdmin):
    list_display = ('id', 'votos_entrevista', 'votos_empresa', 'media_aspectos', 'timestamp')
    readonly_fields = ('media_aspectos',)

    def save_model(self, request, obj, form, change):
        # Calcula automáticamente la media
        if obj.votos_entrevista and obj.votos_empresa:
            obj.media_aspectos = (obj.votos_entrevista + obj.votos_empresa) / 2
        super().save_model(request, obj, form, change)

admin.site.register(Mensaje)
