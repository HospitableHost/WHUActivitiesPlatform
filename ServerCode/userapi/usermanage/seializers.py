from rest_framework import serializers
from .models import *


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        
class TokenSerializers(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = "__all__"

class ActivitySerializers(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = "__all__"

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class ApplicationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"

class  ReplySerializers(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = "__all__"

# class CommentToActivitySerializers(serializers.ModelSerializer):
#     class Meta:
#         model = CommentToActivity
    
class BanUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = BanUser
        fields = "__all__"

class FeedbackSerializers(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"

class ParticipateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Participate
        fields = "__all__"


class AdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = "__all__"