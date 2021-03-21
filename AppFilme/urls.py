from django.urls import path
from AppFilme.views import Index, CriaFilme, ListaFilme, AtualizaFilme,\
    DeletaFilme 
from ProjetoFilmes.models import Filme

###
urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('filme/cadastrar/', CriaFilme.as_view(model=Filme), name="cadastra_filme"),
    path('filmes/', ListaFilme.as_view(), name="lista_filmes"),
    path('filme/<pk>', AtualizaFilme.as_view(model=Filme), name="atualiza_filme"),
    path('filme/excluir/<pk>', DeletaFilme.as_view(model=Filme), name="deleta_filme"),
]