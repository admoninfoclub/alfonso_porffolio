# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

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

