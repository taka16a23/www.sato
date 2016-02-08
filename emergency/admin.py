# -*- coding: utf-8 -*-

from django.contrib import admin
from emergency.models import Emergency
from django import forms

# Register your models here.
admin.site.disable_action('delete_selected')

def make_unpublish(modeladmin, request, queryset):
    r"""SUMMARY

    unpublish_all(modeladmin, request, queryset)

    @Arguments:
    - `modeladmin`:
    - `request`:
    - `queryset`:

    @Return:

    @Error:
    """
    queryset.update(status=1)

make_unpublish.short_description = u'非公開にする'


class EmergencyAdminForm(forms.ModelForm):
    r"""EmergencyAdminForm

    EmergencyAdminForm is a forms.ModelForm.
    Responsibility:
    """
    # def __init__(self, *args, **kwargs):
    #     r"""

    #     @Arguments:
    #     - `args`:
    #     - `kwargs`:
    #     """
    #     super(EmergencyAdminForm, self).__init__(*args, **kwargs)
    #     self.fields['status'].widget = admin.widgets.AdminRadioSelect()
    class Meta:
        model = Emergency
        fields = '__all__'
        widgets = {
            'title': admin.widgets.AdminTextInputWidget,
            'description': admin.widgets.AdminTextareaWidget,
            'published_from': admin.widgets.AdminSplitDateTime,
            'expires_on': admin.widgets.AdminSplitDateTime,
            'status': admin.widgets.AdminRadioSelect,}


class EmergencyAdmin(admin.ModelAdmin):
    r"""EmergencyAdmin

    EmergencyAdmin is a admin.Model.
    Responsibility:
    """
    form = EmergencyAdminForm
    list_display = ('title', 'published_from', 'expires_on', 'status', 'description')
    # list_editable = ('status',)

    actions = [make_unpublish, 'delete_selected']


admin.site.register(Emergency, EmergencyAdmin)
