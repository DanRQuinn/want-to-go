from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Review
from django.urls import reverse_lazy

class ReviewListView(ListView):
  template_name = 'reviews-list.html'
  model = Review
  context_object_name = 'reviews'
  
class ReviewDetailView(DetailView):
  template_name = 'reviews-detail.html'
  model = Review
  
class ReviewCreateView(CreateView):
  template_name = 'reviews-create.html'
  model = Review
  fields = ['title', 'body', 'author']
  
class ReviewUpdateView(UpdateView):
  template_name = 'reviews-update.html'
  model = Review
  fields = ['id', 'title', 'body', 'author']
  
class ReviewDeleteView(DeleteView):
  template_name = 'reviews-delete.html'
  model = Review
  success_url = reverse_lazy('review_list')
