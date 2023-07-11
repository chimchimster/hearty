from django import template
from datetime import date

register = template.Library()


@register.filter(name='calc_age')
def calculate_age(bdate):
    today = date.today()

    age = today.year - bdate.year

    if today.month < bdate.month or (today.month == bdate.month and today.day < bdate.day):
        age -= 1

    return age