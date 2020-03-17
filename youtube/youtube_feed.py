import xmltodict


class YoutubeEntry:
    def __init__(self, youtube_entry):
        self.id = youtube_entry['id']
        self.video_id = youtube_entry['yt:videoId']
        self.title = youtube_entry['title']
        self.title_with_80_limit = youtube_entry['title'].split(" | ")[0][:80]
        self.author = youtube_entry['author']['name']
        self.published = youtube_entry['published']
        self.updated = youtube_entry['updated']
        self.media_description = youtube_entry['media:group']['media:description']
        self.details = f'''
            title: {self.title}
            author: {self.author}
            published: {self.published}
            updated: {self.updated}
            description: {self.media_description}
        '''


class YoutubeFeed:
    def __init__(self, youtube_feed_xml):
        self.youtube_feed = xmltodict.parse(youtube_feed_xml)['feed']
        self.channel_id = self.youtube_feed['yt:channelId']
        self.title = self.youtube_feed['title']
        self.author = self.youtube_feed['author']['name']
        self.published = self.youtube_feed['published']
        self.entries = [YoutubeEntry(entry) for entry in self.youtube_feed['entry']]
