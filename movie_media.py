import webbrowser

class Media():
    def __init__(self, title, poster_URL, trailer_link):
        self.title = title
        self.poster_image_url = poster_URL
        self.trailer_youtube_url = trailer_link

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
