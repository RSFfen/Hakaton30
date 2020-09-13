#from django.shortcuts import render
from django.http import HttpResponse

def pupil_index(request) :
    return HttpResponse("Это точка входа для нашего ученика.")
