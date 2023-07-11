from django import template

register = template.Library()

@register.filter
def uhPercent(obj):
    print(obj.hospedagem.n_total_uh)
    try:
        return str(int(((obj.n_uh_ocupados)/(obj.hospedagem.n_total_uh))*100))+'%'
    except (ValueError, ZeroDivisionError):
        return None

@register.filter
def maskCPF(obj):
    return 'CPF'