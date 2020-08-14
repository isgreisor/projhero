from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Movie
# Create your views here.

class MovieListView(LoginRequiredMixin, ListView):
    model = Movie
    context_object_name = 'movie_list.html'
    template_name = 'movies/movie_list.html'
    fields = ("title","year","Dhero")
    login_url = 'login'

class MovieDetailView(LoginRequiredMixin, DetailView):
    model = Movie
    context_object_name = 'movie'
    template_name = 'movies/movie_detail.html'
    login_url = 'login'

class MovieUpdateView(LoginRequiredMixin, UpdateView):
    model = Movie
    fields = ('year','Dhero')
    template_name = 'movies/movie_edit.html'
    login_url = 'login'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class MovieDeleteView(LoginRequiredMixin, DeleteView):
    model = Movie
    template_name = 'movies/movie_delete.html'
    success_url = reverse_lazy('movie_list')
    login_url = 'login'


class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    template_name = 'movies/movie_new.html'
    fields = ('title', 'year', 'Dhero',)
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class SearchResultsListView(ListView):
    model = Movie
#    context_object_name = 'movie_detail'
    template_name = 'movies/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Movie.objects.filter(
          Q(title__icontains=query) | (Q(Dhero__icontains=query) |
          Q(year__icontains=query))
        )
