from django.urls import path
from . import views # import views from current directory

urlpatterns  = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('musicians/', views.musicians_index, name='musician-index'),
    path('musicians/<int:musician_id>/', views.musicians_detail, name='musician-detail'),
    path('musicians/create/', views.MusicianCreate.as_view(), name='musician-create'),
    path('musicians/<int:pk>/update/', views.MusicianUpdate.as_view(), name='musician-update'),
    path('musicians/<int:pk>/delete/', views.MusicianDelete.as_view(), name='musician-delete'),
    path('musicians/<int:musician_id>/add_music/', views.add_music, name='add-music'),
    path('tools/create/', views.ToolCreate.as_view(), name='tool-create'),
    path('tools/<int:pk>/', views.ToolDetail.as_view(), name='tool-detail'),
    path('tools/', views.ToolList.as_view(), name='tool-index'),
    path('tools/<int:pk>/update/', views.ToolUpdate.as_view(), name='tool-update'),
    path('tools/<int:pk>/delete/', views.ToolDelete.as_view(), name='tool-delete'),
    path('musicians/<int:musician_id>/associate-tool/<int:tool_id>/', views.associate_tool, name='associate-tool'),
    path('musicians/<int:musician_id>/remove-tool/<int:tool_id>/', views.remove_tool, name='remove-tool'),
]