from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.MealCreateView.as_view(), name='meal_create'),
    path('update/<int:pk>', views.MealUpdateView.as_view(), name='meal_update'),
    path('delete/<int:pk>', views.MealDeleteView.as_view(), name='meal_delete'),
    # path('list/<str:date>/', views.MealListView.as_view(), name='meal_list'),
    # path('mealtype_list/<str:date>/<str:meal_type>', views.MealTypeListView.as_view(), name='meal_list'), 
    path('summary/<str:date>/', views.MealSummaryView.as_view(), name='meal_summary'),
    # path('summary/mealtype/<str:date>/<str:meal_type>', views.MealTypeSummaryView.as_view(), name='mealtype_summary'),
    # path('streak/', views.MealStreakView.as_view(), name='meal_streak'),
    path('list/<str:date>', views.UserMealDetailView.as_view(), name='meal_list'),
    path('listByUserId/<int:user_id>/<str:date>/', views.GetMealByuserIdView.as_view(), name='meal_list'),
]
