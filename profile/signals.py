from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.db import transaction

from profile.models import Profile
from profile.models import HeightWeightRecord

@receiver(pre_save, sender=Profile)
def update_profile(sender, instance, **kwargs):
    """__summary__
        description:
        - Profile 모델의 height, weight가 업데이트될 때마다 HeightWeightRecord 모델에 기록하는 signal
    """
    try:
        # 삭제 중에는 Signal 무시
        if not instance.pk or not Profile.objects.filter(pk=instance.pk).exists():
            return
        
        # 1. 기존 정보 조회
        old_profile = Profile.objects.get(pk=instance.pk)
        
        # 2. height, weight 변경 여부 확인
        height_changed = instance.height is not None and old_profile.height != instance.height
        weight_changed = instance.weight is not None and old_profile.weight != instance.weight

        # 3. 변경된 경우에만 기록
        if height_changed or weight_changed:
            changed_fields = {
                'height': instance.height if height_changed else old_profile.height,
                'weight': instance.weight if weight_changed else old_profile.weight,
            }
            
            # 4. 오늘 날짜의 기록이 있는지 확인
            today = timezone.now().date()
            existing_record = HeightWeightRecord.objects.filter(
                user_id=instance.user_id,
                created_at=today
            ).first()

            # 5. 기록 업데이트
            with transaction.atomic():
                # 6. 기록이 있는 경우에는 업데이트
                if existing_record:
                    existing_record.height = changed_fields['height']
                    existing_record.weight = changed_fields['weight']
                    existing_record.save()
                # 7. 기록이 없는 경우에는 생성
                else:
                    HeightWeightRecord.objects.create(
                        user_id=instance.user_id,
                        **changed_fields,
                        created_at=timezone.now()
                    )
    except Profile.DoesNotExist:
        # 신규 생성 시에는 기록을 남기지 않음
        pass
