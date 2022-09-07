
from django.urls import path
from accounts import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'accounts'

urlpatterns = [

    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('activate/<uuid:username>/', views.UserActivateView.as_view(), name='user_activate'),
    path('my-profile/', views.UserProfileView.as_view(), name='my_profile'),

]

urlpatterns.extend(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
