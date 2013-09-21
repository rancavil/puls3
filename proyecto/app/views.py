# Create your views here.

from django.shortcuts import render_to_response, render, get_object_or_404, redirect
from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout

from .models import Enlace, Categoria
from .forms import EnlaceForm

def home(request):
	categorias = Categoria.objects.all()
	enlaces = Enlace.objects.all()
	return render(request,'index.html',{'categorias':categorias,'enlaces':enlaces,'request':request})

def categoria(request, id_enlace):
	categorias = Categoria.objects.all()
	cat = get_object_or_404(Categoria, pk=id_enlace)
	enlaces = Enlace.objects.filter(categoria = cat)
	return render(request,'index.html',{'categorias':categorias,'enlaces':enlaces,'request':request})

@login_required
def plus(request, id_enlace):
	enlace = get_object_or_404(Enlace, pk=id_enlace)
	enlace.votos += 1
	enlace.save()
	return redirect('/')

@login_required
def minus(request, id_enlace):
	enlace = get_object_or_404(Enlace, pk=id_enlace)
	enlace.votos -= 1
	enlace.save()
	return redirect('/')

@login_required
def add(request):
	categorias = Categoria.objects.all()
	if request.POST:
		form = EnlaceForm(request.POST)
		if form.is_valid():
			enlace = form.save(commit=False)
			if isinstance(request.user,User):
				enlace.usuario = request.user
			enlace.save()
			return redirect('/')
	else:
		form = EnlaceForm()

	return render_to_response('form.html',context_instance=RequestContext(request,{'categorias':categorias,'form':form,'request':request}))

def logout(request):
	auth_logout(request)
	return redirect('/')