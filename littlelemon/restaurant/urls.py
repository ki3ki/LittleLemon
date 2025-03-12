from django.urls import path, include
from .views import index, MenuItemView, SingleMenuItemView, BookingViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', index, name = 'index'),
    path('menu/', MenuItemView.as_view(), name='menu-list-create'),
    path('menu/<int:pk>/', SingleMenuItemView.as_view(), name='menu-detail'),
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token)
]
