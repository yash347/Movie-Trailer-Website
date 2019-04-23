import webbrowser

class Video():#it is not necessary class name should start with capital letter
    #but as we follow google style guide for python, so we write in that way
    
    """ this parent class provides a way to store information related to video"""    

    def __init__(self,title,duration):
        self.title = title
        self.duration = duration
        
class Movie(Video): #here class Movie inherited from parent class Video in order
#to initialize variables inherited from parent class using Video __init__()method
    
    """This child class provides a way to store movies related information"""
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    """ Symbols meaning:
                        G : General Audiences
                        PG : Parental Guidance Suggested
                        PG-13 : Parental Strongly cautioned
                        R : Restricted"""
             
    
    """VALID_RATINGS is manually created class variable and as it is constant,
       that's why it is in capital letters according to google python notation"""
    
    """This __init__() is also called a constructor as it creates a free space in
        memory for a instance and a keyword self points to instance we are creating"""
    
    def __init__(self, title, duration, movie_storyline, poster_image,
                 trailer_youtube, user_rating):
        Video.__init__(self,title,duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = user_rating
        
    """__init__() and show_trailer() are instance methods and their first argument
      must be self"""
   
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
