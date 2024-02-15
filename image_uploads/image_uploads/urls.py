
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name = 'home'),
    path('upload/',views.upload,name = 'upload'),
    path('view/',views.view,name = 'view'),
    path('submit/',views.submit,name ='submit'),
    path('properties/<int:id>',views.properties,name = 'properties'),
    path('home/',views.home,name='home'),
    path('resize/<int:id>',views.resize,name='resize'),
    path('download/<int:id>',views.download,name = 'download'),
    path('display/<int:id>',views.display,name='display'),
    path('gray/<int:id>',views.gray,name='gray'),
    path('test/<int:id>',views.test,name='test'), 
    path('delete/<int:id>',views.delete,name = 'delete')   
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)