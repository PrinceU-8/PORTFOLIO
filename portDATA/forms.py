from django import forms
from .models import ProjDATA, OtherProjDATA, contactDATA, TestimonialDATA

class ProjDATAForm(forms.ModelForm):
    class Meta:
        model = ProjDATA
        fields = ['project_name', 'description', 'tech_stack', 'link']
        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Project stuffs'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Project teaaa...'}),
            'tech_stack': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Python, Django, Bootstrap'}),
            'link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Add link here'}),
        }

class OtherProjDATAForm(forms.ModelForm):
    class Meta:
        model = OtherProjDATA
        fields = ['project_name', 'description', 'tech_stack', 'link']
        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Project stuffs'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Project teaaa...'}),
            'tech_stack': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Python, Django, Bootstrap'}),
            'link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Add link here'}),
        }

class contactDATAForm(forms.ModelForm):
    class Meta:
        model = contactDATA
        fields = ['first_name', 'last_name', 'contact_number', 'email', 'address', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Address'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Your message...'}),
        }

class TestimonialDATAForm(forms.ModelForm):
    class Meta:
        model = TestimonialDATA
        fields = ['full_name', 'email', 'content']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Your testimonial...'}),
        }