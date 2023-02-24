from django.urls import path
from django.views.generic import TemplateView
from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register('customers', views.CustomerViewSet)
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet)
router.register('orders', views.OrderViewSet, basename='orders')
# router.register('jkl', TemplateView.as_view(template_name='store/jkl.html'), basename='jkl.html')



products_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet,
                         basename='product-reviews')
products_router.register('images', views.ProductImageViewSet, basename='product-images')

carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', views.CartItemViewSet, basename='cart-items')

# URLConf
urlpatterns = router.urls + products_router.urls + carts_router.urls
# + [
#     path('jkl', TemplateView.as_view(template_name='store/jkl.html'))
# ]
