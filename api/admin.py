from django.contrib import admin
from .models import Quote


class QuoteAdmin(admin.ModelAdmin):
    list_display = ("pk", "text", "author", "image")
    search_fields = ("text",)
    list_filter = ("text",)
    empty_value_display = "-пусто-"


admin.site.register(Quote, QuoteAdmin)
