from datetime import datetime
import random, string
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, render, get_object_or_404
from urls.models import Url
from urls.templates.addUrl import UrlForm
import requests as fetch

def index(request:HttpRequest):
    form = UrlForm()
    return render(request, 'addUrl.html', {'form': form})

def add_url(request:HttpRequest):
    if request.method == "POST":
        # url = request.GET.get('url')
        form = UrlForm(request.POST)
        if form.is_valid():
            try:
                url = request.POST['url']
                if not fetch.get(url).status_code:
                    return HttpResponse("URL INVALIDA")
            except:
                return HttpResponse("URL INVALIDA")

            hash = ''.join(random.choices(string.ascii_letters, k=7))

            modelUrl= Url(hash=hash, original_url=url)
            modelUrl.created_at = int(datetime.now().timestamp())
            modelUrl.owner = "Anonymous"
            modelUrl.save()

            final_url = f'http://{request.get_host()}/{hash}'

            return render(request, 'okUrl.html', { 'url': final_url })


    return HttpResponse("Fez errado alguma coisa ai meu rei")

def get_url(request:HttpRequest, hash: str):
    target:Url = Url.objects.get(hash=hash)
    url = target.original_url
    if url:
        print(f'REDIRECT -> {url}')
        return redirect(url)

    return HttpResponse("Vixe, sem url aqui")

# def index(request:HttpRequest):
#     print("index")
#     print(request.GET.get('url'))
#
#     request.get_signed_cookie
#     return HttpResponse("Hello om!")
#
# def printMessage(request:HttpRequest, q:int):
#     print("print")
#     print(request)
#
#     bod = ''
#
#     for i in range(q):
#         bod += "Meu nome\n"
#
#     return HttpResponse(bod)
