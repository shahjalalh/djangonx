from django.views.generic.base import TemplateView


class HomePageView(TemplateView):

    template_name = "home/index.html"


class UserProfileView(TemplateView):

    template_name = "account/profile.html"
