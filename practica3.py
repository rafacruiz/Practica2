#!/usr/bin/env python
import web
from web import form
from formulario3 import *

urls = (
    '/formulario', 'Formulario',
    '/(.*)', 'hello'
)

plan = web.template.render('./templates/')

app = web.application(urls, globals())
    
class hello:        
    def GET(self, name):
        return "<html><title>Error 404</title><body>Pagina no enconstrada, Error 404</body></html>"


if __name__ == "__main__":
    app.run()