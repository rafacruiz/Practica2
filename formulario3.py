#!/usr/bin/python
# -*- coding: utf-8 -*-

import web
import re
from web import form

# Creamos el formulario. Su ámbito es global

formularionuevo= form.Form( 
    form.Textbox("nombre", form.notnull, description = "Nombre:", value="xxxx"),
    form.Textbox("apellido", form.notnull, description = "Apellido:", value="xxxx"),
    form.Textbox("email", form.notnull, description = "E-mail:", value="xxxx"),
    form.Textbox("nvisa", form.notnull, description = "NºVisa:", value="0000"),
    form.Dropdown("dia", [(1, '1'), (2, '2'), (3, '3'), (4, '4'),(5, '5'),(6, '6'),(7, '7'),(8, '8'),(9, '9'),(10, '10'),(11, '11'),(12, '12'),(13, '13'),(14, '14'),(15, '15'),(16, '16'),(17, '17'),(18, '18'),(19, '19'),(20, '20'),(21, '21'),(22, '22'),(23, '23'),(24, '24'),(25, '25'),(26, '26'),(27, '27'),(28, '28'),(29, '29'),(30, '30'),(31, '31')]),
    form.Dropdown("mes", [('enero', 'Enero'), ('febrero', 'Febrero'), ('marzo', 'Marzo'), ('abril', 'Abril'),('mayo', 'Mayo'),('junio', 'Junio'),('julio', 'Julio'),('agosto', 'Agosto'),('septiembre', 'Septiembre'),('octubre', 'Octubre'), ('noviembre', 'Noviembre'),('diciembre', 'Diciembre')]),
    form.Dropdown("anio", [(2003, '2003'),(2004, '2004'),(2005, '2005'),(2006, '2006'),(2007, '2007'),(2008, '2008'),(2009, '2009'),(2010, '2010'),(2011, '2011'), (2012, '2012'), ('2013', '2013')]),
    form.Textarea("direccion", form.notnull, description = "Direccion:", value="xxxx"),
    form.Password("contrasena", form.notnull, description = "Contraseña:", value="xxxx"),
    form.Password("verificacion", form.notnull, description = "Verificar Contraseña:", value="xxxx"),
    form.Radio("forma", [('contra', 'Contra Reembolso'), ('visa', 'Visa')]),
    form.Checkbox("valor", form.Validator("Acepta la clausulas", lambda i:"valor" not in i), description = "Aceptación de clausulas:"),
    form.Button("Enviar"),
) 

# Una clase para generar un formulario
class Formulario:        
    # El método GET devolverá el formulario para que lo rellene el usuario
    def GET(self):
        form = formularionuevo()  # Hacemos una copia del formulario para evitar que se use la misma información en distintas llamadas

        # Creamos el HTML de la página "a pelo". Usualmente no se hará así (utilizaremos templates)
        html = """
        <html>
          <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
            <title>Formulario</title>
          </head>
          <body>
	    <h1>Introduzca datos en el formulario:</h1>
            <form method="POST">
            %s
            </form>
          </body>
        </html>""" % (form.render())
        
        return html
      
    # El método POST devolverá la página donde se gestionan los datos introducidos por el usuario
    def POST(self): 
      form = formularionuevo() 
  
      if not form.validates():
	return form.render()
      else:
# Comprueba si es un email
	def email(string):
	  a = re.compile(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b')
	  return a.match(string)
	  
# Comprueba si es un numero de tarjeta visa
	def tarjetaCredito(string):
	  a = re.compile(r'([0-9]{4}) ([0-9]{4}) ([0-9]{4}) ([0-9]{4})|([0-9]{4})-([0-9]{4})-([0-9]{4})-([0-9]{4})')
	  return a.match(string)
	  
  ###################################################################################################################
  
	line = form.d.email
	if email(line) == None:
	    return "<html><title>Error</title><body><h1>Error formato e-mail</h1>Formato de e-mail incorrecto</body></html>"
        
        num = form.d.nvisa
        if tarjetaCredito(num) == None:
	    return "<html><title>Error</title><body><h1>Error formato número Visa</h1>Formato del número de Visa es incorrecto</body></html>"
        
        dat = int(form.d.anio)
        if (dat % 4 == 0 and not dat % 100 == 0) or dat % 400 == 0:
	  day = int(form.d.dia)
	  if (form.d.mes == 'febrero' and day >= 29):
	    return "<html><title>Error</title><body><h1>Error formato Fecha Incorrecto</h1>Formato de fecha erroneo, año no bisiesto</body></html>"
        
        if (form.d.contrasena != form.d.verificacion):
            return "<html><title>Error</title><body><h1>Error Contraseña</h1>La contraseña no coincide con la validadación</body></html>"
            
        if (len(form.d.contrasena) <= 6 and len(form.d.verificacion) <= 6):
	    return "<html><title>Error</title><body><h1>Error Contraseña</h1>La longitud debe ser igual a 7 [Contraseña | Validación]</body></html>"
	    
	if (form.d.forma == None):
	    return "<html><title>Error</title><body><h1>Error Forma de pago</h1>Indicar una forma de pago</body></html>"
                            
        html = """
        <html>
          <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
            <title>Generado</title>
          </head>
          <body>
            <h1>Datos Recibidos del formulario</h1>
		<p>Nombre <code>%s</code></p>
		<p>Apellido <code>%s</code></p>
		<p>Email <code>%s</code></p>
		<p>NVisa <code>%s</code></p>
		<p>Dia <code>%s</code></p>
		<p>Mes <code>%s</code></p>
		<p>Año <code>%s</code></p>
		<p>Direccion <code>%s</code></p>
		<p>Contraseña <code>%s</code></p>
		<p>Verificacion <code>%s</code></p>
		<p>Forma de pago <code>%s</code></p>
          </body>
        </html>""" % (str(form.d.nombre), str(form.d.apellido), str(form.d.email), str(form.d.nvisa), str(form.d.dia), str(form.d.mes), str(form.d.anio), str(form.d.direccion), str(form.d.contrasena), str(form.d.verificacion), str(form.d.forma))
        
        return html
