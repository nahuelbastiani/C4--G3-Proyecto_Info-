from django import template

register = template.Library()

def nombre_default(parametro1, parametro2):
    if parametro1:
        return parametro1
    return parametro2  
register.filter("nombre_default", nombre_default)