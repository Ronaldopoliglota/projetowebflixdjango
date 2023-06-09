from django.shortcuts import render, redirect, reverse
from .models import Filme, Usuario
from .forms import CriarContaForm, FormHomePage
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class Homepage(FormView):
    template_name = "homepage.html"
    form_class = FormHomePage

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('filme:homefilmes')
        else:
            return super().get(request, *args, **kwargs)

    def get_success_url(self):
        email = self.request.POST.get("email")
        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            return reverse('filme:login')
        else:
            return reverse('filme:criarconta')


class Homefilmes(LoginRequiredMixin, ListView):
    template_name = "homefilmes.html"
    model = Filme


class Detalhefilme(LoginRequiredMixin, DetailView):
    template_name = "detalhesfilme.html"
    model = Filme

    def get(self, request, *args, **kwargs):
        # preciso descobrir qual o filme o usuário está acessando
        filme = self.get_object()
        # pegar a visualização e somar + 1
        filme.visualizacoes += 1
        # Salvar o número de visualizações
        filme.save()
        usuario = request.user
        usuario.filmes_vistos.add(filme)
        return super(Detalhefilme, self).get(request, *args, **kwargs)  # retorna o usuário para a página final

    def get_context_data(self, **kwargs):
        context = super(Detalhefilme, self).get_context_data(**kwargs)
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]
        context['filmes_relacionados'] = filmes_relacionados
        return context


class PesquisarFime(LoginRequiredMixin, ListView):
    template_name = "pesquisar.html"
    model = Filme

    def get_queryset(self):
        termode_pesquisa = self.request.GET.get('query')
        if termode_pesquisa:
            object_list = self.model.objects.filter(titulo__icontains=termode_pesquisa)
            return object_list
        else:
            return None


class PaginaPerfil(LoginRequiredMixin, UpdateView):
    template_name = 'editarperfil.html'
    model = Usuario
    fields = ['first_name', 'last_name', 'username', 'email']

    def get_success_url(self):
        return reverse('filme:homefilmes')


class CriarConta(FormView):
    template_name = 'criarconta.html'
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super(CriarConta, self).form_valid(form)

    def get_success_url(self):
        return reverse('filme:login')


# def filme_destaque(request):
#     filme = Filme.objects
#     return {'filme_destaque': filme}


# def homepage(request):
#     return render(request, 'homepage.html')


# def homefilmes(request):
#     context = {}
#     lista_filmes = Filme.objects.all()
#     context['lista_filmes'] = lista_filmes
#
#     return render(request, 'homefilmes.html', context)
