from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Activity)
admin.site.register(Comment)
admin.site.register(Application)
admin.site.register(Reply)
# admin.site.register(CommentToActivity)


admin.site.register(BanUser)
admin.site.register(Feedback)
admin.site.register(Participate)
admin.site.register(Admin)
admin.site.register(Token)
