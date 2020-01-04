from django.urls import path
from .views import BookmarkList, BookmarkCreate, BookmarkDetail, BookmarkDelete, BookmarkUpdate

app_name = 'bookmark'
urlpatterns = [
    path('', BookmarkList.as_view(), name = 'index'),
    path('detail/<int:pk>', BookmarkDetail.as_view(), name = 'detail'),
    path('update/<int:pk>', BookmarkUpdate.as_view(), name = 'update'),
    path('delete/<int:pk>', BookmarkDelete.as_view(), name = 'delete'),
    path('create/', BookmarkCreate.as_view(), name = 'create'),
]
