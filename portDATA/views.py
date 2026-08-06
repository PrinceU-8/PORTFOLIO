from django.shortcuts import render, get_object_or_404
from .models import OtherProjDATA, ProjDATA, PersonDATA, contactDATA, TestimonialDATA
from .forms import ProjDATAForm, OtherProjDATAForm, contactDATAForm, TestimonialDATAForm
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404

def about(request):
    personal_info = PersonDATA.objects.first()
    return render(request, 'about.html', {'profile': personal_info})

def project_list(request):
    projects = ProjDATA.objects.all()
    other_projects = OtherProjDATA.objects.all()
    project_form = ProjDATAForm()
    
    return render(request, 'works.html', {
        'ProjDATA': projects,
        'OtherProjDATA': other_projects,
        'project_form': project_form,
    })
def project_detail(request, project_id):
    project = get_object_or_404(ProjDATA, pk=project_id)
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
            print("--- CONTACT SAVED SUCCESSFULLY! ---")
        else:
            print("--- INVALID FORM ERRORS ---:", form.errors)
            
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
