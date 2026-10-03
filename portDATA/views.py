from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.views.decorators.http import require_POST
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy

from .models import OtherProjDATA, ProjDATA, PersonDATA, contactDATA, TestimonialDATA, TechStack
from .forms import (ProjDATAForm, OtherProjDATAForm, contactDATAForm,TestimonialDATAForm, CreateProjectForm, TechStackForm,SuperuserAuthenticationForm
)


def superuser_required(view_func):
    decorator = user_passes_test(
        lambda u: u.is_authenticated and u.is_superuser,
        login_url='admin_login'
    )
    return decorator(view_func)


# --- Public Views ---

def about(request):
    personal_info = PersonDATA.objects.first()
    return render(request, 'about.html', {'profile': personal_info})

def project_list(request):
    projects = ProjDATA.objects.prefetch_related('tech_stacks').all()
    other_projects = OtherProjDATA.objects.all()

    return render(request, 'works.html', {
        'ProjDATA': projects,
        'OtherProjDATA': other_projects,
        'project_form': ProjDATAForm(),
        'other_project_form': OtherProjDATAForm(),  # <-- Added
    })

def project_detail(request, project_id):
    project = get_object_or_404(ProjDATA.objects.prefetch_related('tech_stacks'), id=project_id)
    return render(request, 'project_detail.html', {'project': project})

def add_project(request):
    if request.method == 'POST':
        form = ProjDATAForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER', 'works'))
    return redirect(request.META.get('HTTP_REFERER', 'works'))

def add_otherproject(request):
    if request.method == 'POST':
        form = OtherProjDATAForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER', 'works'))
    return redirect(request.META.get('HTTP_REFERER', 'works'))

def add_testimonial(request):
    if request.method == 'POST':
        form = TestimonialDATAForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER', 'testimony'))
    return redirect(request.META.get('HTTP_REFERER', 'testimony'))

def add_contact(request):
    if request.method == 'POST':
        form = contactDATAForm(request.POST)
        if form.is_valid():
            form.save()
    next_url = request.META.get('HTTP_REFERER')
    if next_url:
        return redirect(next_url)
    return redirect('home')

class TestimonialDATAListView(ListView):
    model = TestimonialDATA
    template_name = 'testimony.html'
    context_object_name = 'testimonies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['testimony_form'] = TestimonialDATAForm() 
        return context

def testimony_detail(request, detail_id):
    testimonial = get_object_or_404(TestimonialDATA, pk=detail_id)
    return render(request, 'testimony_detail.html', {'testimonial': testimonial})

def contact_page(request):
    form = contactDATAForm()
    return render(request, 'contact.html', {'contact_form': form})


# --- Authentication Views ---

class AdminLoginView(LoginView):
    template_name = 'admin_login.html'
    authentication_form = SuperuserAuthenticationForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('dashboard')


# --- Dashboard & Management Views ---


@superuser_required
def dashboard(request):
    projects = ProjDATA.objects.prefetch_related('tech_stacks').all()
    other_projects = OtherProjDATA.objects.all()
    tech_stacks = TechStack.objects.prefetch_related('projects').all()
    contact_messages = contactDATA.objects.all().order_by('-id')
    testimonials = TestimonialDATA.objects.all().order_by('-id')

    return render(request, 'dashboard.html', {
        'projects': projects,
        'other_projects': other_projects,
        'tech_stacks': tech_stacks,
        'contact_messages': contact_messages,
        'testimonials': testimonials,
    })

@superuser_required
def create_project(request):
    if request.method == 'POST':
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CreateProjectForm()
    return render(request, 'create_project.html', {'form': form})

@superuser_required
def create_techstack(request):
    if request.method == 'POST':
        form = TechStackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TechStackForm()
    return render(request, 'create_techstack.html', {'form': form})

@superuser_required
def edit_project(request, project_id):
    project = get_object_or_404(ProjDATA, id=project_id)
    initial_data = {}
    if project.tech_stacks.exists():
        initial_data['tech_stack_selection'] = project.tech_stacks.first()

    if request.method == 'POST':
        form = CreateProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CreateProjectForm(instance=project, initial=initial_data)

    return render(request, 'edit_project.html', {'form': form, 'project': project})

@superuser_required
def edit_otherproject(request, other_id):
    other_proj = get_object_or_404(OtherProjDATA, id=other_id)
    if request.method == 'POST':
        form = OtherProjDATAForm(request.POST, instance=other_proj)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = OtherProjDATAForm(instance=other_proj)

    return render(request, 'edit_otherproject.html', {'form': form, 'other_proj': other_proj})

@superuser_required
def edit_techstack(request, stack_id):
    stack = get_object_or_404(TechStack, id=stack_id)
    if request.method == 'POST':
        form = TechStackForm(request.POST, instance=stack)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TechStackForm(instance=stack)

    return render(request, 'edit_techstack.html', {'form': form, 'stack': stack})

@superuser_required
@require_POST
def delete_project(request, project_id):
    project = get_object_or_404(ProjDATA, id=project_id)
    project.delete()
    return redirect('dashboard')

@superuser_required
@require_POST
def delete_otherproject(request, other_id):
    other = get_object_or_404(OtherProjDATA, id=other_id)
    other.delete()
    return redirect('dashboard')

@superuser_required
@require_POST
def delete_techstack(request, stack_id):
    stack = get_object_or_404(TechStack, id=stack_id)
    stack.delete()
    return redirect('dashboard')

@superuser_required
@require_POST
def delete_contact(request, contact_id):
    msg = get_object_or_404(contactDATA, id=contact_id)
    msg.delete()
    return redirect('dashboard')

@superuser_required
@require_POST
def delete_testimony(request, testimonial_id):
    testimony = get_object_or_404(TestimonialDATA, id=testimonial_id)
    testimony.delete()
    return redirect('dashboard')