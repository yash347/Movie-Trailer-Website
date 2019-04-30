import fresh_tomatoes
import media

"""It is a good practice to define a class in another file, and use it or call
it in another file like we defined Movie class in media file and using it in
entertainment_center file"""

fast_and_furious = media.Movie("Fast & Furious 8",
                               "2hrs 29mins",
                               "Dom encounters a mysterious woman, "
                               "Cipher, who gets him involved in the "
                               "world of terrorism. The crew has to "
                               "reunite to stop Cipher and save the "
                               "man who brought them together as a family.",
                               "https://upload.wikimedia.org/wikipedia/en/2/2d/The_Fate_of_The_Furious_Theatrical_Poster.jpg",  # noqa
                               "https://www.youtube.com/watch?v=uisBaTkQAEs",
                               "PG")
avatar = media.Movie("Avatar",
                     "2hrs 42mins",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/sco/b/b0/Avatar-Teaser-Poster.jpg",  # noqa
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     "G")

john_wick = media.Movie("John Wick",
                        "1hr 41mins",
                        "John Wick, a retired hitman grieving the "
                        "loss of his wife, is forced to "
                        "return to his old ways",
                        "https://upload.wikimedia.org/wikipedia/en/9/98/John_Wick_TeaserPoster.jpg",  # noqa
                        "https://www.youtube.com/watch?v=RllJtOw0USI",
                        "PG")

the_perfect_date = media.Movie("The Perfect Date",
                               "1hr 30mins",
                               "A high school student creates an app to offer "
                               "his services as a fake date to make money for "
                               "college. When he develops feelings "
                               "for someone, his plan gets complicated.",
                               "https://upload.wikimedia.org/wikipedia/en/7/7a/The_Perfect_Date.jpg",  # noqa
                               "https://www.youtube.com/watch?v=Hld-7oBn3Rk",
                               "R")

avengers = media.Movie("Avengers: Endgame",
                       "3hrs",
                       "Adrift in space with no food or water, "
                       "Tony Stark sends a message to Pepper "
                       "Potts as his oxygen supply starts to dwindle.",
                       "https://upload.wikimedia.org/wikipedia/en/0/0d/Avengers_Endgame_poster.jpg",  # noqa
                       "https://www.youtube.com/watch?v=TcMBFSGVi1c&t=2s",
                       "G")

spectre = media.Movie("Spectre",
                      "2hrs 40mins",
                      "James Bond receives an obscure message from "
                      "M about a sinister organisation, 'SPECTRE'.",
                      "http://www.impawards.com/2015/posters/spectre.jpg",
                      "https://www.youtube.com/watch?v=7GqClqvlObY",
                      "PG")

movies = [fast_and_furious, avatar, john_wick, the_perfect_date, avengers,
          spectre]
fresh_tomatoes.open_movies_page(movies)
