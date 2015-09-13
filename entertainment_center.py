import fresh_tomatoes
import media

# Data inputs for class instances of "movie"

brazil = media.Movie(
    "Brazil",
    "A bureaucrat in a retro-future world tries to correct an\
    administrative error and himself becomes an enemy of the\
    state.",
    "http://assets.flicks.co.nz/images/movies/poster/89/8973ba741e7bd6450d8023552f43728e_500x735.jpg",  # noqa
    "https://www.youtube.com/watch?v=EvBF3Lxla98")


nightmare_before_christmas = media.Movie(
    "The Nightmare Before Christmas",
    "Jack Skellington, king of Halloween Town,\
    discovers Christmas Town, but doesn't quite\
    understand the concept.",
    "http://ecx.images-amazon.com/images/I/51frysl%2BZzL._SX940_.jpg",  # noqa
    "https://www.youtube.com/watch?v=wr6N_hZyBCk")

bernie = media.Movie(
    "Bernie",
    "In small-town Texas, an affable mortician strikes up a\
    friendship with a wealthy widow, though when she starts to\
    become controlling, he goes to great lengths to separate\
    himself from her grasp.",
    "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTj_-UpQ3isf6NjY3RBlkp-wJOF4fDs75Rd0gu-9mUv8I8RWdwcvg",  # noqa
    "https://www.youtube.com/watch?v=YJuhWKcY_6U")

paranorman = media.Movie(
    "Paranorman",
    "A misunderstood boy takes on ghosts, zombies and\
    grown-ups to save his town from a centuries-old curse.",
    "http://www.iceposter.com/thumbs/MOV_81d2f3d4_b.jpg",
    "https://www.youtube.com/watch?v=QJaIeGrg6YY")

coraline = media.Movie(
    "Coraline",
    "An adventurous girl finds another world that is a\
    strangely idealized version of her frustrating home,\
    but it has sinister secrets.",
    "https://s-media-cache-ak0.pinimg.com/236x/e6/de/1d/e6de1d31cdfb9a82932b1a82a1c1ed0f.jpg",  # noqa
    "https://www.youtube.com/watch?v=LO3n67BQvh0")

brick = media.Movie(
    "Brick",
    "A teenage loner pushes his way into the underworld of a\
    high school crime ring to investigate the disappearance of\
    his ex-girlfriend.",
    "https://weekdaymatinee.files.wordpress.com/2011/06/brick_movie_poster_painted_by_jam_bad.jpg",  # noqa
    "https://www.youtube.com/watch?v=4Zfw8__A7ps")

corpsebride = media.Movie(
    "Corpsebride",
    "When a shy groom practices his wedding vows in the\
    inadvertent presence of a deceased young woman, she rises\
    from the grave assuming he has married her.",
    "http://www.impawards.com/2005/posters/corpse_bride.jpg",
    "https://www.youtube.com/watch?v=G9boDkpEyvc")

boxtrolls = media.Movie(
    "Boxtrolls",
    "A young orphaned boy raised by underground cave-dwelling\
    trash collectors tries to save his friends from an evil\
    exterminator.",
    "https://s-media-cache-ak0.pinimg.com/736x/a5/04/43/a5044340e12073a122862085ea565c68.jpg",  # noqa
    "https://www.youtube.com/watch?v=Q2dFVnp5K0o")

# Build a list of movies
movies = [brazil, nightmare_before_christmas, bernie, paranorman, coraline,
          brick, corpsebride, boxtrolls]
fresh_tomatoes.open_movies_page(movies)
