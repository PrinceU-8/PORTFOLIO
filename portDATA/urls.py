from django.urls import path
from django.views.generic import TemplateView  # 👑 Import this built-in view shortcut
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('contact/', TemplateView.as_view(template_name='home.html'), name='contact'),
    path('mworks/', TemplateView.as_view(template_name='mworks.html'), name='mworks'),
    
    path('about/', views.about, name='about'),
    path('works/', views.project_list, name='works'),
    path('works/<int:project_id>/', views.project_detail, name='project_detail'),
]