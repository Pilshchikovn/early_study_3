from django.shortcuts import render

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse
from django.template.loader import render_to_string


def get_rectangle_area(request, width, height):
    return render(request, 'geometry/rectangle.html')
    # """(площадь прямоугольника) принимает длину и ширину фигуры"""
    # return HttpResponse(f'Площадь прямоугольника размером {width}x{height} равна {width*height}')


def get_square_area(request, width):
    return render(request, 'geometry/square.html')
    # """(площадь квадрата) принимает размер стороны квадрата"""
    # return HttpResponse(f'Площадь квадрата размером {width}x{width} равна {width*width}')


def get_circle_area(request, radius):
    return render(request, 'geometry/circle.html')
    # """(площадь круга) принимает радиус круга"""
    # return HttpResponse(f'Площадь круга радиуса {radius} равна {pi*radius**2}')

# def figure(request, figure: str):
#     if 'figure' in ('square', 'circle', 'rectangle'):
#         return render(request, f'geometry/{figure}')
#     else:
#         return HttpResponseBadRequest('Invalid url')
