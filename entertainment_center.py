import fresh_tomatoes  # importing fresh_tomatoes.py
import media  # importing media.py


# initialising the list of movies
warrior_daughter = media.Movie(
    "daughter of a warrior",
    ("Oulaya encapsulates the complexity of femininity: equal parts delicate "
        "and strong."),
    "https://vice-thefifthsense-assets-cdn.vice.com/_800xAUTO_crop_center-center/HW_PARIS010_1600.jpg",
    "https://www.youtube.com/watch?time_continue=1&v=ubAFcWJAw2o"
    )

flesh_blood = media.Movie(
    "the documentary of flesh and blood",
    ("We meet photographer Momo in Tokyo on the day of her wedding, later ",
        "encountering the city and its inhabitants ",
        "amongst Shinjuku’s quiet gay scene"),
    "https://vice-thefifthsense-assets-cdn.vice.com/_1040xAUTO_crop_center-center/HW_TOKYO005_1600.jpg",
    "https://www.youtube.com/watch?v=ta56-qYiOMA"
    )

more_woman = media.Movie(
    "i am not your baby girl, i will swallow you whole",
    ("Zariya’s poems are provocative musings on love, lust and longing: ",
        "little insights into the mind of a young woman ",
        "on the cusp of adulthood as she continues to",
        "figure out her place in the world."),
    "https://vice-thefifthsense-assets-cdn.vice.com/_600xAUTO_crop_center-center/HW_CHANEL_LA010_1600.jpg",
    "https://www.youtube.com/watch?v=81PxGQfZ92A"
    )


five_minutes = media.Movie(
    "don't be five minutes, be timeless",
    ("Manthe’s is a story of constant movement."),
    "https://vice-thefifthsense-assets-cdn.vice.com/_800xAUTO_crop_center-center/HW_JBOURGH006_1600.jpg",
    "https://www.youtube.com/watch?v=Fq9sZtqSMb8"
    )

music_head = media.Movie(
    "this is how i see music in my head",
    ("Born deaf, Christine creates work that asks ",
        "viewers to think about sound itself not simply ",
        "as something we physically hear, but as an idea"),
    "https://vice-thefifthsense-assets-cdn.vice.com/_1040xAUTO_crop_center-center/HW_BERLIN_20_1600.jpg",
    "https://www.youtube.com/watch?time_continue=5&v=BxVZUZpKqVI"
    )

making_movements = media.Movie(
    "a mixture between documentary and fantasy",
    ("Meet photographer Harley Weir and the ",
        "other image makers shaping the world ",
        "through a female gaze, presented by ",
        "CHANEL and i-D."),
    "http://fashioncow.com/flowerpower/wp-content/uploads/2017/05/iD-Summer-2017-Adut-Akech-Nyaueth-Riam-by-Harley-Weir-02-1.jpg",
    "https://www.youtube.com/watch?v=AtzQrWQctD8"
    )


#  making the array of movies
movies = [
    music_head, five_minutes, making_movements, more_woman,
    flesh_blood, warrior_daughter
    ]

# calling the open movies page function and passing in movie array
fresh_tomatoes.open_movies_page(movies)
