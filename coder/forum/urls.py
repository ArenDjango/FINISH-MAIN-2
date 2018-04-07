from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from .views import(
	forum_list,
	forum_create,
	forum_detail,
	forum_update,
	forum_delete,
	)

app_name = 'forum'

urlpatterns = [
    path('', forum_list, name='list'),
    path('create/', forum_create),
    path('<int:id>/', forum_detail, name='detail'),
    path('<int:id>/edit/', forum_update, name='update'),
    path('<int:id>/delete/', forum_delete),
]