from django.urls import path
from about import views

urlpatterns = [
    # about
    path('', views.about_main, name='about_main'),
    path('manual/', views.about_manual, name='about_manual'),
    path('notice/', views.about_notice, name='about_notice'),
]