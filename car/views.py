from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator
from .forms import *
from .filters import CarFilter

# Create your views here.
def job_list(request):
    job_list = Job.objects.all()
    # filters
    myfilter = CarFilter(request.GET, queryset=job_list)
    job_list = myfilter.qs

    paginator = Paginator(job_list, 5) # Show 4 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'jobs': page_obj,
        'job_list': job_list,
        'myfilter': myfilter

    }
    return render(request, 'job/job_list.html', context)

def job_details(request, slug):
    job_detail = Job.objects.get(slug=slug)

    if request.method == 'POST':
        form = Apply_job(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
            return redirect('jobs:job_list')

    else:
        form = Apply_job()



    context = {
        'job': job_detail,
        'form': form

    }
    return render(request, 'job/job_detail.html', context)





@login_required
def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST,  request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect('jobs:job_list')

    else:
        form=JobForm()

    cotext= {
        'form': form
    }


    return render(request, 'job/add_job.html', cotext)


def index(request):
    cars = Job.objects.all()
    context = {
        'cars': cars
    }

    return render(request, 'job/index.html', context)

@login_required
def bid(request, slug):
    bid = Job.objects.get(slug=slug)
    bidders = Bid_price.objects.all()

    if request.method == 'POST':
        form = Bid_price_Form(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner_bid = request.user
            myform.save()
    else:
        form = Bid_price_Form()


    context = {
        'bid': bid,
        'form': form,
        'bidders': bidders,
    }

    return render(request, 'bid/bid.html', context)

