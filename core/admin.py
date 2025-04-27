from django.contrib import admin
from .models.user import User
from .models.account import Account

class UserAdmin(admin.ModelAdmin):
    list_display     = ('id', 'username', 'email', 'cpf',
                        'telephone_number', 'is_active',
                        'is_staff', 'created_at')
    search_fields    = ('username', 'email', 'cpf', 'telephone_number')
    list_filter      = ('is_active', 'is_staff')
    ordering         = ('-created_at',)
    list_per_page    = 25

admin.site.register(User, UserAdmin)


class AccountAdmin(admin.ModelAdmin):
    list_display     = ('id', 'user', 'name', 'balance', 'created_at')
    search_fields    = ('name', 'user__username', 'user__email')
    list_filter      = ('user__is_active',)
    ordering         = ('-created_at',)
    list_select_related = ('user',)
    list_per_page    = 25


admin.site.register(Account, AccountAdmin)
