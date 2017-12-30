##====================================================
#import sys

#def application(environ, start_response):
#    status = '200 OK'
#
#    output = u''
#    output += u'sys.version = %s\n' % repr(sys.version)
#    output += u'sys.prefix = %s\n' % repr(sys.prefix)

#    response_headers = [('Content-type', 'text/plain'),
#                        ('Content-Length', str(len(output)))]
#    start_response(status, response_headers)
#
#    return [output.encode('UTF-8')]
##====================================================
import os
import sys

sys.path.append('/var/www/tempsites1/devforless')
sys.path.append('/var/www/tempsites1/devforless/devforless')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "devforless.settings")

application = get_wsgi_application()
##====================================================
#import sys
#
#def application(environ, start_response):
#    status = '200 OK'
#    output = u'sys.path = %s' % repr(sys.path)
#
#    response_headers = [('Content-type', 'text/plain'),
#                        ('Content-Length', str(len(output)))]
#    start_response(status, response_headers)
#
#    return [output.encode('UTF-8')]
##====================================================
#
#def application(environ, start_response):
#    status = '200 OK'
#    output = b'Hello World!'
#
#    response_headers = [('Content-type', 'text/plain'),
#                        ('Content-Length', str(len(output)))]
#    start_response(status, response_headers)
#
#    return [output]

#
#
#!/usr/bin/python3
#"""
#WSGI config for devforless project.
#
#It exposes the WSGI callable as a module-level variable named ``application``.
#
#For more information on this file, see
#https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
#"""

