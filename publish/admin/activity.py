#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""activity -- DESCRIPTION

"""
from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from publish.models import ActivityPostModel, TagModel
from publish.models import NewsCategoryModel, NewsPostModel
from django.db.models import ManyToOneRel
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
from django.core import exceptions


@admin.register(TagModel)
class TagModelAdmin(admin.ModelAdmin):
    r"""TagModelAdmin

    TagModelAdmin is a admin.ModelAdmin.
    Responsibility:
    """

def get_default_category():
    r"""SUMMARY

    get_default_category()

    @Return:

    @Error:
    """
    try:
        return NewsCategoryModel.objects.get(name=u'お知らせ')
    except exceptions.ObjectDoesNotExist:
        print('DEBUG-4-activity.py')
        return None


class ActivityPostForm(forms.ModelForm):
    r"""ActivityPostForm

    ActivityPostForm is a forms.Form.
    Responsibility:
    """
    news_title = forms.CharField(
        label=u'おしらせ名',
        required=False,
        help_text=u'入力がなかった場合、活動の題名で表示されます')
    categories = forms.ModelChoiceField(
        label=u'カテゴリー',
        # initial=get_default_category,
        queryset=NewsCategoryModel.objects.all(),
        required=False,
        empty_label=u'作成しない',
        help_text=mark_safe('お知らせを作成すると<br>公開日時にトップページで<br>おしらせが表示されます。')
    )

    def __init__(self, *args, **kwargs):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        super(ActivityPostForm, self).__init__(*args, **kwargs)
        categories = NewsCategoryModel.objects.all()
        self.fields['categories'].queryset = categories
        print('DEBUG-1-activity.py')
        # if categories.exists():
            # print(self.fields['categories'].initial)
            # self.fields['categories'].initial = list(NewsCategoryModel.objects.all())[-1]
        # rel = ManyToOneRel(NewsCategoryModel, 'name')
        # self.fields['categories'].widget = RelatedFieldWidgetWrapper(
            # self.fields['categories'].widget, rel, self.admin_site)

    class Meta(object):
        r"""Meta

        Meta is a object.
        Responsibility:
        """
        model = ActivityPostModel
        exclude = ['description', 'news', ]


@admin.register(ActivityPostModel)
class ActivityPostAdmin(admin.ModelAdmin):
    r"""ActivityPostAdmin

    ActivityPostAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    model = ActivityPostModel
    form = ActivityPostForm
    filter_horizontal = ['tags', ]

    list_display = ('title', 'publish_date', 'expiry_date',
                    'description', '_tags', 'status', )
    list_display_links = ("title", )
    list_editable = ('status', )
    ordering = ('-modified', )
    exclude = ('description', 'news', )
    radio_fields = {"status": admin.HORIZONTAL}
    date_hierarchy = 'publish_date'
    list_filter = ('status', 'publish_date', 'expiry_date', 'tags')

    class Media:
        css = {'all': ('css/admin_sato.css', ),}

    fieldsets = (
        (None,
         {'fields': ['title', 'status', 'body', 'tags', ],}),
        (u'公開日/有効期限の設定',
         {'classes': ('collapse', ),
          'fields': [('publish_date', 'expiry_date'), ],}),
        (u'お知らせ作成',
         {'fields': [('categories', 'news_title'), ],})
    )

    def _tags(self, row):
        return ','.join([x.name for x in row.tags.all()])

    def _category(self, row):
        r"""SUMMARY

        _category(row)

        @Arguments:
        - `row`:

        @Return:

        @Error:
        """
        if row.news:
            return row.news.category
        return ''

    def save_related(self, request, form, formsets, change):
        super(ActivityPostAdmin, self).save_related(request, form, formsets, change)
        # add tag of 年度
        instance = form.instance
        fiscalyear = instance.publish_date.year
        if instance.publish_date.month in (1, 2, 3):
            fiscalyear -= 1
        fiscalyearname = unicode(fiscalyear) + u'年度'
        tag, created = TagModel.objects.get_or_create(
            name=fiscalyearname, defaults={'name': fiscalyearname,})
        if not tag in list(instance.tags.all()):
            instance.tags.add(tag)

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
        form = super(ActivityPostAdmin, self).get_form(request, obj, **kwargs)
        if obj is None:
            # created
            form.base_fields['categories'].initial = get_default_category()
            form.base_fields['news_title'].initial = None
        else:
            # change
            if obj.news is None:
                # don't have news
                form.base_fields['news_title'].initial = obj.title
                form.base_fields['categories'].initial = None
            else:
                form.base_fields['news_title'].initial = obj.news.title
                form.base_fields['categories'].initial = obj.news.category
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
        super(ActivityPostAdmin, self).save_model(request, obj, form, change)
        if not change and form.cleaned_data['categories'] is None:
            # created and choiced empty
            return
        if change: # changed
            if form.cleaned_data['categories'] is None: # choiced empty
                if obj.news:
                    obj.news.delete()
                obj.news = None
                obj.save()
            else:
                # choiced categories
                newstitle = form.cleaned_data['news_title'] or form.cleaned_data['title']
                if obj.news is None:
                    # don't have news create category
                    obj.news = NewsPostModel.objects.create(
                        title=newstitle,
                        url=obj.get_absolute_url(),
                        category=form.cleaned_data['categories'],
                        publish_date=obj.publish_date,
                        expiry_date=obj.expiry_date,
                        status=obj.status)
                else:
                    # already have news to update
                    obj.news.title = newstitle
                    obj.news.url = obj.get_absolute_url()
                    obj.news.category = form.cleaned_data['categories']
                    obj.news.publish_date = obj.publish_date
                    obj.news.expiry_date = obj.expiry_date
                    obj.news.status = obj.status
                    obj.news.save()
        else: # created
            newstitle = form.cleaned_data['news_title'] or form.cleaned_data['title']
            news = NewsPostModel.objects.create(
                title=newstitle,
                url=obj.get_absolute_url(),
                category=form.cleaned_data['categories'],
                publish_date=obj.publish_date,
                expiry_date=obj.expiry_date,
                status=obj.status)
            obj.news = news
        obj.save()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# activity.py ends here
