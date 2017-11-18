# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def disc_list(request):
    return render(request, 'MIXAPP/disc_list.html', {})
