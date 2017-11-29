#media.py
import webbrowser

# Using classes , minimize's repetitve codes
class Movie():
	"""This calss provides a way to store move related information"""
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]
	""" WHEN A LIST IS CONSTANT , MAKE THE VARIABLE NAME IN ALL CAPS"""

	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		"""Func contructs an instance of Movie class for each input passed through as strings of the
		movie title, it's storyline, poster_image, and trailer to which the args are assigned to
		corresponding instance variables"""
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		"""Func constructs an instance of Movie class for which self is passed through as input,
		telling the browser to open the trailer to the corresponding YouTube video when the user
		selects from your website, after your site has load properly."""
		webbrowser.open(self.trailer_youtube_url)