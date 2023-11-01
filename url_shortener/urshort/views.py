from django.shortcuts import render, HttpResponse
from urshort.models import *
from urshort.forms import CreateNewShortUrl
import random
import string
import datetime
# Create your views here.


def home(request):
    return render(request, 'index.html')


def create(request):
    if request.method == "POST":
        form = CreateNewShortUrl(request.POST)
        if form.is_valid:
            original_web = form.data['long_url']
            random_chars_list = list(string.ascii_letters)
            random_chars = ''
            for i in range(6):
                random_chars += random.choice(random_chars_list)
            while len(ShortUrl.objects.filter(short_code=random_chars)) != 0:
                for i in range(6):
                    random_chars += random.choice(random_chars_list)
            d = datetime.datetime.now()
            s = ShortUrl(long_url=original_web,
                         short_code=random_chars, date_time_created=d)
            s.save()
            curr = ShortUrl.objects.filter(short_code=random_chars)
            # print(curr[0].short_code)
            if len(curr) == 0:
                return HttpResponse("NOT FOUND")
            # context = {'obj': curr[0]}

            return render(request, 'url_created.html', context={'chars': random_chars, 'full_url': curr[0].long_url})
    else:
        form = CreateNewShortUrl()
        context = {'form': form}
        return render(request, 'create.html', context)


def redirect(request, url):
    curr = ShortUrl.objects.filter(short_code=url)
    # print(curr[0].short_code)
    if len(curr) == 0:
        return HttpResponse("NOT FOUND")
    context = {'obj': curr[0]}
    return render(request, "redirect.html", context)


def display(request):
    query_set = ShortUrl.objects.all()
    context = {'url': query_set}
    return render(request, 'display.html', context)


def long(request):
    if request.method == "POST":
        URL = request.POST.get('URL')
        context = {'url': URL}
        return redirect(request, URL)
    return render(request, "long.html")
