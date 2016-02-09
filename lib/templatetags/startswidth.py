#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""startswidth -- DESCRIPTION

"""
from django import template

register = template.Library()

@register.filter
def startswith(value, arg):
    """Usage, {% if value|starts_with:"arg" %}"""
    return value.startswith(arg)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# startswidth.py ends here
