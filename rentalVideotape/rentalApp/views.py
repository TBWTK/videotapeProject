from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Genre, Director, Status, Videotape, Rental
from .forms import GenreForm, DirectorForm, StatusForm, VideotapeForm, RentalForm


def index(request):
    rental = Rental.objects.all()
    return render(request, "index.html", {'rental': rental})


def createRental(request):
    if request.method == "POST":
        form = RentalForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = RentalForm()
    return render(request, "createRental.html", {'form': form})


def editRental(request, id):
    instance = Rental.objects.get(id=id)
    if request.method == "POST":
        form = RentalForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
    else:
        form = RentalForm()
    return render(request, "createRental.html", {'form': form})


def displayGenre(request):
    genre = Genre.objects.all()
    return render(request, "displayGenre.html", {'genre': genre})


def createGenre(request):
    if request.method == "POST":
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/displayGenre/")
    else:
        form = GenreForm()
    return render(request, "createGenre.html", {'form': form})


def editGenre(request, id):
    instance = Genre.objects.get(id=id)
    if request.method == "POST":
        form = GenreForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/displayGenre/")
    else:
        form = GenreForm()
    return render(request, "createGenre.html", {'form': form})


def displayDirector(request):
    director = Director.objects.all()
    return render(request, "displayDirector.html", {"director": director})


def createDirector(request):
    if request.method == "POST":
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/displayDirector/")
    else:
        form = DirectorForm()
    return render(request, "createDirector.html", {'form': form})


def editDirector(request, id):
    instance = Director.objects.get(id=id)
    if request.method == "POST":
        form = DirectorForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/displayDirector/")
    else:
        form = DirectorForm()
    return render(request, "createDirector.html", {'form': form})


def displayStatus(request):
    status = Status.objects.all()
    return render(request, "displayStatus.html", {'status': status})


def createStatus(request):
    if request.method == "POST":
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/displayStatus/")
    else:
        form = StatusForm()
    return render(request, "createStatus.html", {'form': form})


def editStatus(request, id):
    instance = Status.objects.get(id=id)
    if request.method == "POST":
        form = StatusForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/displayStatus/")
    else:
        form = StatusForm()
    return render(request, "createStatus.html", {'form': form})


def displayVideoTape(request):
    video = Videotape.objects.all()
    return render(request, "displayVideotape.html", {'video': video})


def createVideoTape(request):
    if request.method == "POST":
        form = VideotapeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/displayVideotape/")
    else:
        form = VideotapeForm()
    return render(request, "createVideotape.html", {'form': form})
