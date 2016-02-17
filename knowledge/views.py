#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from knowledge.models import SecKnowledgeModel
from django.template import RequestContext
from lib.utils import get_context


# Create your views here.
def knowledge_view(request):
    r"""SUMMARY

    knowledge_view(request)

    @Arguments:
    - `request`:

    @Return:

    @Error:
    """
    context = get_context()
    context['knowledges'] = SecKnowledgeModel.objects.filter(publish=True).order_by('sortid')
    return render_to_response(
        'knowledge/index.html',
        context,
        context_instance=RequestContext(request))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# views.py ends here
