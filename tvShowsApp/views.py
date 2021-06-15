from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages

from . models import *

def first(request):
    print(TvShows.objects.all())
    context = {
        'allshows': TvShows.objects.all()
    }
    return render(request, "showlist.html", context)

def index(request):
    return render(request, "mark.html")

def newShow(request):
    print("**********************")
    print(request.POST)
    print("**********************")

    errorFromTheValidator = TvShows.objects.i_am_the_validator(request.POST)

    print("Errors from the Validator is HERE!!!", errorFromTheValidator)

    if len(errorFromTheValidator)>0:
        for key, value in errorFromTheValidator.items():
            messages.error(request, value)
        return redirect("/shows/new")
            

    fluffy = TvShows.objects.create(title = request.POST["tt"], network = request.POST["net"], release_date = request.POST["RDate"], description = request.POST["desc"])
    
    return redirect(f"/shows/{fluffy.id}")


def TvShowinfomation(request, theShowID):
    print(request.GET)
    print(TvShows.objects.get(id=theShowID))
    context = {
        "oneShow": TvShows.objects.get(id=theShowID)
    }
    return render(request, "ShowInfo.html",context)

def EditShow(request, theShowID):
    print(request.GET)
    print(TvShows.objects.get(id=theShowID))
    context = {
        'editshow':TvShows.objects.get(id=theShowID)
    }
    return render(request, "EditShowInfo.html", context)

def updatedCheese(request, theShowID):
    errorFromTheValidator = TvShows.objects.i_am_the_validator(request.POST)

    print("Errors from the Validator is HERE!!!", errorFromTheValidator)

    if len(errorFromTheValidator)>0:
        for key, value in errorFromTheValidator.items():
            messages.error(request, value)
        return redirect("/shows/new")

    c = TvShows.objects.get(id=theShowID)
    c.title = request.POST["tt"]
    c.network = request.POST["net"]
    c.release_date = request.POST["RDate"]
    c.description = request.POST["desc"]
    c.save()

    return redirect(f"/shows/{theShowID}/edit")

def completedestrution(request, theShowID):
    c = TvShows.objects.get(id=theShowID)
    c.delete()

    return redirect("/shows")

