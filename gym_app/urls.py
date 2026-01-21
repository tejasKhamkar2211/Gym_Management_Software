"""from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('members/', views.members, name='members'),
    path('plans/', views.plans, name='plans'),
    path('trainers/', views.trainers, name='trainers'),
    path('payments/', views.payments, name='payments'),
]"""

'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('members/', views.members, name='members'),

    # Dummy routes (needed to avoid errors)
    path('members/add/', views.member_add, name='member_add'),
    path('members/edit/<int:id>/', views.member_edit, name='member_edit'),
    path('members/delete/<int:id>/', views.member_delete, name='member_delete'),
]
'''


from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('members/', views.members, name='members'),
    path('members/add/', views.member_add, name='member_add'),
    path('members/edit/<int:id>/', views.member_edit, name='member_edit'),
    path('members/delete/<int:id>/', views.member_delete, name='member_delete'),

    path('plans/', views.plans, name='plans'),
    path('trainers/', views.trainers, name='trainers'),
    path('payments/', views.payments, name='payments'),
]
