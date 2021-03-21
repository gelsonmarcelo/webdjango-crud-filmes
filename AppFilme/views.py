from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from ProjetoFilmes.models import Filme
from django.urls.base import reverse_lazy

###
# -*- coding: utf-8 -*-
class ListaFilme(ListView):
    template_name = "lista.html"
    model = Filme
    context_object_name = 'filmes'
    
class Index(TemplateView):
    template_name = "index.html"
    
class CriaFilme(CreateView):
    template_name = "cria.html"
    model = Filme()
    fields = '__all__'
    success_url = reverse_lazy("lista_filmes")
    
class AtualizaFilme(UpdateView):
    template_name = "atualiza.html"
    model = Filme()
    fields = '__all__'
    context_object_name = 'filme'
    success_url = reverse_lazy("lista_filmes")

class DeletaFilme(DeleteView):
    template_name = "exclui.html"
    model = Filme()
    context_object_name = 'filme'
    success_url = reverse_lazy("lista_filmes")
    