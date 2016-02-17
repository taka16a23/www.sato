#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""forms -- DESCRIPTION

"""
from django.forms import ModelForm
from contact.models import ContactModel
from captcha.fields import CaptchaField


class ContactForm(ModelForm):
    r"""ContactForm

    ContactForm is a ModelForm.
    Responsibility:
    """
    # もしスパムがひどい用ならコメントアウト
    # captcha = CaptchaField()
    class Meta:
        model = ContactModel
        exclude = ('created', 'finished', )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# forms.py ends here
