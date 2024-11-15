from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from meal.models import UserMeal
from point.services import add_points

class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=20, verbose_name='닉네임', null=False, blank=False, unique=True)
    total_points = models.IntegerField(default=0)
    height = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    
    # Attendance fields
    consecutive_attendance_days = models.IntegerField(default=0)  # 연속 출석 일수
    cumulative_attendance_days = models.IntegerField(default=0)  # 누적 출석 일수
    last_attendance_date = models.DateField(null=True, blank=True)  # 마지막 출석 날짜
    
    # Goal achievement fields
    consecutive_goals_achieved = models.IntegerField(default=0)  # 연속 목표 달성
    cumulative_goals_achieved = models.IntegerField(default=0)  # 누적 목표 달성
    last_goal_date = models.DateField(null=True, blank=True)  # 마지막 목표 달성 날짜
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'profile'
        ordering = ['user_id']

    def update_attendance(self, meal_date):
        today = timezone.now().date()
        
        # 과거 날짜 체크 추가
        if meal_date != today or self.last_attendance_date == today:  # 이미 오늘 출석했으면 리턴
            return
            
        self.cumulative_attendance_days += 1
        if self.last_attendance_date == today - timezone.timedelta(days=1):
            self.consecutive_attendance_days += 1
        else:
            self.consecutive_attendance_days = 1
        add_points(self.user, 100, '출석 보상')
        self.last_attendance_date = today
        self.save()

    def update_goal_achievement(self):
        today = timezone.now().date()
        if self.last_goal_date == today:  # 이미 오늘 목표 달성했으면 리턴
            return
        
        # 오늘 날짜의 식사만 체크
        meals_today = UserMeal.objects.filter(
            user=self.user,  # Profile 객체 대신 User 객체 사용
            date=today  # 해당 날짜의 식사만 카운트
        ).values('meal_type').distinct().count()
        
        if meals_today == 3:
            self.cumulative_goals_achieved += 1
            if self.last_goal_date == today - timezone.timedelta(days=1):
                self.consecutive_goals_achieved += 1
            else:
                self.consecutive_goals_achieved = 1
            add_points(self.user, 200, '모든 식단 등록')
            self.last_goal_date = today
            self.save()

class HeightWeightRecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    height = models.FloatField()
    weight = models.FloatField()
    created_at = models.DateField(default=timezone.now, help_text="체중 기록일")

    class Meta:
        db_table = 'height_weight_record'
        ordering = ['-created_at']