import webbrowser


class Movie():

    """Class Movie stores data about a film such as it's title, storyline, a
    link to it's poster and a link to it's trailer."""

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """__init__ takes a films title, storyline, a URL to an image of a the
        movie's poster, and a youtube URL to the film's trailer and stores them
        within the class"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """show_trailer opens a web browser then navigates to the youtube URL
        of a film's trailer."""
        webbrowser.open(self.trailer_youtube_url)
