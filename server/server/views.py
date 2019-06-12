from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class Home(View):

    template = 'home.html'

    def get(self, request):
        return render(request, self.template)
