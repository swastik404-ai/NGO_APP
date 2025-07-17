from django.contrib import admin
from django.utils.html import format_html
from .models import ProjectManagement
from django.utils.translation import gettext_lazy as _
from django.contrib.admin import SimpleListFilter
from datetime import datetime
from django.db import models
from .forms import ProjectManagementAdminForm


@admin.register(ProjectManagement)
class ProjectManagementAdmin(admin.ModelAdmin):
    form = ProjectManagementAdminForm
    list_display = ['project_id', 'project_name', 'description_preview', 'formatted_start_date', 'formatted_end_date',
                    'formatted_goal_amount', 'status', 'action_buttons']
    list_filter = []
    search_fields = ['project_name', 'description']
    readonly_fields = ['start_date']

    def description_preview(self, obj):
        from django.utils.html import strip_tags
        clean_description = strip_tags(obj.description)
        return clean_description[:100] + '...' if len(clean_description) > 100 else clean_description

    description_preview.short_description = _('Description')

    def formatted_start_date(self, obj):
        return obj.start_date.strftime('%Y-%m-%d') if obj.start_date else ''

    formatted_start_date.short_description = _('Start Date')

    def formatted_end_date(self, obj):
        return obj.end_date.strftime('%Y-%m-%d') if obj.end_date else ''

    formatted_end_date.short_description = _('End Date')

    def formatted_goal_amount(self, obj):
        return f'{obj.goal_amount:,.2f} SAR' if obj.goal_amount else ''

    formatted_goal_amount.short_description = _('Goal Amount')

    def action_buttons(self, obj):
        return format_html(
            '<a class="button" href="{}" style="margin-right: 5px;">{}</a>'
            '<a class="button" href="{}" style="color: red;">{}</a>',
            f'/admin/project_management/projectmanagement/{obj.pk}/change/',
            _('Edit'),
            f'/admin/project_management/projectmanagement/{obj.pk}/delete/',
            _('Delete')
        )

    action_buttons.short_description = _('Actions')

    class Media:
        css = {
            'all': (
                'https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap',
            )
        }

    def get_fields(self, request, obj=None):
        fields = ['project_name', 'featured_image', 'description', 'end_date', 'goal_amount', 'status']
        if obj:  # If editing an existing object
            fields.insert(3, 'start_date')
        return fields