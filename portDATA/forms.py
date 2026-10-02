from django import forms
from .models import ProjDATA, OtherProjDATA, contactDATA, TestimonialDATA, TechStack
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

class ProjDATAForm(forms.ModelForm):
    class Meta:
        model = ProjDATA
        fields = ['project_name', 'description', 'tech_stacks', 'link']
        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Project stuffs'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Project teaaa...'}),
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

class SuperuserAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        super().confirm_login_allowed(user)
        if not user.is_superuser:
            raise ValidationError(
                "Access restricted: Only administrator accounts can sign in here.",
                code="not_superuser",
            )

class TechStackForm(forms.ModelForm):
    class Meta:
        model = TechStack
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Python, Django, PostgreSQL',
                'required': 'required'
            }),
        }

class CreateProjectForm(forms.ModelForm):
    # Requirement: Radio buttons fetching all tech stack objects
    tech_stack_selection = forms.ModelChoiceField(
        queryset=TechStack.objects.all(),
        widget=forms.RadioSelect,
        required=True,
        empty_label=None,
        label="Select Tech Stack"
    )

    class Meta:
        model = ProjDATA
        fields = ['project_name', 'description', 'link']
        widgets = {
            'project_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter project title',
                'required': 'required'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter detailed project description...',
                'required': 'required'
            }),
            'link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://github.com/... or live URL',
                'required': 'required'
            }),
        }

    def save(self, commit=True):
        instance = super().save(commit=commit)
        if commit:
            selected_stack = self.cleaned_data.get('tech_stack_selection')
            if selected_stack:
                instance.tech_stacks.set([selected_stack])
        return instance

    