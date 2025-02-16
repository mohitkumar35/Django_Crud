from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    # path('first/', views.first, name='first'),
    # path('last/', views.last, name='last'),
    # path('letest/', views.letest, name='letest'),
    # path('earliast/', views.earliast, name='earliast'),
    # path('exists/', views.exists, name='exists'),
    # path('create/', views.create, name='create'),
    # path('get_or_create/', views.get_or_create, name='get_or_create'),
    # path('update/', views.update, name='update'),
    # path('delete/', views.delete, name='delete'),
    # path('count/', views.count, name='count'),
    # path('explain/', views.explain, name='explain'),
    # path('update_or_create/', views.update_or_create, name='update_or_create'),
    # path('bulk_create/', views.bulk_create, name='bulk_create'),
    # path('fillter_update/', views.fillter_update, name='fillter_update'),
    # path('get_delete/', views.get_delete, name='get_delete'),
    # path('fillter_delete/', views.fillter_delete, name='fillter_delete'),

    # path('all_details/', views.all_details, name='all_details'),
    # path('filter/', views.filter, name='filter'),
    # path('exclude/', views.exclude, name='exclude'),
    # path('assending/', views.assending, name='assending'),
    # path('decending/', views.decending, name='decending'),
    # path('decending2/', views.decending2, name='decending2'),
    # path('rendom/', views.rendom, name='rendom'),
    path('slice/', views.slice, name='slice'),
    path('query/', views.query, name='query'),
    path('edit/<int:x>', views.edit, name='edit'),
    path('update/<int:x>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
    


]