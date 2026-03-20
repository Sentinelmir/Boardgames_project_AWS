from django import template

register = template.Library()


@register.filter
def stars(value):
    try:
        return "★" * int(value)
    except (TypeError, ValueError):
        return ""