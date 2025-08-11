from django.urls import path
from .utils import ImageLocalStorage
from .views import HomePageView, AboutPageView, ProductIndexView, ProductShowView, ProductCreateView, ProductCreatedView, CartView, CartRemoveAllView, ImageViewFactory, ImageViewNoDI

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name='about'),
    path('products/', ProductIndexView.as_view(), name='index'),
    path('products/create', ProductCreateView.as_view(), name='form'),
    path('products/created', ProductCreatedView.as_view(), name='created'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
    path('cart/', CartView.as_view(), name='cart_index'),
    path('cart/add/<str:product_id>', CartView.as_view(), name='cart_add'),
    path('cart/removeAll', CartRemoveAllView.as_view(), name='cart_removeAll'),
    path('image/', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_index'),
    path('image/save', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_save'),
    path('image-not-di/', ImageViewNoDI.as_view(), name='imagenotdi_index'),
    path('image-not-di/save', ImageViewNoDI.as_view(), name='imagenotdi_save'),
]

