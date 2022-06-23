from django.contrib import admin
#
# # Register your models here.
from user_auth.models import Account, Address
from django.contrib.auth.admin import UserAdmin


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    ...


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    ...

# admin.site.register(Account, UserAdmin)
