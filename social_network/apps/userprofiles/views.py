from django.views.generic import ListView, DetailView, FormView, UpdateView
from django.views.generic.edit import ModelFormMixin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .forms import UserProfileForm, FollowForm, UnfollowForm, UserProfileUserForm
from .models import UserProfile, Rank


class UserProfilePage(UpdateView):
    model = UserProfile
    template_name = 'settings/settings_page.html'
    success_url = '/settings/'
    form_class = UserProfileForm


    def get_object(self, queryset=None):
        if self.request.user.is_authenticated():
            try:
                return UserProfile.objects.get(user=self.request.user)
            except:
                self.request.user.profile.follows.count()


    def form_valid(self, form):
        UserProfileForm = form.save(commit=False)

        if self.request.user.userprofile.rank.id == 1:
            UserProfileForm.background = ''
            UserProfileForm.color = '#000000'
        else:
            "nice"
        self.object = form.save()
        return super(ModelFormMixin, self).form_valid(form)


class UsersProfile(FormView, DetailView):
    model = UserProfile
    form_class = FollowForm
    template_name = 'userprofile/userprofile_detail.html'
    slug_field = 'user__username'
    slug_url_kwarg = 'page_slug'
    context_object_name = 'username'

    def get_success_url(self):
        return reverse('account:page_slugs', kwargs={'page_slug':self.kwargs['page_slug']})

    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated():
            context = super(UsersProfile, self).get_context_data(**kwargs)
            context['following'] = UserProfile.objects.get(user__username=self.kwargs['page_slug']) in self.request.user.profile.follows.all()
            #test = self.request.user.objects.filter(followers__contains=user).count()
            return context


    def form_valid(self, form):
        form.process(self.request, self.kwargs)
        return super(UsersProfile, self).form_valid(form)

    def get_form_class(self):
        if UserProfile.objects.get(user__username=self.kwargs['page_slug']) in self.request.user.profile.follows.all():
            return UnfollowForm
        else:
            return FollowForm