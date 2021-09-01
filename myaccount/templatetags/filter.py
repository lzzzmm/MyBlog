from django import template
register = template.Library()
@register.filter('strVal')
def strVal(value):
    return str(value)