from django import template

register = template.Library()

@register.filter
def meu_filtro(data):
    return data + " - " + 'Alterado pelo filtro'


@register.filter
def arredonda(value, casas):
    return round(value, casas)


@register.filter
def footer_message():
    return "Desenvolvido por Ricardo Gaya"