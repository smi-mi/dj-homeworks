from datetime import datetime
import os
from django.conf import settings
from django.http import Http404
from django.shortcuts import render


def file_list(request, date=None):
    template_name = 'index.html'
    files_path = settings.FILES_PATH
    files = []
    for file in os.listdir(files_path):
        stats = os.stat(os.path.join(files_path, file))
        ctime = datetime.fromtimestamp(stats.st_ctime)
        mtime = datetime.fromtimestamp(stats.st_mtime)
        if date is None or ctime <= date:
            files.append({'name': file,
                          'ctime': ctime,
                          'mtime': mtime})
    context = {
        'files': files,
        'date': date
    }

    return render(request, template_name, context)


def file_content(request, name):
    files_path = settings.FILES_PATH
    if name not in os.listdir(files_path):
        raise Http404()
    with open(os.path.join(files_path, name)) as f:
        content = f.read()
    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': content}
    )

