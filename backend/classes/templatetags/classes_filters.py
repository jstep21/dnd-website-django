from django import template

register = template.Library()

@register.filter
def dict_key_exists(dictionary, key):
    return key in dictionary

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def dict_keys(dictionary):
    return dictionary.keys()

@register.filter
def generate_key(prefix, level):
    return f'{prefix}{level}'