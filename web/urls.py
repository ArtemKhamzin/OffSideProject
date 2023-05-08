from django.urls import path
from web.views import main_view, registration_view, auth_view, logout_view, blog_edit_view, tags_view, tags_delete_view, \
    blogs_delete_view, analytics_view

urlpatterns = [
    path('', main_view, name='main'),
    path('analytics/', analytics_view, name='analytics'),
    path('registration/', registration_view, name='registration'),
    path('auth/', auth_view, name='auth'),
    path('logout/', logout_view, name='logout'),
    path("blogs/add/", blog_edit_view, name="blogs_add"),
    path("blogs/<int:id>/", blog_edit_view, name="blogs_edit"),
    path("blogs/<int:id>/delete/", blogs_delete_view, name="blogs_delete"),
    path("tags/", tags_view, name="tags"),
    path("tags/<int:id>/delete/", tags_delete_view, name="tags_delete")
]
