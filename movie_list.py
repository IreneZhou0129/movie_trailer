import fresh_tomatoes
import movie_media

Harry_Potter = movie_media.Media("Harry Potter And The Philosopher's Stone", "http://harrypotterfanzone.com/wp-content/2015/07/philosophers-stone-theatrical-poster.jpg","https://www.youtube.com/watch?v=VyHV0BRtdxo")
LOTR = movie_media.Media("The Lord of the Rings: The Felloship of the Ring", "https://images-na.ssl-images-amazon.com/images/I/51Qvs9i5a%2BL._SL500_AC_SS350_.jpg","https://www.youtube.com/watch?v=V75dMMIW2B4")
Zootopia = movie_media.Media("Zootopia", "https://image.tmdb.org/t/p/original/1YzLAWykXzZhydoGJCqoVQ0gVyC.jpg", "https://www.youtube.com/watch?v=jWM0ct-OLsM")

movies = [Harry_Potter, LOTR, Zootopia]
fresh_tomatoes.open_movies_page(movies)

