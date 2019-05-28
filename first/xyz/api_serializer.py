from rest_framework import serializers
from .models import UsersTbl, UserAccountDetailTbl, AdminUsersTbl

class UserSerailizer(serializers.ModelSerializer):
    class Meta:
        model = UsersTbl
        fields = ('user_id','user_name','user_email','user_mobile','user_dob','user_date_created','first_name','last_name','is_user_verified','is_email_verified','is_mob_num_verified')

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccountDetailTbl
        fields =('user_id','bank_acc_no','acc_holder_name','is_verified')
class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminUsersTbl
        fields = ('id','designation','name','access','loginemail')
