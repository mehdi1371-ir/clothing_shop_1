from atexit import register
from django import template

register = template.Library()


@register.filter
def get_value(dict, arg):
    for value in dict.values():
        return f'{arg} : {value:.1f}'