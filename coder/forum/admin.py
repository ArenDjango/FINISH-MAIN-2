from django.contrib import admin

from .models import Forum

class PostModelAdmin(admin.ModelAdmin):
		list_display = ["title", "timestamp"]
		list_display_links = ["timestamp"]
		list_filter = ["timestamp"]
		search_fields = ["title", "content"]
		class Meta:
			model = Forum


admin.site.register(Forum, PostModelAdmin)