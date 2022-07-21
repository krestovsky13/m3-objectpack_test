from django.conf import settings
from django.shortcuts import render


def workspace(request):
    """
    Возвращает view для отображения Рабочего Стола на
    основе шаблона m3
    """
    return render(
        request,
        'm3_workspace.html',
        context={'debug': settings.DEBUG},
    )
