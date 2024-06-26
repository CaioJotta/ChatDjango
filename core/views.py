from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Evento

class EventoListView(ListView):
    model = Evento
    template_name = 'evento_list.html'
    context_object_name = 'eventos'

class EventoCreateView(CreateView):
    model = Evento
    template_name = 'evento_create.html'
    fields = ['nome', 'descricao', 'data']
    success_url = reverse_lazy('evento_list')

class EventoUpdateView(UpdateView):
    model = Evento
    template_name = 'evento_update.html'
    fields = ['nome', 'descricao', 'data']
    success_url = reverse_lazy('evento_list')

class EventoDeleteView(DeleteView):
    model = Evento
    template_name = 'evento_delete.html'
    success_url = reverse_lazy('evento_list')
