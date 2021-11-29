"""userapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from usermanage.views import *


route = routers.DefaultRouter()

route.register(r'user', UserView)
route.register(r'activity', ActivityView)
route.register(r'comment', CommentView)
route.register(r'application', ApplicationView)
route.register(r'reply', ReplyView)
# route.register(r'commentToActivity', CommentToActivityView)
route.register(r'banuser', BanUserView)
route.register(r'feedback', FeedbackView)
route.register(r'participate', ParticipateView)


urlpatterns = [
    path('admin/', admin.site.urls),
    url('', include(route.urls)),
    url(r'activity_new', ActivitynewView.as_view()),
    url(r'activity_pt/', ActivityptView.as_view()),
    url(r'activity_pic', ActivitypicView.as_view()),
    url(r'activity_op', ActivityOpView.as_view()),
    # url(r'comment/new/toActivity', CommentNewView.as_view()),
    url(r'comment_all/', CommentAllView.as_view()),
    url(r'user_profile/', UserprofileView.as_view()),
    url(r'user_application/', UserapplicationView.as_view()),
    url(r'enrollment_participate/', EnrollView.as_view()),
    url(r'enrollment_all/', EnrollmentallView.as_view()),
    url(r'adminuser/login/', AdminLoginView.as_view()),
    url(r'adminuser/logout', AdminLogoutView.as_view()),
    url(r'signup/', SignupView.as_view()),
    url(r'participants', ParticipantsAllView.as_view()),
    url(r'blacklist', BlacklistView.as_view()),
    url(r'oneActivity', OneActivityView.as_view()),
    url(r'comment_delete/', CommentDeleteView.as_view()),
    url(r'comment_add/', CommentAddView.as_view()),
    url(r'comments_act_all/', CommentsActAllView.as_view()),
    url(r'adminuser/info', AdminInfoView.as_view()),
    url(r'comment_addToActivity/', CommentNewView.as_view()),
]
