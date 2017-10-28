import webbrowser  # importing webbrowser


class Movie():  # creating class movie

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):

            self.title = movie_title
            self.storyline = movie_storyline
            self.poster_image_url = poster_image
            self.youtube_trailer_url = trailer_youtube

    def show_trailer(self):
        """Call self and open trailer on youtube"""
        webbrowser.open(self.youtube_trailer_url)
