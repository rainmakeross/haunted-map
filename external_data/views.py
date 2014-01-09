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
PYTHONIOENCODING= 'utf-8'

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


class YouTubeSearchJSONView(JSONResponseMixin, TemplateView):
    DEVELOPER_KEY = "AIzaSyB-oAO1zdcHG8wgT15KhZ1yvfEXIcwnaLA"
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)

    def youtube_search(self,query,max_results):
        videos = []
        youtube = build(self.YOUTUBE_API_SERVICE_NAME, self.YOUTUBE_API_VERSION,developerKey=self.DEVELOPER_KEY)
        search_response = youtube.search().list(
            q=query,
            part="id,snippet",
            maxResults=max_results
        ).execute()
        # Add each result to the appropriate list, and then display the lists of
        # matching videos, channels, and playlists.
        for idx,search_result in enumerate(search_response.get("items", [])):
            temp_video = [{"videoId":"1"}]
            if search_result["id"]["kind"] == "youtube#video":
                video = {"videoId":str(search_result["id"]["videoId"].encode('utf-8')), "title":str(search_result["snippet"]["title"].encode('utf-8'))}
                videos.append({"video":video})
        return videos

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(YouTubeSearchJSONView, self).get_context_data(**kwargs)

        context['video_list'] = self.youtube_search(self.kwargs['query'],self.kwargs['max_results'])
        context['view'] =''

        return context



