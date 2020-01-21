from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('signin', views.signin),
    path('register', views.register),
    path('dashboard', views.dashboard),
    path('dashboard/admin', views.admin_dashboard),
    path('users/new', views.users_new),
    path('users/show/<int:user_id>', views.the_wall),
    path('users/edit/<int:user_id>', views.edit_user),
    path('users/edit', views.edit_self),
    # POST METHODS
    path('log_in', views.log_in),
    path('log_out', views.log_out),
    path('create_user', views.create_user),
    path('users/make_changes', views.make_changesx),
    path('users/change_password', views.change_passwordx),
    path('users/edit/<int:user_id>/make_changes', views.make_changes),
    path('users/edit/<int:user_id>/change_password', views.change_password),
    path('confirmation/<int:user_id>', views.confirmation),
    path('confirmation/<int:user_id>/delete', views.delete_user),
    

    
]
