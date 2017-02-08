from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag
def is_active(request, url):
    if request.path in reverse(url):
        return "active"
    return ""