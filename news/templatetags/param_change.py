from django import template

register = template.Library()

@register.simple_tag()
def url_replace(request, key, value):
    copied      = request.GET.copy()
    if value == "" and key in copied:
        copied.pop(key)
    elif value == "":
        pass
    else:
        copied[key] = value
    
    return copied.urlencode()