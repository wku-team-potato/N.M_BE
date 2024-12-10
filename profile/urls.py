from django.urls import path, include
from . import views

# 주석은 더 세부적인 api가 필요할 때 사용할 수 있도록 남겨둠
urlpatterns = [
    # username(=nickname) 업데이트
    # path('username/update/<int:user_id>/', views.UserNameUpdateView.as_view(), name='update_username'),
    # path('username/update/', views.UserNameUpdateView.as_view(), name='update_username'),
    # height, weight 업데이트
    # path('heightweight/update/<int:user_id>/', views.HeightWeightUpdateView.as_view(), name='update_heightweight'),
    path('heightweight/update/', views.HeightWeightUpdateView.as_view(), name='update_heightweight'),
    # username, height, weight 업데이트
    path('usernameheightweight/update/', views.UserNameHeightWeightUpdateView.as_view(), name='update_usernameheightweight'),
    # username 조회
    # path('username/retrieve/<int:user_id>/', views.UserNameRetrieveView.as_view(), name='retrieve_username'),
    # height, weight 조회
    # path('heightweight/retrieve/<int:user_id>/', views.UserHeightWeightRetrieveView.as_view(), name='retrieve_heightweight'),
    # total_points 조회
    # path('totalpoints/retrieve/<int:user_id>/', views.UserTotalPointsRetrieveView.as_view(), name='retrieve_totalpoints'),
    path('totalpoints/retrieve/', views.UserTotalPointsRetrieveView.as_view(), name='retrieve_totalpoints'),
    # profile 전체 조회
    # path('all/retrieve/<int:user_id>/', views.UserProfileRetrieveView.as_view(), name='retrieve_profile'),
    # height, weight 기록 조회
    # path('heightweightrecord/list/<int:user_id>/', views.HeightWeightRecordListView.as_view(), name='list_heightweightrecord'),
    path('heightweightrecord/list/', views.HeightWeightRecordListView.as_view(), name='list_heightweightrecord'),
    # 랭킹
    path('rankings/top3/', views.Top3RankingsView.as_view(), name='rankings-top3'),
    path('rankings/my/', views.MyRankingView.as_view(), name='rankings-my'),
    path('userprofile/<int:user_id>/', views.GetUserProfilebyIdView.as_view(), name='userprofile'),
]