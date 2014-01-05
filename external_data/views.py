__author__ = 'derya'

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import json
from django.views.generic import TemplateView
from django.http import HttpResponse

DEVELOPER_KEY = "AIzaSyB-oAO1zdcHG8wgT15KhZ1yvfEXIcwnaLA"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search():
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q="google",
        part="id,snippet",
        maxResults=25
    ).execute()
    videos = []
    channels = []
    playlists = []

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                       search_result["id"]["videoId"]))
        elif search_result["id"]["kind"] == "youtube#channel":
            channels.append("%s (%s)" % (search_result["snippet"]["title"],
                                         search_result["id"]["channelId"]))
        elif search_result["id"]["kind"] == "youtube#playlist":
            playlists.append("%s (%s)" % (search_result["snippet"]["title"],
                                          search_result["id"]["playlistId"]))
    print "Videos:\n", "\n".join(videos), "\n"
    print "Channels:\n", "\n".join(channels), "\n"
    print "Playlists:\n", "\n".join(playlists), "\n"

class JSONResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """
    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return HttpResponse(
            self.convert_context_to_json(context),
            content_type='application/json',
            **response_kwargs
        )

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return json.dumps(context)

class YoutubeSearchView(JSONResponseMixin, TemplateView):
    #youtube_search()

    def get_context_data(self, **kwargs):

        # Call the base implementation first to get a context
        context = super(YoutubeSearchView, self).get_context_data(**kwargs)
        # Add in HTML content
        context['Ping'] = "Pong"

        return context

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)



