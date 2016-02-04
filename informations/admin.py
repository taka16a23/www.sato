from django.contrib import admin
from informations.models import Information

# Register your models here.
class InformationAdmin(admin.ModelAdmin):
    r"""InformationAdmin

    InformationAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = ('title', 'pub_date', 'category', 'publish')

admin.site.register(Information, InformationAdmin)
