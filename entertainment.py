#import fresh_tomatoes module which contains HTML code
#import media.py module which contains Movies Class definition
import fresh_tomatoes
import media

# A new instance for Movies Class is created. Here the instance created is inception
inception = media.Movies("Inception","A thief, who steals corporate \
                        secrets through use of dream-sharing technology, \
                        is given the inverse task of planting an idea \
                        into the mind of a CEO.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=1g4PLj0PlOM")

# A new instance for Movies Class is created. Here the instance created is forrest_gump
forrest_gump = media.Movies("Forrest Gump","Forrest Gump, while not \
                           intelligent, has accidentally been present \
                           at many historic moments, but his true love, \
                           Jenny Curran, eludes him.",
                           "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
                           "https://www.youtube.com/watch?v=bLvqoHBptjg")

# A new instance for Movies Class is created. Here the instance created is titanic
titanic = media.Movies("Titanic","A seventeen-year-old aristocrat \
                     falls in love with a kind but poor artist aboard \
                     the luxurious, ill-fated R.M.S. Titanic.",
                      "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSRYd4WJ-4rOQroQPu0sSb3eHLz9aBHwJiZrsraU3E0PZ7sYShfGg",
                      "https://www.youtube.com/watch?v=2e-eXJ6HgkQ")

# A new instance for Movies Class is created. Here the instance created is avengers
avengers = media.Movies("Avengers","Earth's mightiest heroes must \
                       come together and learn to fight as a team if \
                       they are to stop the mischievous Loki and his \
                       alien army from enslaving humanity.",
                       "http://vignette2.wikia.nocookie.net/marvelmovies/images/3/37/Avengers_live_banner.jpg/revision/latest?cb=20120131230337",
                       "https://www.youtube.com/watch?v=NkoKBJ7rgEs")

# A new instance for Movies Class is created. Here the instance created is interstellar
interstellar = media.Movies("Interstellar", "A team of explorers travel \
                           through a wormhole in space in an attempt to \
                           ensure humanity's survival.",
                           "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRTH2sIixvEExrShGuee-JYlEmiFeYNz4niTX-WSWIkcDHSOI6Qvw ",
                           "https://www.youtube.com/watch?v=-gieJQejbHQ")

# A new instance for Movies Class is created. Here the instance created is gladiator
gladiator = media.Movies("Gladiator", "When a Roman general is betrayed \
                        and his family murdered by an emperor's corrupt son, \
                        he comes to Rome as a gladiator to seek revenge.",
                        "http://analogaddiction.files.wordpress.com/2013/08/gladiator-maximus-vs-tigris-of-gaul-04.jpg",
                        "https://www.youtube.com/watch?v=ol67qo3WhJk")

# Create a new list which holds all instances for Movie Class 
movie_list = [inception, forrest_gump, titanic, avengers, interstellar, gladiator]

# Give movie_list as argument to open_movies_page function in fresh_tomatoes.py module.
fresh_tomatoes.open_movies_page(movie_list)
