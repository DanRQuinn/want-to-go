from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Places
from django.urls import reverse_lazy

class PlacesListView(ListView):
  template_name = 'places-list.html'
  model = Places
  context_object_name = 'places'

class PlacesDetailView(DetailView):
  template_name = 'places-detail.html'
  model = Places

class PlacesCreateView(CreateView):
  template_name = 'places-create.html'
  model = Places
  fields = ['title', 'body', 'author']

class PlacesUpdateView(UpdateView):
  template_name = 'places-update.html'
  model = Places
  fields = ['id', 'title', 'body', 'author']

class PlacesDeleteView(DeleteView):
  template_name = 'places-delete.html'
  model = Places
  success_url = reverse_lazy('places_list')
