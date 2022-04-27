from urllib import request
from django.shortcuts import render, redirect
from .forms import queryForm
from .ranking import didyoumean, perform_query_search
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
    print(query)
    # print(didyoumean(query))
    result = perform_query_search(query)
    print(result)
    return render(
        request=request,
        template_name='resultpage.html'
    )

