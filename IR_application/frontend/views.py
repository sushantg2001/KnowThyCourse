from urllib import request
from django.shortcuts import render, redirect

from .forms import queryForm
from .bm25 import bm25output, didyoumean
from .filter import filter
corrected_query = ""
# Create your views here.
def home(request):
    global corrected_query
    filtered_results = []
    if request.method == 'GET':
        return render(
            request=request,
            template_name='search_results.html',
            context= {
                'corrected_query':corrected_query,
            }
        )
    if request.method == 'POST':
        query  = request.POST.get('search')
        corrected_query = didyoumean(query)
        filters = [
            0.0,
            [],
            []
        ]
        if request.POST.get('level-beginner'):
            filters[2].append(True)
        else:
            filters[2].append(False)
        if request.POST.get('level-intermediate'):
            filters[2].append(True)
        else:
            filters[2].append(False)
        if request.POST.get('level-advanced'):
            filters[2].append(True)
        else:
            filters[2].append(False)
        if request.POST.get('4.5'):
            filters[0] = float(4.5)
        else:
            filters[0] = float(0)
        if request.POST.get('4'):
            filters[0] = float(0)
        else:
            filters[0] = float(0)
        if request.POST.get('3'):
            filters[0] = float(3.5)
        else:
            filters[0] = float(0)
        if request.POST.get('3'):
            filters[0] = float(3)
        else:
            filters[0] = float(0)
        if request.POST.get('website-coursera'):
            filters[1].append(True)
        else:
            filters[1].append(False)
        if request.POST.get('website-edx'):
            filters[1].append(True)
        else:
            filters[1].append(False)
        if request.POST.get('website-udemy'):
            filters[1].append(True)
        else:
            filters[1].append(False)
        if request.POST.get('website-udacity'):
            filters[1].append(True)
        else:
            filters[1].append(False)

        if query == "":
            return render(
                request=request,
                template_name='search_results.html',
            )
        print(query)
        print(request.POST)
        print(filters)
        # filters = [
        #     float(4.0),
        #     [True, True, True, True],
        #     [True, True, True]
        # ]
        results = bm25output(query, 100)
        filtered_results = filter(results, filters)
        # return redirect('results', query = query_form.cleaned_data.get('query'))

        return render(
            request=request,
            template_name='search_results.html',
            context={
                "results":filtered_results,
                'query': query,
                'corrected_query': corrected_query,
                'time' : 0.01
            }
        )