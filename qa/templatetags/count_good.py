from django import template

register    = template.Library()

@register.simple_tag()
def count_good(good_user):
    return len(good_user)