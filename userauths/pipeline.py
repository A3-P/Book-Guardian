import logging

from allauth.account.utils import perform_login
from django.contrib.auth import get_user_model

logger = logging.getLogger(__name__)


def link_to_existing_user(request, sociallogin):
    User = get_user_model()
    email = sociallogin.account.extra_data.get("email")

    if email:
        try:
            user = User.objects.get(email=email)
            # If a user with the email exists, link the social account to this user
            sociallogin.connect(request, user)
            logger.info(f"Linked social account to existing user: {user}")
            return None
        except User.DoesNotExist:
            logger.info(f"No existing user with email: {email}")
    return None
