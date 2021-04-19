from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventListView.as_view(), name='events-home'),
    path('event/<int:pk>/', views.EventDetailView.as_view(), name='events-detail'),
    path('event/<int:pk>/update/', views.EventUpdateView.as_view(), name='events-update'),
    path('event/<int:pk>/delete/', views.EventDeleteView.as_view(), name='events-delete'),
    path('event/new/', views.EventCreateView.as_view(), name='events-create'),
    path('about/', views.about, name='events-about')
]
