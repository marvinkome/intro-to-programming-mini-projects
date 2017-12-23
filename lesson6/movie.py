import webbrowser


class Movie():

    ''' This is the movie class to store movie information'''

    def __init__(self, title, story_line, poster_image, trailer_link):
        self.title = title
        self.story_line = story_line
        self.poster_image = poster_image
        self.trailer_link = trailer_link

    def show_trailer(self):
        webbrowser.open(self.trailer_link)

