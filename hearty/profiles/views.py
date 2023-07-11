from .models import Profile
from django.views.generic import DetailView


class ProfileView(DetailView):
    model = Profile
    template_name = 'profile/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context