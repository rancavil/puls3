from django.forms import ModelForm
from .models import Enlace

class EnlaceForm(ModelForm):
	class Meta:
		model = Enlace
		exclude = ('votos','usuario','timestamp',)