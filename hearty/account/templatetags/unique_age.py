from django import template

register = template.Library()


@register.filter(name='unique_age')
def unique_age(value):
    last_char = str(value)[-1]
    if last_char in ('5', '6', '7', '8', '9'):
        return str(value) + ' лет'
    elif last_char in ('2', '3', '4'):
        return str(value) +' года'
    else:
        return str(value) + ' год'