from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from mysite.core import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('upload/', views.upload, name='upload'),
    path('assignments/', views.assignment, name='assignments'),
    path('books/upload/', views.upload_1, name='upload_1'),
    path('books/<int:pk>/', views.delete_book, name='delete_book'),

    path('class/books/', views.BookListView.as_view(), name='class_book_list'),
    path('class/books/upload/', views.UploadBookView.as_view(), name='class_upload_book'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
