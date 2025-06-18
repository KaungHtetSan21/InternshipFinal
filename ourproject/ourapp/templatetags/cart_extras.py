from django import template
register = template.Library()






register = template.Library()

@register.filter
def multiply(qty, price):
    return qty * price