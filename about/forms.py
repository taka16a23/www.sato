#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""forms -- DESCRIPTION

"""
from django.forms import ModelForm
from django import forms
from about.models import ContactPostModel
# もしスパムがひどい用ならコメントアウト
# from captcha.fields import CaptchaField


class ContactPostForm(ModelForm):
    r"""ContactForm

    ContactForm is a ModelForm.
    Responsibility:
    """
    # もしスパムがひどい用ならコメントアウト
    # captcha = CaptchaField()
    error_css_class = 'error'
    required_css_class = 'required'

    email = forms.CharField(widget=forms.TextInput(attrs={'size': 40,}))

    class Meta:
        model = ContactPostModel
        exclude = ('created', 'finished', )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# forms.py ends here
