# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Note
from .forms import NoteForm

from django.http import HttpResponseRedirect
from django.shortcuts import render

def home(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NoteForm(request.POST)
        # check whether it's valid:
        print "request_method"
        if form.is_valid():
            note = Note(note=form.cleaned_data['captured_note'])
            note.save()
            notes = Note.objects.all()
            return render(request, 'home.html', {'form': form, 'notes': notes})
    # if a GET (or any other method) we'll create a blank form
    else:
        print "get_method"
        form = NoteForm()
    notes = Note.objects.all()
    return render(request, 'home.html', {'form': form, 'notes': notes})

# Create your views here.
