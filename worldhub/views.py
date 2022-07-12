from django.shortcuts import render
from django.http import HttpResponse

from worldhub.controllers.worldgen import generateWorld


def index(request):
    world = generateWorld()
    kingdoms = world.kingdoms
    religions = world.religions
    return render(request, 'world_display.html', {'world' : world, 'kingdoms':kingdoms, 'religions': religions})
