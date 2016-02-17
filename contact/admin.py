from django.contrib import admin
from contact.models import ContactModel


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    r"""ContactAdmin

    ContactAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = ('name', 'title', 'created', 'email', 'body',  'finished')
    list_editable = ('finished', )

admin.site.register(ContactModel, ContactAdmin)
