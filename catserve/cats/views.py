import random
import time
from django.views.generic import TemplateView


class HomeView(TemplateView):

    template_name = "cat.html"

    def get_context_data(self, *args, **kwargs):

        context = super(HomeView, self).get_context_data(*args, **kwargs)

        context['cat_img_src'] = "http://lorempixel.com/{}/{}/cats/".format(
            random.randrange(3,8) * 100, random.randrange(3,8) * 100,
        )
        return context


class CatView(HomeView):

    def get_context_data(self, *args, **kwargs):

        time.sleep(10)

        return super(CatView, self).get_context_data(*args, **kwargs)