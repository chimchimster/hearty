from django import template

register = template.Library()


@register.filter(name='gender')
def define_gender(gender):

    if gender == 'М':
        return 'Мужчина'
    return 'Женщина'