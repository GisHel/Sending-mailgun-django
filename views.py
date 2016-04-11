
import smtplib
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import SuscriptoreForm
from .models import Suscriptore
from django.template import loader
from django.core.mail import send_mail, BadHeaderError
from email.mime.text import MIMEText

# Create your views here.

def hello_world(request):
	#return HttpResponse('hello world')
	return render(request,'index.html')
	
def nuevo_usuario(request):

	if request.method == 'POST':
		formulario = SuscriptoreForm(request.POST)
		if formulario.is_valid():
			Suscriptore= formulario.save()
			Suscriptore.save()

			msg = MIMEText('TestingMailgun awesomness')
			msg['subject']="Hello"
			msg['from']= "your service email"
			msg['to']= Suscriptore.correo
			
			s= smtplib.SMTP('smtp.mailgun.org',587)
			s.login('postmaster@your domain','your pass')
			s.sendmail(msg['from'],msg['to'],msg.as_string())
			s.quit()
		
			return HttpResponseRedirect('/thanks/')
	else:
		formulario = SuscriptoreForm()

	template = loader.get_template('nuevo_usuario.html')
	context = {
		'form': formulario
	}
	return HttpResponse(template.render(context,request))


def gracias(request):
	template = loader.get_template('gracias.html')
	title = 'gracias'
	context = {
		'title':title
	}
	return HttpResponse(template.render(context,request))