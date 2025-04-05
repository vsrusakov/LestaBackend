from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.views.decorators.http import require_POST

from tf_idf.forms import FilesForm
from tf_idf.utils import compute_tf_idf


def index(request: HttpRequest):
    return render(request, 'tf_idf/index.html', {'form': FilesForm()})


@require_POST
def process_form(request: HttpRequest):
    form = FilesForm(request.POST, request.FILES)
    if form.is_valid():
        cd = form.cleaned_data['files']
        file_names = [f.name for f in cd]
        corpus = [f.file for f in cd]
        words, tf_idf_array = compute_tf_idf(corpus)
        return render(request, 'tf_idf/table.html')
    return redirect('tf_idf:index')
