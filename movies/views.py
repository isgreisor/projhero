from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Movie
# Create your views here.

class MovieListView(ListView):
    model = Movie
    context_object_name = 'movie_list.html'
    template_name = 'movies/movie_list.html'
    fields = ("title","year","Dhero")

class MovieDetailView(DetailView):
    model = Movie
    context_object_name = 'movie'
    template_name = 'movies/movie_detail.html'

class MovieUpdateView(UpdateView):
    model = Movie
    fields = ('title','year','Dhero')
    template_name = 'movies/movie_edit.html'

class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'movies/movie_delete.html'
    success_url = reverse_lazy('movie_list')

class MovieCreateView(CreateView):
    model = Movie
    template_name = 'movies/movie_new.html'
    fields = ('title', 'year', 'Dhero',)
