from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('profile/', views.profile, name='profile'),
  path('logout/', views.logout, name='logout'),
  path('post/<int:post_id>', views.view_post, name='post'),
  path('test/<str:city_name>', views.test, name='test'),
  path('edit/<int:post_id>',views.edit_post, name='edit'),
  path('test/<str:city_name>/delete/<int:post_id>', views.delete, name='delete')

]