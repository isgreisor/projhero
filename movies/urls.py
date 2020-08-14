from django.urls import path
from .views import MovieListView, MovieDetailView, \
                   MovieUpdateView, MovieDetailView, \
                   MovieDeleteView, MovieCreateView, \
                   SearchResultsListView

urlpatterns = [
  path('<uuid:pk>/edit/', MovieUpdateView.as_view(), name='movie_edit'),
  path('<uuid:pk>/', MovieDetailView.as_view(), name='movie_detail'),
  path('<uuid:pk>/delete/', MovieDeleteView.as_view(), name='movie_delete'),
  path('new/', MovieCreateView.as_view(), name='movie_new'),
  path('search/', SearchResultsListView.as_view(), name='search_results'),
  path('', MovieListView.as_view(), name='movie_list'),
]
