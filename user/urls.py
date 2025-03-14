from django.urls import path
# from rest_framework_simplejwt import views as jwt_views
from .views import LoginView, profile_view
from .views import login_view, register_view, logout_view, send_otp

urlpatterns = [
#     path('api/token', TokenObtainPairViewNew.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
#     path('api/token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path("send_otp",send_otp,name="send otp")
]

