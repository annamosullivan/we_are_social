from django.shortcuts import render
from .models import Membership


def all_memberships(request):
    membership = Membership.objects.all()
    return render(request, "membership/membership.html", {"membership": membership})
