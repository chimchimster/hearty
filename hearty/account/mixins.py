from django.views.generic import View
from profiles.models import Profile, Notification


class CreateProfileMixin(View):
    def create_profile(self, user):

        profile = Profile.objects.create(user=user)

        return profile


class NotificationMixin:

    def add_notification(self, context):
        user_notifications = Notification.objects.filter(user=self.request.user, is_read=False)
        context['user_notifications'] = user_notifications

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.add_notification(context)
        return context