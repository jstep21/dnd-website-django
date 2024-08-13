from django import template

register = template.Library()

@register.filter
def trim(value, chars):
    """
    Remove specified characters from the beginning and end of the string
    """
    if not isinstance(value, str):
        return value
    return value.strip(chars)
