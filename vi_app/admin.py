from django.contrib import admin

from vi_app.models import Story, Resize


class StoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'title', 'description', 'created_at')
    list_filter = ('user_name',)
    search_fields = ('user_name', 'title',)


admin.site.register(Story, StoryAdmin)
admin.site.register(Resize)
