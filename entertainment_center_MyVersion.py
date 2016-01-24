import media
import fresh_tomatoes

Deadpool=media.Movie("Deadpool",
	"Ryan Reynolds, The Movie!! ",
	"http://www.joblo.com/newsimages1/deadpool-teaser-poster-small.jpg",
	"https://www.youtube.com/watch?v=ZIM1HydF9UA",
	"A real treat. Fun for all ages")

TheHangover=media.Movie("The Hangover III",
	"3 Friends take a trip to Vegas",
	"https://s-media-cache-ak0.pinimg.com/236x/d0/2b/1f/d02b1f7127f1b46e437b7cc1b4f9510f.jpg",
	"https://www.youtube.com/watch?v=96TelFMZwHc",
	"Just slightly better than the second one")

Revanent=media.Movie("The Revenant",
	"guy loses fight with bear",
	"http://0.media.collegehumor.cvcdn.com/11/95/797d11732f3f61f3d512bdc1004aa6b0.jpg",
	"https://www.youtube.com/watch?v=QRfj1VCg16Y",
	"Seriously, just give the man an oscar")

TheoryOfEverything=media.Movie("The Theory of Everything",
	"Nerd finds wife, loses ability to walk",
	"http://f12-distractify.imgix.net/http%3A%2F%2Fdistractify-media-prod.cdn.bingo%2F1531039-980x.jpg?crop=faces&w=750&ixlib=js-0.2.1&s=96a10933a37738246f56826b3042de6f",
	"https://www.youtube.com/watch?v=Salz7uGp72c",
	"Like a sexy big bang theory")

TheMartian=media.Movie("The Martian",
	"Man becomes lonely, eats potatoes",
	"http://2.media.collegehumor.cvcdn.com/77/99/113e89a298a4676f05860d564b93abf3.jpg",
	"https://www.youtube.com/watch?v=Ue4PCI0NamI",
	"Almost makes NASA cool again")

AmericanSniper=media.Movie("American Sniper",
	"Bradley Cooper deadlifts a ton of weight",
	"http://i.huffpost.com/gen/2497500/thumbs/o-SNIPER-570.jpg?6",
	"https://www.youtube.com/watch?v=NTya9A4O9Ws",
	"America!!")

movies=[Deadpool,TheHangover,Revanent,TheoryOfEverything,TheMartian,AmericanSniper]
fresh_tomatoes.open_movies_page(movies)
#print(toy_story.storyline)
#print(avatar.storyline)
#avatar.show_trailer()
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)