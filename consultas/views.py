from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Consulta, Categoria
from .forms import ConsultaForm, CategoriaForm
from django.urls import reverse_lazy

# ✅ Vista que lista todas las consultas (y permite búsqueda por título)
class ConsultaListView(ListView):
    model = Consulta
    template_name = 'consultas/consulta_list.html'
    context_object_name = 'consultas'

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Consulta.objects.filter(titulo__icontains=query)
        return super().get_queryset()

# ✅ Vista para crear una nueva consulta
class ConsultaCreateView(CreateView):
    model = Consulta
    form_class = ConsultaForm
    template_name = 'consultas/consulta_form.html'
    success_url = reverse_lazy('consultas:consulta-list')  # 🔧 corregido con namespace

# ✅ Vista para crear una nueva categoría
class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'consultas/categoria_form.html'
    success_url = reverse_lazy('consultas:consulta-list')  # 🔧 corregido con namespace
