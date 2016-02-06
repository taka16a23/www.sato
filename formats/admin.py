from django.contrib import admin
from formats.models import SatoFormat, OtherFormat


# Register your models here.
class SatoFormatAdmin(admin.ModelAdmin):
    r"""SatoFormatAdmin

    SatoFormatAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = ('title', 'description', 'file', 'form', 'sortid', 'publish')
    list_editable = ('sortid', 'publish', )
    ordering = ('sortid', )


class OtherFormatAdmin(admin.ModelAdmin):
    r"""OtherFormatAdmin

    OtherFormatAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = ('title', 'description', 'sortid', 'publish')
    list_editable = ('sortid', 'publish', )
    ordering = ('sortid', )


admin.site.register(OtherFormat, OtherFormatAdmin)
admin.site.register(SatoFormat, SatoFormatAdmin)
