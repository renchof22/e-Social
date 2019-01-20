from django.views.generic import CreateView, UpdateView
from django.http import HttpResponse
from .models import Player, Clan
from .forms import PlayerForm, ClanForm, PlayerUpdateForm
from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.signing import BadSignature, SignatureExpired, loads, dumps
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, resolve_url
from django.template.loader import get_template


class PlayerCreateView(CreateView):
    model = Player
    form_class = PlayerForm
    template_name = "app1/setting.html"
    success_url = "/user"  # 成功時にリダイレクトするURL


class ClanCreateView(CreateView):
    model = Clan
    form_class = ClanForm
    template_name = "app1/clan_create.html"
    success_url = "/user"  # 成功時にリダイレクトするURL


class MyPage(generic.TemplateView):
    """マイページ"""
    template_name = 'app1/mypage.html'


User = get_user_model()


class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        # 今ログインしてるユーザーのpkと、そのユーザー情報ページのpkが同じか、又はスーパーユーザーなら許可
        # user = self.request.user
        # return user.pk == self.kwargs['pk'] or user.is_superuser
        return True


class UserDetail(OnlyYouMixin, generic.DetailView):
    model = User
    template_name = 'app1/user_detail.html'


class UserUpdate(OnlyYouMixin, generic.UpdateView):
    model = User
    form_class = PlayerUpdateForm
    template_name = 'app1/user_form.html'

    def get_success_url(self):
        return resolve_url('app1:user_detail', pk=self.kwargs['pk'])


def index(request):
    str_out = "*** app2 ***<p />"
    str_out += "こんにちは<p />"
    str_out += "ここがホームだとして"
    return HttpResponse(str_out)
