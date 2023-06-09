from .models import Filme


def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:10]
    return {'lista_filmes_recentes': lista_filmes}


def lista_filmes_emalta(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[0:10]
    return {'lista_filmes_emalta': lista_filmes}


def filme_destaque(request):
    lista_destaque = Filme.objects.order_by('-data_criacao')
    if lista_destaque:
        destaque = lista_destaque[0]
    else:
        destaque = None
    return {'filme_destaque': destaque}
