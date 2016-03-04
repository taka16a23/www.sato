#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""forms -- DESCRIPTION

"""
from django.forms import Form
from django import forms
from django.utils.safestring import mark_safe

import datetime


def years():
    r"""SUMMARY

    years()

    @Return:

    @Error:
    """
    year = datetime.datetime.now().year
    return ((x, str(x) + '年') for x in range(year, year + 3))


MONTH = ((1, '1月'),
         (2, '2月'),
         (3, '3月'),
         (4, '4月'),
         (5, '5月'),
         (6, '6月'),
         (7, '7月'),
         (8, '8月'),
         (9, '9月'),
         (10, '10月'),
         (11, '11月'),
         (12, '12月'),
)

DAYS = ((1, '1日'),
        (2, '2日'),
        (3, '3日'),
        (4, '4日'),
        (5, '5日'),
        (6, '6日'),
        (7, '7日'),
        (8, '8日'),
        (9, '9日'),
        (10, '10日'),
        (11, '11日'),
        (12, '12日'),
        (13, '13日'),
        (14, '14日'),
        (15, '15日'),
        (16, '16日'),
        (17, '17日'),
        (18, '18日'),
        (19, '19日'),
        (20, '20日'),
        (21, '21日'),
        (22, '22日'),
        (23, '23日'),
        (24, '24日'),
        (25, '25日'),
        (26, '26日'),
        (27, '27日'),
        (28, '28日'),
        (29, '29日'),
        (30, '30日'),
        (31, '31日'),
)

HOURS = ((8, '8時'),
         (9, '9時'),
         (10, '10時'),
         (11, '11時'),
         (12, '12時'),
         (13, '13時'),
         (14, '14時'),
         (15, '15時'),
         (16, '16時'),
         (17, '17時'),
         (18, '18時'),
         (19, '19時'),
         (20, '20時'),
         (21, '21時'),
         (22, '22時'),
)

MINUTES = ((0, '00分'),
           (10, '10分'),
           (20, '20分'),
           (30, '30分'),
           (40, '40分'),
           (50, '50分'),
)

ROOMS = ((u'ホール', u'ホール'),
         (u'2階和室', u'2階和室'))


class HorizRadioRenderer(forms.RadioSelect.renderer):
    """ this overrides widget method to put radio buttons horizontally
        instead of vertically.
    """
    def render(self):
            """Outputs radios"""
            return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


class HallBookingForm(Form):
    r"""HallBookingForm

    HallBookingForm is a ModelForm.
    Responsibility:
    """
    error_css_class = 'error'
    required_css_class = 'required'

    orgname = forms.CharField(label=u'団体名', required=True,
        widget=forms.TextInput(
            attrs={'placeholder': u'ブロック1/1-1組', 'class': 'textinput',}))
    name = forms.CharField(label=u'使用責任者', required=True,
        widget=forms.TextInput(
            attrs={'placeholder': u'田中美里', 'class': 'textinput',}))
    address = forms.CharField(label=u'住所', required=True,
        widget=forms.TextInput(
            attrs={'placeholder': u'里5丁目7-22', 'class': 'textinput',}))
    phone = forms.CharField(label=u'TEL', required=True,
        widget=forms.TextInput(
            attrs={'placeholder': u'090-XXXX-XXXX', 'class': 'textinput',}))
    email = forms.EmailField(label=u'メールアドレス', required=True,
        widget=forms.EmailInput(
            attrs={'placeholder': u'example@example.com', 'class': 'textinput',}))
    purpose = forms.CharField(label=u'使用目的(会合名称)', required=True,
        widget=forms.TextInput(
            attrs={'placeholder': u'ブロック1/1-1組会合',
                   'class': 'textinput',}))
    matter = forms.CharField(
        label=u'内容', required=False,
        widget=forms.TextInput(
            attrs={'placeholder': u'ごみステーションについての話し合い',
            'class': 'textinput',}))
    room = forms.ChoiceField(
        label='使用室名',
        initial=u'ホール',
        choices=ROOMS,
        required=False,
        widget=forms.RadioSelect(renderer=HorizRadioRenderer),
    )
    startyear = forms.ChoiceField(choices=years)
    startmonth = forms.ChoiceField(choices=MONTH)
    startday = forms.ChoiceField(choices=DAYS)
    starthour = forms.ChoiceField(choices=HOURS)
    startminutes = forms.ChoiceField(choices=MINUTES)
    endhour = forms.ChoiceField(choices=HOURS)
    endminutes = forms.ChoiceField(choices=MINUTES)
    body = forms.CharField(
        label=u'備考欄', required=False,
        widget=forms.Textarea(attrs={'style':'resize:none;'}))

    def clean(self, ):
        r"""SUMMARY

        clean()

        @Return:

        @Error:
        """
        cleaned_data = super(HallBookingForm, self).clean()
        now = datetime.datetime.now()
        booking = datetime.datetime(
            int(cleaned_data['startyear']), int(cleaned_data['startmonth']),
            int(cleaned_data['startday']), int(cleaned_data['starthour']),
            int(cleaned_data['startminutes']),)
        if booking < now:
            raise forms.ValidationError(u'過去の日時は指定できません')
        return cleaned_data



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# forms.py ends here
