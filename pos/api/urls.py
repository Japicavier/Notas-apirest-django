from django.urls import path
from . import views

urlpatterns = [
    path('categorias/', views.CategoriaListView.as_view(), name='categoria-list'),
    path('productos/', views.ProductoListView.as_view(), name='producto-list'),
    path('clientes/', views.ClienteView.as_view(), name='cliente-list'),
    path('clientes/<int:cliente_id>/', views.ClienteDetailView.as_view(), name='cliente-detail'),
    path('categorias/<int:categoria_id>/productos/', views.CategoriaProductosView.as_view(), name='categoria-productos'),
    path('pedidos/', views.PedidoCreateView.as_view(), name='pedido-create'),
]