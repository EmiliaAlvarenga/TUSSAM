#!/usr/bin/env python


from lxml import etree
from suds.client import Client
import suds

url='http://www.infobustussam.com:9001/services/dinamica.asmx?wsdl'
cliente = Client(url, retxml=True)
print '''
	Informacion de lineas de empresa TUSSAM
'''
linea=raw_input("Linea :")
try:
	respuesta = cliente.service.GetStatusLinea(linea)
	print """
	"""
except suds.WebFault as error:
	print "Error la linea no existe"
else:
	raiz=etree.fromstring(respuesta)
	raiz2=raiz[0][0]
	ns="{http://tempuri.org/}"
	find_activos=raiz2.find(ns+"GetStatusLineaResult/"+ns+"activos")
	activos=find_activos.text
	find_frecuencia=raiz2.find(ns+"GetStatusLineaResult/"+ns+"frec_bien")
	buenafrec=find_frecuencia.text
	find_graves=raiz2.find(ns+"GetStatusLineaResult/"+ns+"graves")
	graves=find_graves.text
	print "El numero de coches es: %s"%activos
	print "El numero de coches con buena frecuencia: %s"%buenafrec
	print "El numero de incidencias graves en la linea",linea,"es: ",graves
