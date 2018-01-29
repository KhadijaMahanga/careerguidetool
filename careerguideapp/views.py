from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
import os, json
from .forms import InputForm
from models import Acseeyear2017Subjectperformance, Acseeyear2016Subjectperformance
# Create your views here.

data = json.load(open(os.path.join(settings.BASE_DIR, 'careerguideapp','career.json')))

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = InputForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            career = form.cleaned_data['career']
            region = form.cleaned_data['region']
            gender = form.cleaned_data['gender']

            schools = get_schools(career, region, gender)
            # redirect to a new URL:
            return render(request, 'index.html', {'form': form, 'schools': schools})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = InputForm(label_suffix="  ")
        return render(request, 'index.html', {'form': form})

def school(request, schoolcode):
    return render (request, 'school.html')


def get_schools(career, region, gender):
    schools = []
    subjects = data[career]
    for subject in subjects:
        if not region:
            queryset = Acseeyear2017Subjectperformance.objects.filter(subjectname = subject).filter(subjectnatranking__in=["1","2","3","4","5","6"])
            schools += list(queryset)
        else:
            queryset = Acseeyear2017Subjectperformance.objects.filter(subjectname = subject).filter(region = region).filter(subjectregranking__in=["1","2","3"])
            schools += list(queryset)
    return schools
