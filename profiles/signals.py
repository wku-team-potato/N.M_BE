from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone

from profiles.models import Profile, ProfileRecord

@receiver(pre_save, sender=Profile)
def update_profile(sender, instance, **kwargs):
    try:
        old_profile = Profile.objects.get(pk=instance.pk)
        changed_fields = {}

        # height가 변경되었는지 여부에 관계없이 현재 값과 이전 값을 모두 저장
        changed_fields['height'] = instance.height if instance.height is not None else old_profile.height
        
        # weight도 동일하게 처리
        changed_fields['weight'] = instance.weight if instance.weight is not None else old_profile.weight

        # 변화가 있는 경우 ProfileRecord 생성
        if old_profile.height != instance.height or old_profile.weight != instance.weight:
            ProfileRecord.objects.create(
                user_profile_id=instance,
                **changed_fields,
                recorded_at=timezone.now()
            )
    except Profile.DoesNotExist:
        # 기존 프로필이 없을 경우 예외 처리 (신규 생성 시)
        pass
