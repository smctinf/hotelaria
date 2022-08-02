from django import template

register = template.Library()

@register.filter
def uhPercent(obj):
    print(obj.n_uh_ocupados)
    try:
        return str(int(((obj.n_uh_ocupados)/(obj.hospedagem.n_total_uh))*100))+'%'
    except (ValueError, ZeroDivisionError):
        return None