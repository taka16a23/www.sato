# -*- coding: utf-8 -*-
from django.contrib import admin
from board.models import Board


# Register your models here.
class BoardAdmin(admin.ModelAdmin):
    r"""BoardAdmin

    BoardAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = ('title', 'published_from', 'expires_on', 'status')
    list_editable = ('status', )
    ordering = ('-published_from', )
    exclude = ('thumbnail', )

admin.site.register(Board, BoardAdmin)
