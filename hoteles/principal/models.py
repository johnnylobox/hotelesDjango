from __future__ import unicode_literals
from django.db import models

class Pais(models.Model):
	id_pais = models.Autofield(primary_key=True)
	nombre_pais = models.CharField(max_lenght=45)
	def __str__(self):
		return self.nombre_pais

	class Meta:
		ordering = ['nombre_pais']
		verbose_name = ['Pais']
		db_table = 'pais'
		verbose_name_plural = "Paises"

class Estado(models.Model):
	id_estado = models.Autofield(primary_key=True)
	nombre_estado = models.CharField(max_lenght=100)
	pais = models.ForeignKey('Pais', 
		models.DO_NOTHING, 
		db_column='id_pais', 
		blank=True, 
		null=True, 
		verbose_name = "Pais")
	def __str__(self):
		return self.nombre_estado

	class Meta:
		ordering = ['nombre_estado']
		verbose_name = ['Estado']
		db_table = 'estado'
		verbose_name_plural = "Estados"

class Ciudad(models.Model):
	id_ciudad = models.Autofield(primary_key=True)
	nombre_ciudad = models.CharField(max_lenght=45)
	estado = models.ForeignKey('Estado', 
		models.DO_NOTHING, 
		db_column='id_estado', 
		blank=True, 
		null=True, 
		verbose_name = "Estado")
	def __str__(self):
		return self.nombre_ciudad

	class Meta:
		ordering = ['nombre_ciudad']
		verbose_name = ['Ciudad']
		db_table = 'ciudad'
		verbose_name_plural = "Ciudades"

class Municipio(models.Model):
	id_municipio = models.Autofield(primary_key=True)
	nombre_municipio = models.CharField(max_lenght=45)
	ciudad = models.ForeignKey('Ciudad', 
		models.DO_NOTHING, 
		db_column='id_ciudad', 
		blank=True, 
		null=True, 
		verbose_name = "Ciudad")
	def __str__(self):
		return self.nombre_municipio

	class Meta:
		ordering = ['nombre_municipio']
		verbose_name = ['Municipio']
		db_table = 'municipio'
		verbose_name_plural = "Municipios"

class Parroquia(models.Model):
	id_parroquia = models.Autofield(primary_key=True)
	nombre_parroquia = models.CharField(max_lenght=45)
	municipio = models.ForeignKey('Municipio', 
		models.DO_NOTHING, 
		db_column='id_municipio', 
		blank=True, 
		null=True, 
		verbose_name = "Municipio")
	def __str__(self):
		return self.nombre_parroquia

	class Meta:
		ordering = ['nombre_parroquia']
		verbose_name = ['Parroquia']
		db_table = 'parroquia'
		verbose_name_plural = "Parroquias"

class CalleAvenida(models.Model):
	id_calle_avenida = models.Autofield(primary_key=True)
	nombre_calle_avenida = models.TextField()
	parroquia = models.ForeignKey('Parroquia', 
		models.DO_NOTHING, 
		db_column='id_parroquia', 
		blank=True, 
		null=True, 
		verbose_name = "Parroquia")
	def __str__(self):
		return self.nombre_calle_avenida

	class Meta:
		ordering = ['nombre_calle_avenida']
		verbose_name = ['Dirección: Calle y Avenida']
		db_table = 'calle_avenida'
		verbose_name_plural = "Dirección: Calles y Avenidas"


class Hotel(models.Model):
	id_hotel = models.Autofield(primary_key=True)
	nombre_hotel = models.CharField(max_lenght=45)
	ubicacion = models.ForeignKey('CalleAvenida', 
		models.DO_NOTHING, 
		db_column='id_calle_avenida', 
		blank=True, 
		null=True, 
		verbose_name = "Dirección: Calle y Avenida")
	def __str__(self):
		return self.nombre_hotel

	class Meta:
		ordering = ['nombre_hotel']
		verbose_name = ['Hotel']
		db_table = 'hotel'
		verbose_name_plural = "Hoteles"


class Servicio(models.Model):
	id_servicio = models.Autofield(primary_key=True)
	nombre_servicio = models.CharField(max_lenght=45)
	precio = models.DecimalField(max_digits=None, decimal_places=None)
	def __str__(self):
		return self.nombre_servicio

	class Meta:
		ordering = ['nombre_servicio']
		verbose_name = ['Servicio']
		db_table = 'servicio'
		verbose_name_plural = "Servicios"
