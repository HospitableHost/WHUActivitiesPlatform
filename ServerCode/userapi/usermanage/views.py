from datetime import datetime
from django.shortcuts import render
from rest_framework import viewsets
from .models import *
import json
from django.views.generic import View
from .seializers import *
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.db.utils import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from userapi.settings import BASE_DIR
import uuid
import os



# Create your views here.
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers

class ActivityView(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializers

class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers

class ApplicationView(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializers

class ReplyView(viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializers

# class CommentToActivityView(viewsets.ModelViewSet):
#     queryset = CommentToActivity.objects.all()
#     serializer_class = CommentToActivitySerializers

class BanUserView(viewsets.ModelViewSet):
    queryset = BanUser.objects.all()
    serializer_class = BanUserSerializers

class FeedbackView(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializers

class ParticipateView(viewsets.ModelViewSet):
    queryset = Participate.objects.all()
    serializer_class = ParticipateSerializers


class ActivitynewView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(ActivitynewView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        data = json.loads(request.body)
        data["activity_id"]=uuid.uuid1()
        try:
            newactivity = Activity.objects.create(**data)
            newactivity = model_to_dict(newactivity)
            return JsonResponse({'code': 1000, 'msg': '????????????'}, status=201)
        except IntegrityError:
            return JsonResponse({'code': 1001, 'msg': '????????????'}, status=200)


class ActivityptView(View):
    def get(self, request):
        try:
            activities = Activity.objects.order_by("-publish_time")
            dic_activities=[]
            for activity in activities:
                dic_activity = model_to_dict(activity)
                dic_activities.append(dic_activity)

            return JsonResponse({'code': 1000, 'msg': 'success', 'data': dic_activities}, status=200)
        except Activity.DoesNotExist:
            return JsonResponse({'code': 1001, 'msg': '?????????'}, status=200)


class ActivitypicView(APIView):
    def post(self, request):
        ret = {'code': 1000, 'msg': None}
        file = request.FILES.get("file", None)
        if not file:
            ret['code'] = '1001'
            ret['msg'] = '????????????'
            return JsonResponse(ret)
        save_file = open(os.path.join(BASE_DIR, 'medias/' + file.name), 'wb+')
        for chunk in file.chunks():
            save_file.write(chunk)
        save_file.close()
        ret['msg'] = '????????????'
        ret['url'] = os.path.join(BASE_DIR, 'medias/' + file.name)
        return JsonResponse(ret)


class CommentNewView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(CommentNewView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        data = json.loads(request.body)
        data["comment_id"]=uuid.uuid1()
        try:
            newcomment = Comment.objects.create(**data)
            newcomment = model_to_dict(newcomment)
            user = User.objects.get(user_id=newcomment['user_id'])
            newcomment['user_nickname'] = user.user_nickname
            newcomment['user_avatar'] = user.user_avatar
            return JsonResponse({'code': 1000, 'message': '????????????', 'commentInfo': newcomment}, status=201)
        except IntegrityError:
            return JsonResponse({'code': 1001, 'message': '????????????'}, status=200)
        except User.DoesNotExist:
            return JsonResponse({'code': 1001, 'message': '????????????'}, status=200)


class CommentAllView(View):
    def get(self, request):
        if 'activity_id' in request.GET.keys() and 'user_id' in request.GET.keys():
            raise NotImplementedError
        elif 'activity_id' in request.GET.keys():  
            try:
                activity_id = request.GET.get('activity_id')
                comments = Comment.objects.filter(activity_id=activity_id)
                dic_comments=[]
                for comment in comments:
                    user = User.objects.get(user_id=comment.user_id)
                    dic_comment = model_to_dict(comment)
                    dic_comment['user_nickname'] = user.user_nickname
                    dic_comment['user_avatar'] = user.user_avatar
                    dic_comments.append(dic_comment)
                return JsonResponse({'code': 1000, 'msg': 'success', 'data': dic_comments}, status=201)
            except Comment.DoesNotExist:
                return JsonResponse({'code': 1001, 'msg': '?????????'}, status=200)
        else:
            try:
                user_id = request.GET['user_id']
                comments = Comment.objects.order_by("-comment_time")
                dic_comments=[]
                dic_bereplied = []
                dic_reply = []
                for comment in comments:
                    if comment.user_id == user_id:
                        assert type(comment.user_id) == str 
                        tmp_comment_id = comment.comment_id
                        user = User.objects.get(user_id=comment.user_id)
                        dic_comment = model_to_dict(comment)
                        dic_comment['user_nickname'] = user.user_nickname
                        dic_comment['user_avatar'] = user.user_avatar
                        dic_comments.append(dic_comment)
                        dic_bereplied.append(dic_comment)
                        while(True):
                            try:
                                reply = Reply.objects.get(to_id=tmp_comment_id)
                                user = User.objects.get(user_id=reply.user_id)
                                tmp_comment_id = reply.comment_id
                                dic_reply['user_nickname'] = user.user_nickname
                                dic_reply['user_avatar'] = user.user_avatar
                                dic_reply.append(reply)
                                dic_bereplied.append(reply)
                            except:
                                break
                return JsonResponse({'code': 1000, 'msg': 'success', 'commentToActivities': dic_comments, 'beReplied': dic_bereplied, 'reply': dic_reply}, status=201)
            except Comment.DoesNotExist:
                return JsonResponse({'code': 1001, 'msg': '?????????'}, status=404)

class EnrollView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(EnrollView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        data = json.loads(request.body)
        userid = data["user_id"]
        act_id = data["activity_id"]
        enrollments = Participate.objects.order_by("-parti_time")
        for enrollment in enrollments:
            if enrollment.user_id == userid and enrollment.activity_id == act_id:
                return JsonResponse({'code': 1001, 'msg': '??????????????????????????????'}, status=200)

        data["parti_id"]=uuid.uuid1()
        try:
            enrollment = Participate.objects.create(**data)
            enrollment = model_to_dict(enrollment)
            return JsonResponse({'code': 1000, 'msg': '????????????'}, status=201)
        except IntegrityError:
            return JsonResponse({'code': 1001, 'msg': '????????????'}, status=200)


class EnrollmentallView(View):
    def get(self, request):
        try:
            userid = request.GET["user_id"]
            enrollments = Participate.objects.order_by("-parti_time")
            dic_activities = []
            for enrollment in enrollments:
                if str(enrollment.user_id) == userid:
                    act_id = enrollment.activity_id
                    activity = Activity.objects.get(activity_id=act_id)
                    dic_activity = model_to_dict(activity)
                    dic_activities.append(dic_activity)
            return JsonResponse({'code': 1000, 'msg': 'success', 'activities': dic_activities}, status=201)
        except Participate.DoesNotExist:
            return JsonResponse({'code': 1001, 'msg': '???????????????'}, status=200)

class UserprofileView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(UserprofileView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        data = json.loads(request.body)
        user_nickname = data["user_nickname"]
        user_name = data["user_name"]
        school_id = data["school_id"]
        department = data["department"]
        try:    
            if User.objects.filter(user_nickname=user_nickname).exists():
                user = User.objects.get(user_nickname=user_nickname)
                if user.user_name==user_name and user.school_id==school_id and user.department==department:
                    return JsonResponse({'code': 1000, 'msg': '????????????', 'user_id': user.user_id}, status=201)
                else:
                    return JsonResponse({'code': 1001, 'msg': '????????????'}, status=200)
            else:
                return JsonResponse({'code': 1001, 'msg': '????????????'}, status=200)
        except IntegrityError:
            return JsonResponse({'code': 1001, 'msg': '????????????'}, status=200)

class UserapplicationView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(UserapplicationView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        data = json.loads(request.body)
        userid = data["user_id"]
        user = User.objects.get(user_id=userid)
        if user.is_banned != 0:
            return JsonResponse({'code': 1003, 'msg': '???????????????????????????????????????'}, status=200)
        elif user.user_auth == "???????????????":
            return JsonResponse({'code': 1002, 'msg': '????????????????????????'}, status=200)
        elif Application.objects.filter(user_id=userid).exists():
            return JsonResponse({'code': 1001, 'msg': '??????????????????????????????'}, status=200)
        else:
            data["application_id"]=userid
            data["application_time"]=datetime.now()
            Application.objects.create(**data)
            return JsonResponse({'code': 1000, 'msg': '??????????????????', 'user_id': userid}, status=201)

class SignupView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(SignupView, self).dispatch(request, *args, **kwargs)
    def put(selfself,request):
        data = json.loads(request.body)
        admin_userid=data["admin_userid"]
        activity_id=data["activity_id"]
        user_id=data["user_id"]
        status=data["status"]
        try:
            newactiviti=Activity.objects.filter(activity_id=activity_id).first()
            if not newactiviti:
                return JsonResponse({'code': 1001, 'msg': '??????????????????????????????'}, status=200)
            newactiviti=model_to_dict(newactiviti)
            if not newactiviti["user_id"]==admin_userid:
                return JsonResponse({'code': 1001, 'msg': '???????????????????????????'}, status=200)
            Participate.objects.filter(activity_id=activity_id,user_id=user_id).update(status=status)
            newparti=Participate.objects.filter(activity_id=activity_id,user_id=user_id).first()
            newparti=model_to_dict(newparti)
            if not newparti:
                return JsonResponse({'code': 1001, 'msg': '?????????????????????????????????'}, status=200)
            return JsonResponse({'code': 1000, 'msg': '????????????', 'participate':newparti}, status=201)
        except IntegrityError:
            return JsonResponse({'code': 1001, 'msg': '????????????'}, status=200)


class AdminLoginView(View):
    http_method_names = ['post']

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(AdminLoginView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        data = json.loads(request.body)
        username = data["username"]
        password = data["password"]
        try:    
            if Admin.objects.filter(username=username).exists():
                admin_user = Admin.objects.get(username=username)
                if admin_user.password==password:
                    token_data={}
                    token_data["token_id"]=admin_user.admin_id
                    
                    chech=Token.objects.filter(token_id=admin_user.admin_id)
                    if chech:
                        return JsonResponse({'code': 1003, 'message': '??????????????????'}, status=200)
                    Token.objects.create(**token_data)
                    
                    return JsonResponse({'code': 1000, 'message': '????????????', 'token': admin_user.admin_id}, status=201)
                else:
                    return JsonResponse({'code': 1001, 'message': '????????????'}, status=200)
            else:
                return JsonResponse({'code': 1002, 'message': '???????????????????????????'}, status=200)
        except IntegrityError:
            return JsonResponse({'code': 1004, 'message': '????????????'}, status=200)
    

class AdminLogoutView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(AdminLogoutView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        data = json.loads(request.body)
        token_id = data["token"]
        try:
            Token.objects.filter(token_id=token_id).first().delete()
            return JsonResponse({'code': 1000, 'msg': '????????????'}, status=200)
        except Token.DoesNotExist:
            return JsonResponse({'code': 1001, 'msg': '????????????'}, status=200)

class ActivityOpView(View):
    http_method_names = ['delete','get']
    def get(self, request):
        if 'admin_userid' in request.GET.keys():  
            try:
                admin_id = request.GET.get('admin_userid')
                activities = Activity.objects.order_by("-publish_time")
                dic_activities=[]
                for activity in activities:
                    if activity.user_id == admin_id:
                        dic_activity = model_to_dict(activity)
                        dic_activities.append(dic_activity)
                return JsonResponse({'code': 1000, 'msg': 'success', 'data': dic_activities}, status=201)
            except Comment.DoesNotExist:
                return JsonResponse({'code': 1001, 'msg': '?????????'}, status=200)

    def delete(self, request):
        print(request)
        if 'activity_id' in request.GET.keys() and 'admin_userid' in request.GET.keys():
            try:
                activity_id = request.GET.get('activity_id')
                admin_id = request.GET.get('admin_userid')
                if not Admin.objects.filter(admin_id=admin_id).exists():  # ??????????????????????????????????????????
                    return JsonResponse({'code': 1001, 'msg': '????????????'}, status=200)
                activity = Activity.objects.get(activity_id=activity_id)
                activity.delete()
                return JsonResponse({'code': 1000, 'msg': '????????????'}, status=201)
            except Comment.DoesNotExist:
                return JsonResponse({'code': 1001, 'msg': '?????????'}, status=200)


class ParticipantsAllView(View):
    def get(self, request):
        if 'admin_userid' in request.GET.keys() and 'activity_id' in request.GET.keys():  
            try:
                admin_id = request.GET.get('admin_userid')
                activity_id = request.GET.get('activity_id')
                if not Admin.objects.filter(admin_id=admin_id).exists():  # ??????????????????????????????????????????
                    return JsonResponse({'code': 1002, 'message': '????????????'}, status=200)
                participants = Participate.objects.order_by("-parti_time")
                dic_participants=[]
                for participant in participants:
                    if participant.activity_id == activity_id:
                        user = User.objects.get(user_id=participant.user_id)
                        dic_participant = model_to_dict(user)
                        dic_participant['status'] = participant.status
                        dic_participant['parti_time'] = participant.parti_time
                        dic_participants.append(dic_participant)
                if len(dic_participants) != 0:
                    return JsonResponse({'code': 1000, 'message': '????????????', 'data': dic_participants}, status=201)
                else:
                    return JsonResponse({'code': 1001, 'message': '????????????', 'data': dic_participants}, status=200)
            except Exception as e:
                print(e)
                return JsonResponse({'code': 1002, 'message': '????????????'}, status=200)


class BlacklistView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(BlacklistView, self).dispatch(request, *args, **kwargs)

    def delete(self,request):
        if 'admin_userid' in request.GET.keys() and 'banned_user_id' in request.GET.keys():
            try:
                admin_userid = request.GET.get('admin_userid')
                banned_user_id = request.GET.get('banned_user_id')
                if not Admin.objects.filter(admin_id=admin_userid).exists():  # ???????????????????????????????????????
                    return JsonResponse({'code': 1001, 'msg': '??????????????????????????????'}, status=200)
                del_blacklist = BanUser.objects.filter(banned_user_id=banned_user_id).first()
                if not del_blacklist:
                    return JsonResponse({'code': 1001, 'msg': '????????????????????????????????????'}, status=200)
                # del_blacklist = BanUser.objects.filter(banned_user_id=banned_user_id, org_admin_id=admin_userid).first()
                # if not del_blacklist:
                #     return JsonResponse({'code': 1001, 'msg': '??????????????????????????????????????????'}, status=200)

                del_blacklist=model_to_dict(del_blacklist)
                user_id=del_blacklist["user_id"]
                new_user=User.objects.filter(user_id=user_id).first()
                if not new_user:
                    BanUser.objects.filter(banned_user_id=banned_user_id).first().delete()
                    return JsonResponse({'code': 1001, 'msg': '??????????????????????????????'}, status=200)
                User.objects.filter(user_id=user_id).update(is_banned=0)
                BanUser.objects.filter(banned_user_id=banned_user_id).first().delete()
                return JsonResponse({'code': 1000, 'msg': '????????????'}, status=201)
            except Comment.DoesNotExist:
                return JsonResponse({'code': 1001, 'msg': '????????????'}, status=200)

    def post(self, request):
        data = json.loads(request.body)
        org_admin_id = data["org_admin_id"]
        act_id = data["activity_id"]
        user_id = data["user_id"]
        try:
            activity = Activity.objects.get(activity_id=act_id)
            if not Admin.objects.filter(admin_id=org_admin_id).exists():  # ??????????????????????????????
                return JsonResponse({'code': 1001, 'msg': '????????????1'}, status=200)
            elif activity.user_id != org_admin_id:  # ???????????????????????????????????????
                return JsonResponse({'code': 1001, 'msg': '????????????2'}, status=200)
            else:
                participants = Participate.objects.order_by("-parti_time")
                for participant in participants:
                    if participant.activity_id == act_id and participant.user_id == user_id:  # ???????????????????????????????????????
                        data["banned_user_id"] = uuid.uuid1()
                        BanUser.objects.create(**data)
                        return JsonResponse({'code': 1000, 'msg': '????????????'}, status=201)

                return JsonResponse({'code': 1001, 'msg': '????????????3'}, status=200)

        except Exception as e:
            print(e)
            return JsonResponse({'code': 1001, 'msg': '????????????4'}, status=200)

    def get(self, request):
        if 'admin_userid' in request.GET.keys():
            try:
                admin_userid = request.GET.get('admin_userid')
                if not Admin.objects.filter(admin_id=admin_userid).exists():  # ???????????????????????????????????????
                    return JsonResponse({'code': 1001, 'msg': '??????????????????????????????'}, status=200)
                dic_banuser = []
                for b in BanUser.objects.all():
                    u = model_to_dict(User.objects.get(user_id=b.user_id))
                    b = model_to_dict(b)
                    b.update(u)
                    dic_banuser.append(b)
                if len(dic_banuser) != 0:
                    return JsonResponse({'code': 1000, 'msg': '????????????', 'data': dic_banuser}, status=201)
                else:
                    return JsonResponse({'code': 1000, 'msg': '????????????'}, status=200)
            except:
                return JsonResponse({'code': 1000, 'msg': '????????????'}, status=200)

class OneActivityView(View):
    def get(self,request):
        if 'admin_userid' in request.GET.keys() and "activity_id" in request.GET.keys():
            try:
                admin_userid = request.GET.get('admin_userid')
                activity_id = request.GET.get('activity_id')
                if not Admin.objects.filter(admin_id=admin_userid).exists():  # ???????????????????????????????????????
                    return JsonResponse({'code': 1001, 'msg': '??????????????????????????????'}, status=200)
                new_activity=Activity.objects.filter(activity_id=activity_id).first()
                if not new_activity:
                    return JsonResponse({'code': 1000, 'msg': '???????????????????????????'}, status=200)
                new_activity=model_to_dict(new_activity)
                return JsonResponse({'code': 1000, 'msg': '????????????','data':new_activity}, status=200)
            except:
                return JsonResponse({'code': 1000, 'msg': '????????????'}, status=200)


class CommentDeleteView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(CommentDeleteView, self).dispatch(request, *args, **kwargs)

    def delete(self, request):
        if 'admin_userid' in request.GET.keys() and 'comment_id' in request.GET.keys():
            try:
                admin_userid = request.GET.get('admin_userid')
                comment_id = request.GET.get('comment_id')
                if not Admin.objects.filter(admin_id=admin_userid).exists():  # ???????????????????????????????????????
                    return JsonResponse({'code': 1001, 'msg': '??????????????????????????????'}, status=200)
                del_comment = Comment.objects.filter(comment_id=comment_id).first()
                if not del_comment:
                    return JsonResponse({'code': 1001, 'msg': '?????????????????????????????????'}, status=200)

                del_comment = model_to_dict(del_comment)
                user_id = del_comment["user_id"]
                activity_id = del_comment["activity_id"]

                new_activity = Activity.objects.filter(activity_id=activity_id).first()
                if not new_activity:
                    return JsonResponse({'code': 1001, 'msg': '??????????????????????????????'}, status=200)

                new_activity=model_to_dict(new_activity)
                ac_user_id=new_activity["user_id"]
                if not ac_user_id==admin_userid:
                    return JsonResponse({'code': 1001, 'msg': '????????????????????????????????????????????????'}, status=200)
                reply=Reply.objects.filter(to_comment_id=comment_id).first()
                if not reply:
                    Comment.objects.filter(comment_id=comment_id).first().delete()
                    reply_single=Reply.objects.filter(from_comment_id=comment_id).first()
                    if reply_single:
                        Reply.objects.filter(from_comment_id=comment_id).first().delete()
                    return JsonResponse({'code': 1000, 'msg': '????????????'}, status=200)

                father_comment=Reply.objects.filter(from_comment_id=comment_id).first()
                if father_comment:
                    Comment.objects.filter(comment_id=comment_id).update(comment_content="?????????????????????????????????",is_deleted=1)
                    return JsonResponse({'code': 1000, 'msg': '????????????'}, status=200)

                while Reply.objects.filter(father_comment_id=comment_id).first():
                    reply = Reply.objects.filter(father_comment_id=comment_id).first()
                    reply=model_to_dict(reply)
                    from_comment_id=reply["from_comment_id"]
                    del_reply=Comment.objects.filter(comment_id=from_comment_id).first()
                    if del_reply:
                        Comment.objects.filter(comment_id=from_comment_id).delete()
                    Reply.objects.filter(father_comment_id=comment_id).first().delete()
                Comment.objects.filter(comment_id=comment_id).delete()
                return JsonResponse({'code': 1000, 'msg': '????????????'}, status=200)
                
            except Comment.DoesNotExist:
                return JsonResponse({'code': 1001, 'msg': '????????????'}, status=200)

class CommentAddView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(CommentAddView, self).dispatch(request, *args, **kwargs)

    def post(self,request):
        data = json.loads(request.body)
        new_comment={}
        new_reply={}
        commentInfo={}
        new_comment["comment_id"]=uuid.uuid1()
        new_comment["user_id"]=data["user_id"]
        new_comment["activity_id"]=data["activity_id"]
        new_comment["comment_time"]=data["comment_time"]
        new_comment["comment_content"]=data["comment_content"]
        new_comment["user_status"]=data["user_status"]
        new_comment["is_deleted"]=0

        new_reply["from_comment_id"]=uuid.uuid1()
        new_reply["father_comment_id"]=data["father_comment_id"]
        new_reply["to_comment_id"]=data["to_comment_id"]

        commentInfo["from_comment_id"]=new_reply["from_comment_id"]
        commentInfo["comment_time"]=data["comment_time"]
        commentInfo["activity_id"]=data["activity_id"]
        commentInfo["user_id"]=data["user_id"]
        commentInfo["comment_content"]=data["comment_content"]
        commentInfo["to_comment_id"]=data["to_comment_id"]

        user=User.objects.filter(user_id=data["user_id"]).first()
        user=model_to_dict(user)
        commentInfo["user_nickname"]=user["user_nickname"]
        to_comment=Comment.objects.filter(comment_id=data["to_comment_id"]).first()
        to_comment=model_to_dict(to_comment)
        to_user = User.objects.filter(user_id=to_comment["user_id"]).first()
        to_user = model_to_dict(to_user)

        commentInfo["to_user_nickname"]=to_user["user_nickname"]

        try:
            new_comment = Comment.objects.create(**new_comment)
            new_reply = Reply.objects.create(**new_reply)

            return JsonResponse({'code': 1000, 'message': '????????????', 'commentInfo': commentInfo}, status=201)
        except IntegrityError:
            return JsonResponse({'code': 1001, 'message': '????????????'}, status=200)


class CommentsActAllView(View):
    def get(self,request):
        if not "activity_id" in request.GET.keys():
            return JsonResponse({'code': 1001, 'msg': '????????????'}, status=200)

        act_id = request.GET.get('activity_id')
        try:
            comments = Comment.objects.order_by("-comment_time")
            comments_all = []
            for comment in comments:  # ??????????????????????????????
                if comment.activity_id == act_id:
                    father_com_id = comment.comment_id
                    if not Reply.objects.filter(from_comment_id=father_com_id).exists():  # ????????????????????????
                        # ?????????
                        data = model_to_dict(comment)  # ??????????????????
                        data.pop("user_status")

                        father_user = User.objects.get(user_id=data["user_id"])
                        data["user_nickname"] = father_user.user_nickname
                        data["user_avatar"] = father_user.user_avatar

                        child_coms = []
                        if Reply.objects.filter(father_comment_id=father_com_id).exists():  # ???????????????
                            replys = Reply.objects.filter(father_comment_id=father_com_id)
                            for reply in replys:  # ????????????????????????
                                child_com = model_to_dict(reply)    # ??????????????????
                                child_com.pop("father_comment_id")

                                child_comment = Comment.objects.get(comment_id=child_com["from_comment_id"])
                                child_com["comment_time"] = child_comment.comment_time
                                child_com["activity_id"] = child_comment.activity_id
                                child_com["user_id"] = child_comment.user_id
                                child_com["comment_content"] = child_comment.comment_content

                                to_comment = Comment.objects.get(comment_id=child_com["to_comment_id"])
                                to_user_id = to_comment.user_id
                                to_user_nickname = User.objects.get(user_id=to_user_id).user_nickname
                                child_com["to_user_nickname"] = to_user_nickname

                                child_user = User.objects.get(user_id=child_com["user_id"])
                                child_com["user_nickname"] = child_user.user_nickname
                                child_coms.append(child_com)

                            # ????????????????????????
                            data["reply"] = child_coms[::-1]

                        comments_all.append(data)
                    else:     # ???????????????????????????
                        continue

            return JsonResponse({'code': 1000, 'msg': '????????????', 'data': comments_all}, status=200)

        except:
            return JsonResponse({'code': 1001, 'msg': '????????????'}, status=200)
            
            
            
class AdminInfoView(View):
    def get(self,request):
        if not "token" in request.GET.keys():
            return JsonResponse({'code': 1001, 'msg': '????????????'}, status=200)

        token = request.GET.get('token')
        try:
            admin_info={}
            user=User.objects.filter(user_id=token).first()
            user=model_to_dict(user)
            admin_info["name"]=user["user_nickname"]
            admin_info["avatar"]=user["user_avatar"]
            return JsonResponse({'code': 1000, 'msg': '????????????', 'data': admin_info}, status=200)
        except:
            return JsonResponse({'code': 1001, 'msg': '????????????'}, status=200)
            