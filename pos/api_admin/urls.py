from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

router = DefaultRouter()
router.register(r'categoria',views.CategoriaViewSet,basename='categorias_admin')
router.register(r'producto',views.ProductoViewSet,basename='productos_admin')

urlpatterns = router.urls