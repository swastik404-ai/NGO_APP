from rest_framework import serializers
from .models import ProjectManagement
from django.utils.html import strip_tags

class ProjectManagementSerializer(serializers.ModelSerializer):
    start_date = serializers.DateField(format='%Y-%m-%d')
    end_date = serializers.DateField(format='%Y-%m-%d', required=False)
    goal_amount = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    description = serializers.SerializerMethodField()

    class Meta:
        model = ProjectManagement
        fields = ['project_id', 'project_name', 'featured_image', 'description',
                 'start_date', 'end_date', 'goal_amount', 'status']

    def get_description(self, obj):
        # Strip HTML tags and remove any extra whitespace
        clean_description = strip_tags(obj.description)
        return ' '.join(clean_description.split())