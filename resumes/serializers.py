from rest_framework import serializers
from .models import Resume

class ResumeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Resume
        fields = "__all__"
        read_only_fields = ("user", "created_at")
