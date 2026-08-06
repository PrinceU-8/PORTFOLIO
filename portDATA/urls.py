from django.urls import path
from django.views.generic import TemplateView 
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path('contact/', TemplateView.as_view(template_name='home.html'), name='contact'),
    path('contact/add/', views.add_contact, name='add_contact'),

    path('works/add/', views.add_project, name='add_project'),
    path('works/addother/', views.add_otherproject, name='add_otherproject'),

    path('testimony/', views.TestimonialDATAListView.as_view(), name='testimony'),
    path('testimony/<int:testimonialDATA_id>/', views.testimony_detail, name='testimony_detail'),
    path('Testimony/add/', views.add_testimonial, name='add_testimonial'),
    path('testimonies/<int:detail_id>/', views.testimony_detail, name='testimonialDATA_detail'),

    path('about/', views.about, name='about'),
    path('works/', views.project_list, name='works'),
    path('works/<int:project_id>/', views.project_detail, name='project_detail'),
]