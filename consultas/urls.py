from django.urls import path
from .views import ConsultaListView, ConsultaCreateView, CategoriaCreateView

app_name = 'consultas'

urlpatterns = [
    path('', ConsultaListView.as_view(), name='consulta-list'),
    path('nueva/', ConsultaCreateView.as_view(), name='consulta-create'),
    path('categoria/nueva/', CategoriaCreateView.as_view(), name='categoria-create'),
]