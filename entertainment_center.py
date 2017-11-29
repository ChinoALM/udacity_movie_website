#entertainment_center.py
import fresh_tomatoes
import media

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

batman_begins = media.Movie("Batman Begins",
                    "Can Batman save Gotham from the Scarecrow that lurks in the shadows?",
                    "https://upload.wikimedia.org/wikipedia/en/a/af/Batman_Begins_Poster.jpg",
                    "https://www.youtube.com/watch?v=vak9ZLfhGnQ")

jurassic_park = media.Movie("Jurassic Park",
                    "The most phenomenal discovery of our time becomes the greatest adventure of all time!",
                    "https://upload.wikimedia.org/wikipedia/en/e/e7/Jurassic_Park_poster.jpg",
                    "https://www.youtube.com/watch?v=lc0UehYemQA")

blow = media.Movie("Blow",
                    "A tale of how the cocaine market was born the United States during the 1970s.",
                    "https://upload.wikimedia.org/wikipedia/en/b/bf/Blow_poster.jpg",
                    "https://www.youtube.com/watch?v=q8lGHQn_n9Y")

edward_scissorhands = media.Movie("Edward Scissorhands",
                    "The most incredible tale of the most unusual creature!",
                    "https://upload.wikimedia.org/wikipedia/en/3/3b/Edwardscissorhandsposter.JPG",
                    "https://www.youtube.com/watch?v=M94yyfWy-KI")

toy_story = media.Movie("Toy Story",
                    "A story about a boy and his toys that magically come alive!",
                    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

the_sand_lot = media.Movie("The Sandlot",
                    "The neighborhood kids battle the Beast!",
                    "https://upload.wikimedia.org/wikipedia/en/d/d4/Sandlot_poster.jpg",
                    "https://www.youtube.com/watch?v=-QDq-e1GbjE")

the_saint = media.Movie("The Saint",
                    "A man with no face can not be indentified.",
                    "https://upload.wikimedia.org/wikipedia/en/8/86/The_Saint_1997_poster.jpg",
                    "https://www.youtube.com/watch?v=QWIIu9SWYC0")

top_gun = media.Movie("Top Gun",
                    "Elite United States Navy pilots compete to be the best!",
                    "https://upload.wikimedia.org/wikipedia/en/4/46/Top_Gun_Movie.jpg",
                    "https://www.youtube.com/watch?v=ioWpe3hdFH0")

movies = [avatar, batman_begins, jurassic_park, blow, edward_scissorhands, toy_story,
          the_sand_lot, the_saint, top_gun]

#opens website
fresh_tomatoes.open_movies_page(movies)