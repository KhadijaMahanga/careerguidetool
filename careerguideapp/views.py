from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
import os, json
from .forms import InputForm
from models import Acseeyear2017Subjectperformance, Acseeyear2016Subjectperformance, Cseeyear2016Subjectperformance
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
            edu_level = form.cleaned_data['education_level']

            schools = get_schools(career, region, gender, edu_level)
            if edu_level == '1':
                school_level = "A levels"
            else:
                school_level = "O levels"
            # redirect to a new URL:
            return render(request, 'index.html', {'form': form, 'schools': schools, 'school_level': school_level})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = InputForm(label_suffix="  ")
        return render(request, 'index.html', {'form': form})

def school(request, schoolcode):
    alevel_subjects = Acseeyear2017Subjectperformance.objects.filter(schoolcode = schoolcode)
    olevel_subjects = Cseeyear2016Subjectperformance.objects.filter(schoolcode = schoolcode)
    pageTitle = "School Detail"
    school_name = alevel_subjects[0].schoolname
    school_region = alevel_subjects[0].region
    school_gpa = alevel_subjects[0].gpa
    return render (request, 'school.html', {'olevel_subjects': olevel_subjects, 'alevel_subjects': alevel_subjects, 'pageTitle': pageTitle,
'school_name': school_name, 'school_region': school_region, 'school_gpa': school_gpa})


def get_schools(career, region, gender, edu_level):
    schools = []
    subjects = data[career]
    if not region:
        if edu_level == '1':
            for subject in subjects:
                queryset = Acseeyear2017Subjectperformance.objects.filter(subjectname = subject).filter(subjectnatranking__in=["1","2","3","4","5","6"])
                schools += list(queryset)
        else:
            for subject in subjects:
                queryset =  Cseeyear2016Subjectperformance.objects.filter(subjectname = subject).filter(subjectnatranking__in=["1","2","3","4","5","6"])
                schools += list(queryset)
    else:
        if edu_level == '1':
            for subject in subjects:
                queryset = Acseeyear2017Subjectperformance.objects.filter(subjectname = subject).filter(region = region).filter(subjectregranking__in=["1","2","3"])
                schools += list(queryset)
        else:
            for subject in subjects:
                queryset = Cseeyear2016Subjectperformance.objects.filter(subjectname = subject).filter(region = region).filter(subjectregranking__in=["1","2","3"])
                schools += list(queryset)
    return schools

def alevel_subjects(request):
    subjects = Acseeyear2017Subjectperformance.objects.order_by().values('subjectname').distinct()
    pageTitle = "A-levels Subjects"
    return render(request, 'subjects.html', {'subjects': subjects, 'pageTitle': pageTitle})


def olevel_subjects(request):
    subjects = Cseeyear2016Subjectperformance.objects.order_by().values('subjectname').distinct()
    pageTitle = "O-levels Subjects"
    return render(request, 'subjects.html', {'subjects': subjects, 'pageTitle': pageTitle})
