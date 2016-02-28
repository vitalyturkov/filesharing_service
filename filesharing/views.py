from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf
from .forms import FileForm
from .models import FileEntity
from FileSharingService.settings import BASE_DIR
from FileSharingService.settings import WEBSITE
from django.http import HttpResponse

import datetime


def main(request):

    if request.method == 'POST':

        c = {}
        c.update(csrf(request))

        download_url = "http://" + handle_file(request.FILES['file'])
        print(download_url)

        return render_to_response("link_ready.html", {'download_url': download_url})

    if request.method == 'GET':
        # if it's GET (not POST) - we just serve the form

        c = {}
        c.update(csrf(request))
        c['form'] = FileForm

        return render_to_response("upload.html", c)


def download(request, file_id):
    file_object = FileEntity.objects.filter(id=file_id)[0]
    f_name = file_object.filename

    with open(BASE_DIR + "\\media\\" + file_id, 'rb') as f:
        data = f.read()

    response = HttpResponse(data, content_type='none')
    response['Content-Disposition'] = 'attachment; filename=' + f_name
    # such a stub ...
    response['Content-Length'] = data.__sizeof__()
    return response


def handle_file(file):
    file_object = FileEntity()
    file_object.filename = file._get_name()

    file_object.save()
    print(file_object.filename, " file has an ID of ", file_object.id)

    with open(BASE_DIR + "\\media\\" + str(file_object.id), 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return WEBSITE + "/d/" + str(file_object.id)
