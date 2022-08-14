from django.contrib import admin
from currency.models import Rate, Source, ContactUs, ResponseLog


class RateAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'base_currency_type',
        'currency_type',
        'sale',
        'buy',
        'created',
    )

    def has_change_permission(self, request, obj=None):
        return False


class SourceAdmin(admin.ModelAdmin):
    list_display = (
        'source_name',
        'source_url',
        'created',
    )

    readonly_fields = (
        'created',
    )


class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email_from',
        'email_to',
        'subject',
        'date_message',
    )

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class ResponseLogAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'response_time',
        'request_method',
        'query_params',
        'ip_client',
        'path',
        'created',
    )


admin.site.register(Rate, RateAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(ResponseLog, ResponseLogAdmin)
