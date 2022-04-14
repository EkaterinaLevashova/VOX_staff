from django import template

register = template.Library()


@register.filter(name='cut')  # <<<< WAY 2 - DECORATORS
def cut(value, arg):
    """
    This cuts out all values of 'arg' from the string!
    """
    return value.replace(arg, '')

#  register.filter('cut', cut)  <<<< WAY 1 - classic
