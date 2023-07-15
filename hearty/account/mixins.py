from django.views.generic import View
from profiles.models import Profile


class CreateProfileMixin(View):
    def create_profile(self, user):

        profile = Profile.objects.create(user=user)

        return profile
