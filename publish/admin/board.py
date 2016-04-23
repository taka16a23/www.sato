#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""board -- DESCRIPTION

"""
from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from publish.models import DocumentModel
from publish.models import NewsCategoryModel, NewsPostModel


class DocumentForm(forms.ModelForm):
    r"""DocumentForm

    DocumentForm is a form.ModelForm.
    Responsibility:
    """
    title = forms.CharField(
        label=u'題名',
        widget=forms.TextInput(attrs={'placeholder': '4月15日号',}),
        help_text=mark_safe(u'回覧ページで表示される題名です。')
    )

    news_title = forms.CharField(
        label=u'おしらせ名',
        required=False,
        help_text=mark_safe(u'トップページで表示されるおしらせ名です。<br>入力がなかった場合、題名で表示されます'))

    class Meta(object):
        r"""Meta

        Meta is a object.
        Responsibility:
        """
        model = DocumentModel
        exclude = ['news', 'thumbnail', ]


class DocumentAdmin(admin.ModelAdmin):
    r"""DocumentAdmin

    DocumentAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    form = DocumentForm
    list_display = ('title', 'status', 'publish_date', 'expiry_date')
    list_editable = ('status', )
    ordering = ('-publish_date', )
    exclude = ('thumbnail', 'news', )
    radio_fields = {"status": admin.HORIZONTAL}

    class Media:
        css = {'all': ('css/admin_sato.css', ),}

    fieldsets = (
        (None,
         {'fields': ['title', 'status', 'file', ],}),
        (u'公開日/有効期限の設定',
         {'classes': ('collapse', ),
          'fields': [('publish_date', 'expiry_date'), ],}),
        (u'お知らせ名',
         {'classes': ('collapse', ),
          'fields': ['news_title', ],})
    )

    def get_form(self, request, obj=None, **kwargs):
        r"""SUMMARY

        get_form(request, obj=None, **kwargs)

        @Arguments:
        - `request`:
        - `obj`:
        - `kwargs`:

        @Return:

        @Error:
        """
        form = super(DocumentAdmin, self).get_form(request, obj=None, **kwargs)
        if obj is None:
            # created
            form.base_fields['news_title'].initial = None
        else:
            # change
            if obj.news is None:
                # don't have news
                form.base_fields['news_title'].initial = obj.title
            else:
                form.base_fields['news_title'].initial = obj.news.title
        return form

    def save_model(self, request, obj, form, change):
        r"""SUMMARY

        save_model(request, obj, form, change)

        @Arguments:
        - `request`:
        - `obj`:
        - `form`:
        - `change`:

        @Return:

        @Error:
        """
        super(DocumentAdmin, self).save_model(request, obj, form, change)
        newstitle = form.cleaned_data.get('news_title', None) or form.cleaned_data.get('title', None)
        url = '/board/?year=' + str(obj.publish_date.year)
        if obj.news is None: # update
            if newstitle is None:
                newstitle = obj.title
            obj.news = NewsPostModel.objects.create(
                title=newstitle,
                url=url,
                category=NewsCategoryModel.objects.get(name=u'回覧'),
                publish_date=obj.publish_date,
                expiry_date=obj.expiry_date,
                status=obj.status)
        else:
            if newstitle is not None:
                obj.news.title = newstitle
            obj.news.url = url
            obj.news.category = NewsCategoryModel.objects.get(name=u'回覧')
            obj.news.publish_date = obj.publish_date
            obj.news.expiry_date = obj.expiry_date
            obj.news.status = obj.status
            obj.news.save()
        obj.save()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# board.py ends here
