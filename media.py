# import webbrowser module which helps to open webbrowser
import webbrowser

# A new Movies Class is created
class Movies():

    # __init__ constructor for Movies Class is created
    # which is used to create instances
    def __init__(self, movie_title,
                 movie_story_line,
                 poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.story_line = movie_story_line
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    # An instance method for Movies Class is created
    # which helps to open movie trailers using open
    # function in webbrowser module
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
