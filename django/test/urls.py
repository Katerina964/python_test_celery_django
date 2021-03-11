from django.urls import path, include

urlpatterns = [
    path('', include('news.urls')),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
