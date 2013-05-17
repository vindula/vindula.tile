# coding: utf-8
from five import grok
from vindula.tile.browser.baseview import BaseView

from vindula.tile.content.interfaces import ITilePoll

from Products.CMFCore.utils import getToolByName
from Acquisition import aq_inner

grok.templatedir('templates')


class PollView(BaseView):
    grok.context(ITilePoll)
    grok.name('poll-view')


    def portal_url(self):
        utool = getToolByName(self.context, 'portal_url')
        return utool()

    def has_polls(self):
        return len(self.polls) > 0

    def has_more_polls(self):
        return len(self.polls) > 1

    def polls(self):
        # Note that we can't cache poll data since some of them are user dependant
        context = aq_inner(self.context)
        portal_catalog = getToolByName(context, 'portal_catalog')
        plone_tool = getToolByName(context, 'plone_utils')
        # I "love" the Plone 3 way to get the folderishness of a content :/
        #globals_view = getMultiAdapter((self.context, self.request), name='plone')
        #isStructuralFolder = globals_view.isStructuralFolder
        selection_mode = context.getSelection_mode()
        number_of_polls = context.getNumber_of_polls()

        if selection_mode == 'hidden':
            results = []
        elif selection_mode == 'newest':
            results = portal_catalog.searchResults(
                meta_type='PlonePopoll',
                isEnabled=True,
                sort_on='Date',
                sort_order='reverse',
                sort_limit=number_of_polls)[:number_of_polls]

        elif selection_mode in ('branch', 'subbranches'):
            folder = context
            if not plone_tool.isStructuralFolder(context):
                folder = context.getParentNode()
            depth = (selection_mode == 'branch') and 1 or 1000
            results = portal_catalog.searchResults(
                meta_type='PlonePopoll',
                path={'query': '/'.join(folder.getPhysicalPath()),'depth': depth},
                isEnabled=True,
                sort_on='Date',
                sort_order='reverse',
                sort_limit=number_of_polls)[:number_of_polls]

        else:
            # A specific poll
            results = portal_catalog.searchResults(
                meta_type='PlonePopoll',
                UID=selection_mode)
        if results:
            return [pollFeatures(r.getObject()) for r in results]
        return []

def pollFeatures(poll):
    """Poll features for portlet layout"""

    poll_url = poll.absolute_url()
    choices_count = poll.getNumber_of_choices()
    rval = {
        'url': poll_url,
        'choices_count': choices_count,
        'can_vote': poll.canVote(),
        'title': poll.Title(),
        'question': poll.getQuestion(),
        'form_action': '%s/vote' % poll_url,
        'form_name': 'results-%s' % poll.getId(),
        'results': poll.getResults(),
        'input_widget': choices_count > 1 and 'checkbox' or 'radio',
        'show_results': poll.isVisible() and poll.getShowCurrentResults(),
        'is_visible' : poll.isVisible(),
        'votes_count': poll.getVotesCount(),
        'UID': poll.UID
        }
    # TODO: on reprend au dessus
    return rval

