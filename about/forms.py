#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""forms -- DESCRIPTION

"""
from django.forms import ModelForm
from django import forms
from about.models import ContactPostModel, ContactedModel
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

    # name = forms.CharField(label='お名前', max_length=50)
    email = forms.CharField(widget=forms.TextInput(attrs={'size': 40,}))
    # body = forms.CharField(
        # label=u'内容', required=True, widget=forms.Textarea())

    class Meta:
        model = ContactedModel
        exclude = ('created', 'modified', 'status', 'id', )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# forms.py ends here
