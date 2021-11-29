from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=40)
    user_nickname = models.CharField(max_length=14)
    user_name = models.CharField(max_length=5)
    school_id = models.CharField(max_length=13)
    user_auth = models.CharField(max_length=5, default="普通用户")
    is_banned=models.IntegerField(default=0)
    department=models.CharField(max_length=10)
    user_avatar = models.CharField(max_length=140, null=True,blank=True)  # new add
    
class Token(models.Model):
    token_id = models.CharField(primary_key=True, max_length=40)

class Activity(models.Model):
    activity_id=models.CharField(primary_key=True, max_length=40)
    user_id=models.CharField(max_length=40)
    organization_name=models.CharField(max_length=20)
    activity_type=models.CharField(max_length=20)
    activity_title=models.CharField(max_length=30)
    publish_time=models.DateTimeField()
    activity_detail=models.TextField()
    activity_post=models.CharField(max_length=70,null=True,blank=True)
    parti_ddl=models.DateTimeField()
    oriented_department=models.CharField(max_length=20)

class Comment(models.Model):
    comment_id = models.CharField(primary_key=True, max_length=40)
    user_id=models.CharField(max_length=40)
    activity_id=models.CharField(max_length=40)
    comment_time=models.DateTimeField()
    comment_content=models.CharField(max_length=140)
    user_status=models.CharField(max_length=20, default='普通用户')
    is_deleted=models.IntegerField(default=0)

class Application(models.Model):
    application_id = models.CharField(primary_key=True, max_length=40)
    user_id = models.CharField(max_length=40)
    application_time = models.DateTimeField()

class Reply(models.Model):
    to_comment_id = models.CharField(max_length=40)
    from_comment_id = models.CharField(primary_key=True, max_length=40, default="1")   # same as comment_id
    father_comment_id = models.CharField(max_length=40, default="1")

# class CommentToActivity(models.Model):
#     activity_id = models.CharField(primary_key=True, max_length=40)
#     comment_id = models.CharField(max_length=40)
#     user_status=models.CharField(max_length=20, default='普通用户')

class BanUser(models.Model):
    banned_user_id = models.CharField(primary_key=True, max_length=40)
    user_id=models.CharField(max_length=40)
    org_admin_id=models.CharField(max_length=40)
    activity_id=models.CharField(max_length=40)
    banned_time=models.DateTimeField()
    description=models.CharField(max_length=140)

class Feedback(models.Model):
    problem_id = models.CharField(primary_key=True, max_length=40)
    user_id=models.CharField(max_length=40)
    problem_content=models.TextField()

class Participate(models.Model):
    parti_id = models.CharField(primary_key=True, max_length=40)
    activity_id = models.CharField( max_length=40)
    user_id=models.CharField(max_length=40)
    parti_time=models.DateTimeField()
    status=models.IntegerField(default=0)

class Admin(models.Model):
    admin_id = models.CharField(primary_key=True, max_length=40)  # same as user_id
    username = models.CharField(max_length=13)  # same as school id
    password = models.CharField(max_length=20)
    
