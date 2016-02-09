# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.db.models import Q
from django.template import RequestContext

from board.models import Board

import datetime

# Create your views here.
def board(request):
    r"""SUMMARY

    board(request)

    @Arguments:
    - `request`:

    @Return:

    @Error:
    """
    context = {}
    now = datetime.datetime.now()
    year = request.GET.get('year')
    try:
        year = int(year)
    except (ValueError, TypeError) as err:
        print(err)
        year = now.year
    context['year'] = year
    if year == now.year:
        # 今年で公開期間内かつ公開設定されているもの
        context['board_list'] = Board.objects.filter(
            Q(expires_on__isnull=True)|Q(expires_on__gte=now),
            Q(published_from__isnull=True)|Q(published_from__lte=now),
            Q(status=True)).order_by('-published_from')
    else:
        # 過去の年で有効期限がなく公開設定されているもの
        context['board_list'] = Board.objects.filter(
            Q(expires_on__isnull=True),
            Q(published_from__isnull=True)|Q(published_from__year=year),
            Q(status=True)).order_by('-published_from')
    return render_to_response(
        'board/index.html', context, context_instance=RequestContext(request))
