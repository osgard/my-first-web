# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from .models import Musica#Musica es el modelo/tabla que creamos
#en el tutorial se llama Post

# Create your views here.
def disc_list(request):
   # Muscia = Musica.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    Muscia = Musica.objects.order_by('created_date')
    return render(request, 'MIXAPP/disc_list.html', {'Muscia':Muscia})
