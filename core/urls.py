from django.urls import path
from .views import EventoListView, EventoCreateView, EventoUpdateView, EventoDeleteView

urlpatterns = [
    path('', EventoListView.as_view(), name='evento_list'),
    path('create/', EventoCreateView.as_view(), name='evento_create'),
    path('<int:pk>/update/', EventoUpdateView.as_view(), name='evento_update'),
    path('<int:pk>/delete/', EventoDeleteView.as_view(), name='evento_delete'),
]
