from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account

# Register your models here.
class AccountAdmin(UserAdmin):
    # apa saja yang di display
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    # menambahkan filter pencarian
    search_fields = ('email', 'username')
    # kolom yang hanya bisa diread, tidak bisa edit
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)