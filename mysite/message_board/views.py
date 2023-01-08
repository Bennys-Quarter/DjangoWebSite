import time

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.http import HttpResponseForbidden
from django.http import HttpResponseServerError
from django.http import JsonResponse
from django.http import StreamingHttpResponse
from django.http import FileResponse
from django.http import HttpResponseGone
from django.http import HttpResponseNotModified
from django.template import loader
from .models import Entry
from datetime import datetime

from .forms import NameForm

def index(request):
    form = NameForm()
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            print(request.POST)
            print(form['name_a'].value())
            print(form['name_b'].value())
            print(form['msg'].value())
            new_entry = Entry(name_A=str(form['name_a'].value()),
                              name_B=str(form['name_b'].value()),
                              pub_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                              message=str(form['msg'].value()))
            new_entry.save()
    messages = Entry.objects.all()
    context = {'m_table': messages, }
    return render(request, 'message_board/index.html', context)

def rick_roll(request):
    print(request)
    return render(request, 'message_board/rick_roll.html')

def selection(request):
    if request.method == "POST":
        select = request.POST.get('dropdown', False)
        if select[0] == "1":
            return render(request, 'message_board/rick_roll.html')
        elif select[0] == "2":
            return HttpResponseRedirect("https://amatus.itch.io/earth-defender?secret=auitHm92fSRkdrGA1q9bYvwYbf8")
        elif select[0] == "3":
            return HttpResponseNotFound('Status 404, page not found.')
        elif select[0] == "4":
            return HttpResponseForbidden('Status 403, forbidden action.')
        elif select[0] == "5":
            return HttpResponseServerError('Status 500, Internal server error.')
        elif select[0] == "6":
            return JsonResponse({'1.measurement':
  {
    "date": "2018-05-06",
    "temperatureC": 1,
    "summary": "Freezing",
    "temperatureF": 33
  },
  '2.measurement':{
    "date": "2018-05-07",
    "temperatureC": 14,
    "summary": "Bracing",
    "temperatureF": 57
  }}
)
        elif select[0] == "7":
            return StreamingHttpResponse(my_processor(0.1), content_type='text')
        elif select[0] == "8":
            return FileResponse(open('message_board/images/FollowWall.png', 'rb'))
        elif select[0] == "9":
            return HttpResponseGone('Status 410, That are not the droids you are looking for!')
        elif select[0] == "10":
            return HttpResponseNotModified()
    return render(request, 'message_board/index.html')

def my_processor(sleep_interval):
    lines = [
        'This is a stream package',
        'This is a the data ',
        'This is the end of the stream package'
    ]
    start_time = time.time()
    while True:
        for line in lines:
            elapsed_time = int(time.time() - start_time)
            yield f"[{elapsed_time:>10} s] {line}\n"
            time.sleep(sleep_interval)
        yield "=========== Here we go again ===========\n"