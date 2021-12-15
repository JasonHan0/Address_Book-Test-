from django.shortcuts import render
from .models import Members


def index(request):

    mems = Members.objects.all().order_by('pk')

    return render(
        request,
        'members_app/index.html',
        {
            'mems': mems
        }
    )

def individual_inform(request, pk):
    mem = Members.objects.get(pk=pk)

    return render(
        request,
        'members_app/individual_inform.html',
        {
            'mem' : mem,
        }
    )