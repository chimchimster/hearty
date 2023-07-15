from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.views import View
from .signals import create_like_notification

from .models import Profile, Images, Like, Dislike, Notification
from .forms import UploadImageForm, LikeProfileForm, DislikeProfileForm
from django.views.generic import DetailView, CreateView, ListView


class ProfileView(DetailView):
    model = Profile
    template_name = 'profile/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['upload_image'] = UploadImageForm
        context['dislike_profile'] = DislikeProfileForm
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
        context['like_profile'] = LikeProfileForm

        user_notifications = Notification.objects.filter(user=self.request.user, is_read=False)
        context['user_notifications'] = user_notifications

        return context

    def get_queryset(self):

        user_profile = self.request.user.profile
        liked_profiles = user_profile.sent_likes.values_list('receiver__pk', flat=True)
        disliked_profiles = user_profile.sent_dislikes.values_list('receiver__pk', flat=True)

        profiles = Profile.objects.filter(
            Q(gender__in=user_profile.preferences) & ~Q(pk=self.request.user.pk)
            & ~Q(pk__in=liked_profiles) & ~Q(pk__in=disliked_profiles)
        )
        return profiles


class ProfileLikeView(View):
    def post(self, request, *args, **kwargs):

        receiver_pk = request.POST.get('user')
        sender_pk = request.user.pk

        receiver_profile_instance = Profile.objects.get(pk=receiver_pk)
        sender_profile_instance = Profile.objects.get(pk=sender_pk)

        like = Like.objects.create(receiver=receiver_profile_instance, sender=sender_profile_instance)
        like.save()

        create_like_notification(sender=request.user, instance=like, created=True)

        return redirect('profiles:swipes')


class ProfileDislikeView(View):
    def post(self, request, *args, **kwargs):

        receiver_pk = request.POST.get('user')
        sender_pk = request.user.pk

        receiver_profile_instance = Profile.objects.get(pk=receiver_pk)
        sender_profile_instance = Profile.objects.get(pk=sender_pk)

        dislike = Dislike.objects.create(receiver=receiver_profile_instance, sender=sender_profile_instance)
        dislike.save()

        return redirect('profiles:swipes')


class ProfileOwnSympathyView(ListView):
    model = Profile
    template_name = 'sympathy.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)

        user_pk = self.request.user.pk

        likes = Like.objects.filter(sender=user_pk)
        likes_pk = [x.receiver for x in likes]
        profiles_liked = Profile.objects.filter(pk__in=likes_pk)

        context['object_list'] = profiles_liked

        return context


class ProfileOtherSympathyView(ListView):
    model = Profile
    template_name = 'sympathy.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)

        user_pk = self.request.user.pk

        likes = Like.objects.filter(receiver=user_pk)
        likes_pk = [x.sender for x in likes]
        profiles_liked_my_profile = Profile.objects.filter(pk__in=likes_pk)

        context['object_list'] = profiles_liked_my_profile

        return context


def mark_notification_as_read(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id)
    notification.is_read = True
    notification.save()
    return redirect('profiles:swipes')