#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""forms -- DESCRIPTION

"""
from django.forms import ModelForm
from django import forms
from django.forms import Form
from django.utils.safestring import mark_safe
from django.core.mail import EmailMessage

from about.models import ContactedModel, HallReceiverModel
from sato import settings
from about import PHONE_NUMBER, DEADLINE

import datetime

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

ROOMS = ((u'大ホール', u'大ホール'),
         (u'2階和室', u'2階和室'),
         (u'自治会館2F', '自治会館2F'))


ACCEPT_MSG = u"""
{2[name]} 様

里自治会です。公民館利用申込みを受け付けました。
受付番号は【{0}】です。
内容を確認後、ご連絡いたします。
{1[deadline]}以内にこちらから連絡がない場合は、電話番号: {1[phone]} にて、ご連絡をお願いいたします。

○ 以下の内容で受付しました --

使用責任者: {2[name]}
団体名: {2[orgname]}
住所: {2[address]}
TEL: {2[phone]}
Email: {2[email]}
日時: {2[startyear]}年{2[startmonth]}月{2[startday]}日 {2[starthour]:02}時{2[startminutes]:02}分 から {2[endhour]:02}時{2[endminutes]:02}分
使用室名: {2[room]}
使用目的: {2[purpose]}
内容: {2[matter]}
備考:
{2[body]}
--------------------------------------------

■本メールは自動配信しています。
■本メールにお心当たりがない場合は、メールを削除いただきますようお願いいたします。

◇電話でのお問合せ
里自治会 {1[phone]}
"""

NOTIFY_MSG = u"""
ホームページ訪問者から公民館利用申込みがありました。

受付番号は【{0}】

※必ず入力者と連絡をとってください。
  対応が遅れる場合はその旨の返答をしてください。

使用責任者: {1[name]}
団体名: {1[orgname]}
住所: {1[address]}
TEL: {1[phone]}
Email: {1[email]}
日時: {1[startyear]}年{1[startmonth]}月{1[startday]}日 {1[starthour]:02}:{1[startminutes]:02} から {1[endhour]:02}:{1[endminutes]:02}
使用室名: {1[room]}
使用目的: {1[purpose]}
内容: {1[matter]}
備考:
{1[body]}

"""


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
            attrs={'placeholder': u'077-XXX-XXXX', 'class': 'textinput',}))
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
            attrs={'placeholder': u'ごみ集積所についての話し合い',
            'class': 'textinput',}))
    room = forms.ChoiceField(
        label='使用室名',
        initial=u'大ホール',
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
        try:
            booking = datetime.datetime(
                int(cleaned_data['startyear']), int(cleaned_data['startmonth']),
                int(cleaned_data['startday']), int(cleaned_data['starthour']),
                int(cleaned_data['startminutes']),)
        except KeyError as err:
            # for not POST
            return cleaned_data
        if booking < now:
            raise forms.ValidationError(u'過去の日時は指定できません')
        return cleaned_data

    def send_notify(self, accept_num):
        r"""SUMMARY

        send_notify(accept_num)

        @Arguments:
        - `accept_num`:

        @Return:

        @Error:
        """
        data = self.clean()
        data['starthour'] = int(data['starthour'])
        data['startminutes'] = int(data['startminutes'])
        data['endhour'] = int(data['endhour'])
        data['endminutes'] = int(data['endminutes'])
        emails = [x.email for x in HallReceiverModel.objects.active()]
        subject = u'里公民館の申込みがありました 受付番号:{0}番'.format(
            accept_num)
        msg = EmailMessage(
            subject=subject,
            body=NOTIFY_MSG.format(accept_num, data),
            from_email=settings.EMAIL_HOST_USER, bcc=emails
        )
        return msg.send()

    def send_accept(self, accept_num):
        r"""SUMMARY

        send_accept(accept_num)

        @Arguments:
        - `accept_num`:

        @Return:

        @Error:
        """
        data = self.clean()
        data['starthour'] = int(data['starthour'])
        data['startminutes'] = int(data['startminutes'])
        data['endhour'] = int(data['endhour'])
        data['endminutes'] = int(data['endminutes'])
        content = {}
        content['deadline'] = DEADLINE
        content['phone'] = PHONE_NUMBER
        subject = u'里公民館の申込みを受付しました'
        print(data)
        print(content)
        print(ACCEPT_MSG.format(accept_num, content, data))
        msg = EmailMessage(
            subject=subject, body=ACCEPT_MSG.format(accept_num, content, data),
            from_email=settings.EMAIL_HOST_USER, to=[data['email'], ])
        return msg.send()


class ChildrenPostForm(Form):
    r"""ChildrenPostForm

    ChildrenPostForm is a Form.
    Responsibility:
    """
    # もしスパムがひどい用ならコメントアウト
    # captcha = CaptchaField()
    error_css_class = 'error'
    required_css_class = 'required'

    name = forms.CharField(label=u'使用責任者', required=True,
        widget=forms.TextInput(
            attrs={'placeholder': u'田中美里', 'class': 'textinput',}))
    address = forms.CharField(label=u'住所', required=True,
        widget=forms.TextInput(
            attrs={'placeholder': u'里5丁目7-22', 'class': 'textinput',}))
    phone = forms.CharField(label=u'TEL', required=True,
        widget=forms.TextInput(
            attrs={'placeholder': u'077-XXX-XXXX', 'class': 'textinput',}))
    email = forms.CharField(widget=forms.TextInput(attrs={'size': 40,}))
    body = forms.CharField(
        label=u'内容', required=True, widget=forms.Textarea())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# forms.py ends here
