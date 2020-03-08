from django.contrib import admin
from .models import *
from rest_framework.authtoken.admin import TokenAdmin
admin.site.register(Cat)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(FavoritePost)
TokenAdmin.raw_id_fields = ['user']


# Register your models here.
