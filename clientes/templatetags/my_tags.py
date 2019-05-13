import  datetime
from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def current_time(context, format_string):
    return datetime.datetime.now().strftime(format_string)


@register.simple_tag
def footer_message():
    return "Desenvolvido por Ricardo Gaya em Django 2.2"
