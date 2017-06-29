# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'port/home.html', {})

def skill(request):
    return render(request, 'port/skill.html', {})

def pe(request):
    return render(request, 'port/p&e.html', {})
