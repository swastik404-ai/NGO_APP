from django.contrib import admin
from .models import OrderManagement
from django.utils.translation import gettext_lazy as _

@admin.register(OrderManagement)
class OrderManagementAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'project_case_title', 'sender_name', 'donation_amount', 'currency', 'payment_status', 'created_date']
    list_filter = []
    search_fields = ['sender_name', 'recipient_name', 'project_case_title', 'phone']
    readonly_fields = [
        'order_id', 'project', 'case', 'project_case_title',
        'donation_amount', 'currency', 'sender_name', 'recipient_name',
        'phone', 'gift_template', 'payment_status', 'payment_information',
        'created_date'
    ]

    def has_add_permission(self, request):
        return False  # This removes the "Add" button

    def has_delete_permission(self, request, obj=None):
        return False  # Optional: This removes the "Delete" action

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']  # Remove bulk delete action
        return actions

    class Media:
        css = {
            'all': (
                'https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap',
            )
        }
