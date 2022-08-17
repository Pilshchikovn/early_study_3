from django.shortcuts import render

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

dct = {
    'monday': 'в понедельник работаю',
    'tuesday': 'во вторник - глазею в пропасть',
    'wednesday': 'в среду решаю проблему ',
    'thursday': 'в четверг - зарядка',
    'friday': 'в пятницу работаю',
    'saturday': 'в субботу - борьба ',
    'sunday': 'в воскресенье - работаю'
}
def index(request):
    return render(request, 'week_days/greeting.html')

def week_days_by_day(request, week_day):
    if week_day.lower() in dct:
        return HttpResponse(dct[week_day.lower()])
    return HttpResponseNotFound(f"Неизвестный день недели - {week_day}")


def week_days_by_number(request, week_day):
    if week_day in range(1, 8):
        dctlist = list(dct)
        name_week_day = dctlist[week_day - 1]
        redirect_url = reverse('week_day_name', args=(name_week_day,))
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound(f'Неверный номер дня - {week_day}')


# def week_days_by_number(request, week_day):
#     if week_day in range(1, 8):
#         dctlist = list(dct)
#         name_week_day = dctlist[week_day - 1]
#         return HttpResponseRedirect(f'{name_week_day}')
#     else:
#         return HttpResponseNotFound(f'Неверный номер дня - {week_day}')
