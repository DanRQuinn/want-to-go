from django.urls import path
from .views import PlacesListView, PlacesDetailView, PlacesCreateView, PlacesUpdateView, PlacesDeleteView

urlpatterns = [
  path('', PlacesListView.as_view(), name='places_list'),
  path('<int:pk>/', PlacesDetailView.as_view(), name='places_detail'),
  path('new/', PlacesCreateView.as_view(), name='places_create'),
  path('<int:pk>/edit/', PlacesUpdateView.as_view(), name='places_update'),
  path('<int:pk>/delete/', PlacesDeleteView.as_view(), name='places_delete'),
]
