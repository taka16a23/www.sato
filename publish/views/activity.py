#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""activity -- DESCRIPTION

"""
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404

from publish.models import ActivityPostModel, TagModel
from base.utils import get_context


def activity_view(request, postid):
    """SUMMARY

    activity_view(request)

    @Arguments:
    - `request`:

    @Return:

    @Error:
    """
    context = get_context()
    # example "/activity/1"
    context['activity_post'] = get_object_or_404(ActivityPostModel, id=postid)
    tags = TagModel.objects.all()
    context['tags'] = context['activity_post'].tags.all()
    return render_to_response(
        'activity/detail.html',
        context, context_instance=RequestContext(request))


def activity_list_by_tag(request, context, tagname):
    r"""SUMMARY

    activity_list_by_tag(context, tagname)

    @Arguments:
    - `context`:
    - `tagname`:

    @Return:

    @Error:
    """
    context['activities'] = (ActivityPostModel
                             .objects
                             .published()
                             .by_tagname(tagname)
                             .order_by('-publish_date'))
    context['activityTitle'] = tagname + u' 活動一覧'
    context['activeTag'] = tagname
    return render_to_response(
        'activity/index.html',
        context, context_instance=RequestContext(request))


def activity_list_by_year(request, context, year):
    """SUMMARY

    activity_list_by_year(context, year)

    @Arguments:
    - `context`:
    - `year`:

    @Return:

    @Error:
    """
    context['activityTitle'] = str(year) + u'年 活動一覧'
    publishings = (ActivityPostModel
                   .objects
                   .published()
                   .by_year(int(year))
                   .order_by('-publish_date'))
    context['activities'] = publishings
    return render_to_response(
        'activity/index.html',
        context, context_instance=RequestContext(request))


def activity_list_by_year_tag(request, context, year, tag):
    r"""SUMMARY

    activity_list_by_year_tag(context, year, tag)

    @Arguments:
    - `context`:
    - `year`:
    - `tag`:

    @Return:

    @Error:
    """
    context['activityTitle'] = unicode(year) + u'年' + u' ' + tag + u' 活動一覧'
    context['activities'] = (ActivityPostModel
                             .objects
                             .by_tagname(tag)
                             .published()
                             .by_year(int(year))
                             .order_by('-publish_date'))
    context['activeTag'] = tag
    return render_to_response(
        'activity/index.html',
        context, context_instance=RequestContext(request))


def activity_list_default(request, context, ):
    r"""SUMMARY

    activity_list_default(request, context, )

    @Arguments:
    - `request`:
    - `context`:


    @Return:

    @Error:
    """
    year = context['now'].year
    return activity_list_by_year(request, context, year)


def activity_list_view(request):
    r"""SUMMARY

    activity_list_view(request)

    @Arguments:
    - `request`:

    @Return:

    @Error:

    example "/activity?year=2016"
    """
    context = get_context()
    tags = TagModel.objects.all()
    context['tags'] = tags
    tagname = request.GET.get('tag', None)
    year = request.GET.get('year', None)
    if year is not None and not year.isdigit():
        year = None
    if year is not None and not 2000 <= int(year) <= 2030:
        year = None
    if year and tagname:
        return activity_list_by_year_tag(request, context, year, tagname)
    if not (year or tagname):
        return activity_list_default(request, context)
    if year:
        return activity_list_by_year(request, context, year)
    if tagname:
        return activity_list_by_tag(request, context, tagname)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# activity.py ends here
