from django.shortcuts import render, HttpResponse
from .forms import UploadFileForm
from apdcl_p2.settings import BASE_DIR
import os
import datetime
import json
import pandas as pd

# Create your views here.

def handle_uploaded_file(f):
    with open(os.path.join(BASE_DIR, 'uploaded') + '/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def showUploadPage(request):
    return render(request, 'index.html')

def uploadValidate(request):
    if request.method == 'POST':
        if request.FILES:
            filename = str(request.FILES['file'])

            row1 = request.POST["r1"]
            row2 = request.POST["r2"]
            cols = request.POST["columns"]

            if "" not in [row1, row2, cols]:

                try:
                    row1 = int(row1)
                    row2 = int(row2)

                except:
                    return render(request, 'index.html', {'result': 'Row must be integer!'})

                if filename.split('.')[-1] == 'csv':
                    form = UploadFileForm(request.POST, request.FILES)
                    handle_uploaded_file(request.FILES['file'])

                    result = selection(filename, cols, row1, row2)

                    return HttpResponse(result)

                else:
                    return render(request, 'index.html', {'result': 'Invalid file format!'})

            else:
                return render(request, 'index.html', {'result': 'Fill the row and columns field!'})

        else:
            return render(request, 'index.html', {'result': 'Upload a file first!'})

    else:
        form = UploadFileForm()

def selection(filename, cols, srow, erow):
    file = os.path.join(BASE_DIR, 'uploaded') + '/' + filename
    cols = cols.split(',')
    df = pd.read_csv(file, usecols=cols)
    df = df.loc[srow:erow]

    return df.to_html()