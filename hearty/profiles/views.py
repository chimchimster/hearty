from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import View

from .models import Profile, Images
from .forms import UploadImageForm
from django.views.generic import DetailView, CreateView, ListView


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


class DeleteImageView(View):
    def post(self, request, *args, **kwargs):
        image_id = request.POST.get('image_id')

        try:
            image = Images.objects.get(id=image_id)
            image.delete()
            return redirect('profiles:profile_view', pk=request.user.pk)
        except Images.DoesNotExist:
            return HttpResponse('Image does not exist.')


class Swipes(ListView):
    model = Profile
    template_name = 'swipes.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)

        return context