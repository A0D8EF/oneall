from django import template

register = template.Library()

@register.simple_tag()
def url_replace(request, key, value):
    copied      = request.GET.copy()

    if "major_category" in copied:
        copied.pop("major_category")
    elif "minor_category" in copied:
        copied.pop("minor_category")
    
    copied[key] = value

    return copied.urlencode()