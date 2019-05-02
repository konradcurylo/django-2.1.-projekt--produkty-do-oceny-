from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Towary


# Create your views here.
def home(request):
    towary = Towary.objects.all()
    return render(request,'produkty/home.html', {'towary':towary} )

@login_required
def stworz(request):
    if request.method == "POST":
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            towar = Towary()
            towar.title = request.POST['title']
            towar.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                towar.url = request.POST['url']
            else:
                towar.url = 'http://' + request.POST['url']
            towar.icon = request.FILES['icon']
            towar.image = request.FILES['image']
            towar.hunt_user = request.user
            towar.save()
            return redirect('/produkty/' + str(towar.id))
        else:
            return render(request,'produkty/stworz.html',{'error':'Wszystkie pola są wymagane'})
    else:
        return render(request,'produkty/stworz.html')


def detail(request, towar_id):
    towar = get_object_or_404(Towary,pk= towar_id)
    return render(request,'produkty/detail.html', {'towar':towar})

@login_required(login_url="/konta/rejestracja")
def upvote(request, towar_id):
    if request.method == "POST":
        towar = get_object_or_404(Towary, pk=towar_id)
        towar.votes_total +=1
        towar.save()
        return redirect('/produkty/' + str(towar.id))
