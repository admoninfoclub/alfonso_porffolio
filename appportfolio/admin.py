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
