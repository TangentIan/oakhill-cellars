from django.contrib.humanize.templatetags.humanize import intcomma
from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def get_currency(rands, currency=None):
    if currency is None:
        currency = settings.CURRENCY.get("symbol")
    try:
        rands = float(rands)
        formatted_value = round(rands, 2)
    except ValueError:
        formatted_value = 0

    return "%s%s%s" % (
        currency,
        intcomma(int(formatted_value)),
        ("%0.2f" % formatted_value)[-3:],
    )
