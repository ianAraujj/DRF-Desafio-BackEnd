from rest_framework import serializers
from regular_plan.models import RegularPlan

class RegularPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegularPlan
        fields = "__all__"
    
    def validate(self, data):

        if data['publish'] == False:
            data['owner'] = None
        return data