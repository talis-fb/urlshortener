import random, string
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect
from urls.models import Url

def add_url(request:HttpRequest):
    if request.method == "GET":
        url = request.GET.get('url')
        if url:
            hash = ''.join(random.choices(string.ascii_letters, k=7))
            registration = Url(hash=hash, original_url=url)
            registration.created_at = 321312
            registration.owner = "Eu"
            registration.save()
            return HttpResponse(hash)


    return HttpResponse("Fez errado alguma coisa ai meu rei")

def get_url(request:HttpRequest, hash: str):
    target:Url = Url.objects.get(hash=hash)
    url = target.original_url
    if url:
        return redirect(f'https://{url}')

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
