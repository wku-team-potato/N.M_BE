from datetime import date
from django.core.exceptions import ValidationError
from .models import PointTransaction

def add_points(user, points, description="보상"):
    """
    보상으로 포인트를 적립하는 함수.
    
    :param user: 포인트를 적립할 사용자
    :param points: 적립할 포인트 수 (양수)
    :param description: 트랜잭션 설명 (예: '출석 보상', '미션 완료 보상' 등)
    """
    if points <= 0:
        raise ValidationError("적립할 포인트는 양수여야 합니다.")
    
    # 포인트 적립
    user.profile.total_points += points
    user.save()
    
    # 트랜잭션 기록
    PointTransaction.objects.create(
        user=user,
        points_changed=points,
        transaction_type="추가",
        description=description,
        created_at=date.today()
    )

def deduct_points(user, points, description="사용"):
    """
    포인트를 차감하는 함수.
    
    :param user: 포인트를 차감할 사용자
    :param points: 차감할 포인트 수 (양수로 입력)
    :param description: 트랜잭션 설명 (예: '상점 구매', '이벤트 참여 차감' 등)
    """
    if points <= 0:
        raise ValidationError("차감할 포인트는 양수여야 합니다.")
    
    # 포인트 충분 여부 확인
    if user.profile.total_points < points:
        raise ValidationError("포인트가 부족합니다.")
    
    # 포인트 차감
    user.profile.total_points -= points
    user.save()
    
    # 트랜잭션 기록
    PointTransaction.objects.create(
        user=user,
        points_changed=-points,  # 차감된 포인트는 음수로 기록
        transaction_type="차감",
        description=description,
        created_at=date.today()
    )
