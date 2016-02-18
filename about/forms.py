#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""forms -- DESCRIPTION

"""
from django.forms import ModelForm
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
    class Meta:
        model = ContactPostModel
        exclude = ('created', 'finished', )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# forms.py ends here
