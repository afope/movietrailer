import webbrowser  # importing webbrowser


class Movie():
    """This class is a classification or blueprint of all the movies we
    will be using in this program"""

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """This function initialises the class movie. It takes in the
        movie title, the movie storyline, the poster image, and the
        ypoutube trailer"""

            self.title = movie_title
            self.storyline = movie_storyline
            self.poster_image_url = poster_image
            self.youtube_trailer_url = trailer_youtube

    def show_trailer(self):
        """This function calls self and opens trailer on youtube"""
        webbrowser.open(self.youtube_trailer_url)
