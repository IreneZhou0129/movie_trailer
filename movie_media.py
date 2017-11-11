import webbrowser

class Media():
    ''' This class provide a constructor and a function. '''

    def __init__(self, title, poster_URL, trailer_link):
        '''The constructor provides three parameters:
            title, which is a string
            poster and trailer, which are URL links '''
        self.title = title
        self.poster_image_url = poster_URL
        self.trailer_youtube_url = trailer_link

    def show_trailer(self):
        '''This function use import class to open the trailer.  '''
        webbrowser.open(self.trailer_youtube_url)
