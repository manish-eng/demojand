from django.contrib import admin
from gitpull.models import GitPull, SSHauth

# class GitPullAdmin(admin.ModelAdmin):
#     list_display=["username","password"]


class SSHauthAdmin(admin.ModelAdmin):
    list_display=["username","password","server_ip","posting_date"]

admin.site.register(GitPull)
admin.site.register(SSHauth,SSHauthAdmin)

