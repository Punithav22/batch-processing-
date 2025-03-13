

# from django.contrib import admin
# from django.urls import path,include
# # from pro1.order import views


# urlpatterns = [
#     # path('',include('app1.urls')),
#     path('',include('app2.urls')),
#     path('punitha/',admin.site.urls),
#     ]

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include ('batch1.urls')), 
   
]




# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
