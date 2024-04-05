from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseServerError
from django.db import OperationalError
from .models import JobPost, JobApplication
from .forms import ApplicationForm

# Create your views here.

def home(request):
    return render(request, 'joblistings/home.html')

def index(request):
    jobs = JobPost.objects.all()
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        context = { 'jobs': jobs, 'form':form }
        if form.is_valid():
            job_post_id = request.POST.get('job_post_id')
            job_post = JobPost.objects.get(pk=job_post_id)
            job_app = form.save(commit=False)
            job_app.job_post = job_post
            job_app.save()
            return redirect('success')
    else:
        form = ApplicationForm()
    context = { 'jobs': jobs, 'form':form }
    return render(request, 'joblistings/index.html', context)

def success(request):
    return render(request, 'joblistings/formsuccess.html')