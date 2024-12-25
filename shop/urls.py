from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('menu/', views.menu_view, name='menu'),  # General menu page (no category)
    path('menu/<int:item_id>/', views.menu_detail, name='menu_detail'),  # Item detail page (specific item)
    path('menu/<slug:category_slug>/', views.menu_view, name='menu_by_category'),  # Category filter
]