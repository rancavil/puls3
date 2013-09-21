from django.core.urlresolvers import reverse

from random import choice

def ejemplo(request):
	alternativas = ['Rodrigo','Alvaro','Diana','Carolina']
	return {'frase': choice(alternativas) }

def menu(request):
	menu = {'menu': [
		{'name': 'Home', 'url' : reverse('home')},
		{'name': 'Add', 'url': reverse('add')},
	]}
	for item in menu['menu']:
		if request.path == item['url']:
			item['active'] = True
	return menu