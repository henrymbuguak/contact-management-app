# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B('Hen',SPAN(2),'Tech'),XML('&trade;&nbsp;'),
                  _class="navbar-brand",_href="http://www.web2py.com/",
                  _id="web2py-logo")
response.title = request.application.replace('_',' ').title()
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = myconf.get('app.Kiarie Henry Mbugua')
response.meta.description = myconf.get('app.Simple contact App That companies can use')
response.meta.keywords = myconf.get('app.contact')
response.meta.generator = myconf.get('app.generator')

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('default', 'index'), []),
    (T('Companies'), False, URL('default', 'companies'), []),
    (T('Contact Create'), False, URL('default', 'contact_create'), [])
]
