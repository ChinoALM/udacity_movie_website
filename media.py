import webbrowser

# Minimize code by using class
class Movie():
	"""This calss provides a way to store move related information"""
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]
	"""When a list is constant , make the VARIABLE NAME IN ALL CAPS"""

	def __init__(self, movie_title, poster_image, trailer_youtube):
		self.title = movie_title
		#self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)