from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse

from .models import Profile, Images
from .forms import UploadImageForm
from django.views.generic import DetailView, CreateView


class ProfileView(DetailView):
    model = Profile
    template_name = 'profile/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['upload_image'] = UploadImageForm
        return context


class UploadImageView(CreateView):
    model = Images
    form_class = UploadImageForm

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            image = form.save(commit=False)
            image.profile = self.request.user.profile
            image.save()
            return redirect('profiles:profile_view', pk=self.request.user.pk)

        return self.form_invalid(form)

