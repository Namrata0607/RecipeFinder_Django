# recipes/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def split(value, delimiter):
    """Splits the value by the given delimiter."""
    return value.split(delimiter)

@register.filter
def trim(value):
    """Trims whitespace from the beginning and end of the string."""
    return value.strip()
