from django.conf.urls import url
from .import views


urlpatterns = [
    url(r'^$', views.hello_world, name='hello'),
    url(r'^suscripcion/$', views.nuevo_usuario, name='nuevo_usuario'),
    url(r'^thanks/$', views.gracias, name='gracias'),
   
 	
]
