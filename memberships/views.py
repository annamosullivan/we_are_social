from django.shortcuts import render
from .models import Membership


def all_memberships(request):
    memberships = Membership.objects.all()
    return render(request, "memberships/memberships.html", {"memberships": memberships})
