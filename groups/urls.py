from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateGroup.as_view(), name='create-group'),
    path('join/', views.GroupJoinView.as_view(), name='join-group'),
    path('leave/<int:group_id>/', views.GroupLeaveView.as_view(), name='leave-group'),
    path('list/', views.GroupListView.as_view(), name='group-list'),
    path('all/', views.GroupAllListView.as_view(), name='group-all-list'),
    path('update/<int:pk>/', views.GroupUpdateView.as_view(), name='update-group'),
    path('delete/<int:pk>/', views.GroupDeleteView.as_view(), name='delete-group'),
    path('search/<str:search>/', views.GroupSearchListView.as_view(), name='group-search-list'),
    path('top-ranking/', views.GroupTopRankingView.as_view(), name='group-ranking'),
    path('update-public/<int:group_id>/', views.UpdatePublicInfoView.as_view(), name='update-public'),
    path('members/detail/<int:pk>/', views.GroupDetailView.as_view(), name='group-member-detail'),
    path('member/detail/<int:group_id>/', views.MemberInfowithgroupView.as_view(), name='group-member-detail'),
]
