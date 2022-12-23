from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from card import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.cards_list, name='cards_list'),
    path('generator/', views.card_generator, name='card_generator'),
    path('profile/', views.card_profile, name='card_profile'),
    path('delete/<int:card_id>/', views.delete_card, name='delete_card'),
    path('activate/<int:card_id>/', views.activate_card, name='activate_card')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
