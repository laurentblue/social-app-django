from django.conf import settings
from django.db import models


class UserSocialAuthManager(models.Manager):
    """Manager for the UserSocialAuth django model."""

    class Meta:
        app_label = "social_django"

    def get_social_auth(self, provider, uid):
        try:
            return self.select_related('user').get(provider=provider, uid=uid, user__site_id=settings.SITE_ID)
        except self.model.DoesNotExist:
            return None
