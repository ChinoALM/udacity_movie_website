#entertainment_center.py
import fresh_tomatoes
import media

avatar = media.Movie("Avatar",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

batman_begins = media.Movie("Batman Begins",
                        "https://upload.wikimedia.org/wikipedia/en/a/af/Batman_Begins_Poster.jpg",
                        "https://www.youtube.com/watch?v=vak9ZLfhGnQ")

jurassic_park = media.Movie("Jurassic Park",
                "https://upload.wikimedia.org/wikipedia/en/e/e7/Jurassic_Park_poster.jpg",
                "https://www.youtube.com/watch?v=lc0UehYemQA")

blow = media.Movie("Blow",
                "https://upload.wikimedia.org/wikipedia/en/b/bf/Blow_poster.jpg",
                "https://www.youtube.com/watch?v=q8lGHQn_n9Y")

edward_scissorhands = media.Movie("Edward Scissorhands",
                     "https://upload.wikimedia.org/wikipedia/en/3/3b/Edwardscissorhandsposter.JPG",
                     "https://www.youtube.com/watch?v=M94yyfWy-KI")

toy_story = media.Movie("Toy Story",
                    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

the_sand_lot = media.Movie("The Sandlot",
                     "https://upload.wikimedia.org/wikipedia/en/d/d4/Sandlot_poster.jpg",
                     "https://www.youtube.com/watch?v=-QDq-e1GbjE")

the_saint = media.Movie("The Saint",
                     "https://upload.wikimedia.org/wikipedia/en/8/86/The_Saint_1997_poster.jpg",
                     "https://www.youtube.com/watch?v=QWIIu9SWYC0")

top_gun = media.Movie("Top Gun",
                     "https://upload.wikimedia.org/wikipedia/en/4/46/Top_Gun_Movie.jpg",
                     "https://www.youtube.com/watch?v=ioWpe3hdFH0")

movies = [avatar, batman_begins, jurassic_park, blow, edward_scissorhands, toy_story,
          the_sand_lot, the_saint, top_gun]

#opens website
fresh_tomatoes.open_movies_page(movies)