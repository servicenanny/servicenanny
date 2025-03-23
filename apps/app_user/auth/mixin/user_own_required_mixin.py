from django.contrib.auth.mixins import AccessMixin
from django.http import HttpRequest


class UserOwnRequiredMixin(AccessMixin):
    """Verify that the current nanny is subscriber."""
    def dispatch(self, request: HttpRequest, *args, **kwargs):
        user_id = kwargs.get('user_id')
        if request.user.id == user_id:
            return super().dispatch(request, *args, **kwargs)
        return self.handle_no_permission()
