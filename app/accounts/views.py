
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from accounts.forms import SignUpForm


class SignUpView(generic.CreateView):

    queryset = get_user_model().objects.all()
    template_name = 'accounts/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('index')


class UserActivateView(generic.RedirectView):
    pattern_name = 'index'

    def get(self, request, *args, **kwargs):
        username = kwargs.pop('username')
        user = get_object_or_404(get_user_model(), username=username)

        if user.is_active:
            pass
        else:
            user.is_active = True
            user.save()

        response = super().get(request, *args, **kwargs)
        return response


class UserProfileView(LoginRequiredMixin, generic.UpdateView):
    queryset = get_user_model().objects.all()
    template_name = 'accounts/my_profile.html'
    success_url = reverse_lazy('index')
    fields = (
        'first_name',
        'last_name',
    )

    # 1
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(id=self.request.user.id)
    #     return queryset

    # 2
    def get_object(self, queryset=None):
        return self.request.user
