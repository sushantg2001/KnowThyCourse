from urllib import request
from django.shortcuts import render, redirect

from .forms import queryForm
from .bm25 import bm25output, didyoumean
from .filter import filter
# Create your views here.
def home(request):
    if request.method == 'GET':
        query_form = queryForm()
    if request.method == 'POST':
        query_form = queryForm(request.POST)
        if query_form.is_valid():
            return redirect('results', query = query_form.cleaned_data.get('query'))

    return render(
        request=request,
        template_name='frontpage.html',
        context={
            'form':query_form
        }
    )


def results(request, query):
    corrected_query = didyoumean(query)
    filters = [
        float(4.0),
        [True, True, False, False],
        [True, True, True]
    ]
    results = bm25output(query, 200)
    filtered_results = filter(results, filters)
    if request.method == 'GET':
        return render(
            request=request,
            template_name='resultpage.html',
            context={
                "results":filtered_results,
                'query': query,
            }
        )

    elif request.method == 'POST':
        print(request.POST)
        filters = [
            float(4.0),
            [True, True, True, True],
            [True, True, True]
        ]
        filtered_results = filter(results, filters)
        return render(
            request=request,
            template_name='resultpage.html',
            context={
                "results":filtered_results,
                'query': query,
            }
        )

    print(filters)