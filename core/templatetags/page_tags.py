from decimal import Decimal

from django import template

register = template.Library()


def show_cookie(request, name):
    return request.COOKIES.get(name)


register.simple_tag(show_cookie)
