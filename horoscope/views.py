from django.shortcuts import render

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from dataclasses import dataclass

# @dataclass
# class Person:
#     name: str
#     age: int
#     def __str__(self):
#         return f'Перед вами {self.name} возраста {self.age}'
# mike =Person('Nick',23)
# print(mike.age)

zodiac_dict = {
    "aries": "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).",
    "taurus": "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).",
    "gemini": "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
    "cancer": "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).",
    "leo": "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).",
    "virgo": "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
    "libra": "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
    "scorpio": "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
    "sagittarius": "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).",
    "capricorn": "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
    "aquarius": "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
    "pisces": "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)."
}
zodiac_by_element = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}


def index(request):
    zodiac = list(zodiac_dict)
    # li_elements += f'<li><a href={redirect_path}>{sign.title()}</a></li>'
    context = {
        'zodiacs': zodiac,
        'zodiac_dict': zodiac_dict,
    }
    return render(request, 'horoscope/index.html', context=context)


def index2(request):
    stixii = list(zodiac_by_element)
    li_elements = ''
    for stix in stixii:
        redirect_path = reverse('element-name', args=(stix,))
        li_elements += f'<li><a href={redirect_path}>{stix.title()}</a></li>'
    response = f'''
    <ol>
    {li_elements}
    </ol> 
    '''
    return HttpResponse(response)


def type_element(request, element):
    descriptioin = zodiac_by_element.get(element.lower(), None)
    if descriptioin:
        li_elements = ''
        for sign in descriptioin:
            redirect_path = reverse('horoscope-name', args=(sign,))
            li_elements += f'<li><a href={redirect_path}>{sign.title()}</a></li>'
            response = f'''
            <ol>
            {li_elements}
            </ol> 
            '''
        return HttpResponse(f'<h3>{response}</h3>')
    else:
        return HttpResponseNotFound(f"Неизвестня стихия - {element}")


def get_horoscope_by_sign(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    data = {
        'description_zodiac': description,
        'sign': sign_zodiac,
        # 'my_list': [1,2,3],
        # 'my_tuple': (1,2,3),
        # 'my_int': 100500,
        # 'my_dict': {'name' : 'Jack', 'age':20},
        # 'my_float': 333.33,
        # 'my_class': Person('Nick',31)
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)
    # responce = render_to_string('horoscope/info_zodiac.html')
    # return HttpResponse(responce)


def get_horoscope_by_number(request, sign_zodiac: int):
    zodiac = list(zodiac_dict)
    if sign_zodiac > len(zodiac):
        return HttpResponseNotFound(f"Был передан неправильный порядковый номер {sign_zodiac} знака зодиака")
    name_zodiac = zodiac[sign_zodiac - 1]
    redirect_url = reverse('horoscope-name', args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)

# def get_horoscope_by_number(request, sign_zodiac: int):
#     zodiac = list(zodiac_dict)
#     if sign_zodiac > len(zodiac):
#         return HttpResponseNotFound(f"Был передан неправильный порядковый номер {sign_zodiac} знака зодиака")
#     name_zodiac = zodiac[sign_zodiac - 1]
#     return HttpResponseRedirect(f'horoscope/{name_zodiac}')


# response= '<br> '.join(zodiac) - тэг <br> </br> это просто перенос на следующую строку
# или есть HTML лист. Вот пример:
# <ol>
# <li>aries</li>
# <li>leo</li>
# </ol>

# вот без ссылки просто HTML
# def index(request):
#     zodiac = list(zodiac_dict)
#     li_elements = ''
#     for sign in zodiac:
#         li_elements += f'<li>{sign}</li>'
#     response = f'''
#     <ol>
#     {li_elements}
#     </ol>
#     '''
#     return HttpResponse(response)
