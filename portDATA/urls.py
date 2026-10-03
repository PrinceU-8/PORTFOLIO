from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    # Static & Base Pages
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('contact/', views.contact_page, name='contact'),
    path('about/', views.about, name='about'),

    # Projects
    path('works/', views.project_list, name='works'),
    path('works/<int:project_id>/', views.project_detail, name='project_detail'),
    path('works/add/', views.add_project, name='add_project'),
    path('works/addother/', views.add_otherproject, name='add_otherproject'),

    # Testimonials
    path('testimonies/', views.TestimonialDATAListView.as_view(), name='testimony'),
    path('testimonies/add/', views.add_testimonial, name='add_testimonial'),
    path('testimonies/<int:detail_id>/', views.testimony_detail, name='testimonialDATA_detail'),

    # Contacts
    path('contact/add/', views.add_contact, name='add_contact'),

    # Superuser Stuffs
    path('login/', views.AdminLoginView.as_view(), name='admin_login'),
    path('logout/', LogoutView.as_view(next_page='admin_login'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/project/create/', views.create_project, name='create_project'),
    path('dashboard/techstack/create/', views.create_techstack, name='create_techstack'),
    path('dashboard/project/<int:project_id>/edit/', views.edit_project, name='edit_project'),
    path('dashboard/techstack/<int:stack_id>/edit/', views.edit_techstack, name='edit_techstack'),
    path('dashboard/otherproject/<int:other_id>/edit/', views.edit_otherproject, name='edit_otherproject'),
    path('dashboard/project/<int:project_id>/delete/', views.delete_project, name='delete_project'),
    path('dashboard/techstack/<int:stack_id>/delete/', views.delete_techstack, name='delete_techstack'),
    path('dashboard/otherproject/<int:other_id>/delete/', views.delete_otherproject, name='delete_otherproject'),
    path('dashboard/contact/<int:contact_id>/delete/', views.delete_contact, name='delete_contact'),
    path('dashboard/testimony/<int:testimonial_id>/delete/', views.delete_testimony, name='delete_testimony'),
]