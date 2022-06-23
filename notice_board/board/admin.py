from django.contrib import admin

from board.models import Notice, AccountNoticeRelation


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    ...


@admin.register(AccountNoticeRelation)
class AccountNoticeRelationAdmin(admin.ModelAdmin):
    ...
