


from django.contrib import admin
from django.urls import path, include
from portfolio import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('upload', views.model_form_upload, name='upload'),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)     #for image show

