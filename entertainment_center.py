import fresh_tomatoes
import media

warrior_daughter = media.Movie("Daughter of a warrior",
                               "Oulaya encapsulates the complexity of femininity: equal parts delicate and strong.",
                               "https://vice-thefifthsense-assets-cdn.vice.com/_600xAUTO_crop_center-center/HW_PARIS025_1600.jpg",
                               "https://www.youtube.com/watch?time_continue=1&v=ubAFcWJAw2o")
    
flesh_blood = media.Movie("The documentary of flesh and blood",
                          "We meet photographer Momo in Tokyo on the day of her wedding, later encountering the city and its inhabitants amongst Shinjuku’s quiet gay scene",
                          "https://vice-thefifthsense-assets-cdn.vice.com/_600xAUTO_crop_center-center/HW_TOKYO033_1600.jpg",
                          "https://www.youtube.com/watch?v=ta56-qYiOMA")

more_woman = media.Movie("There's nothing more woman than making a whole ocean move",
                         "Zariya’s poems are provocative musings on love, lust and longing: little insights into the mind of a young woman on the cusp of adulthood as she continues to figure out her place in the world.",
                         "https://vice-thefifthsense-assets-cdn.vice.com/_1040xAUTO_crop_center-center/HW_CHANEL_LA012_1600.jpg",
                         "https://www.youtube.com/watch?v=81PxGQfZ92A")


five_minutes = media.Movie("Don't be five minutes, be timeless",
                           "Manthe’s is a story of constant movement.",
                           "https://vice-thefifthsense-assets-cdn.vice.com/_800xAUTO_crop_center-center/HW_JBOURGH006_1600.jpg",
                           "https://www.youtube.com/watch?v=Fq9sZtqSMb8")

music_head = ("This is how I see music in my head",
           "Born deaf, Christine creates work that asks viewers to think about sound itself not simply as something we physically hear, but as an idea.",
           "https://vice-thefifthsense-assets-cdn.vice.com/_1040xAUTO_crop_center-center/HW_BERLIN_20_1600.jpg",
           "https://www.youtube.com/watch?time_continue=5&v=BxVZUZpKqVI")

movies = [warrior_daughter, flesh_blood, more_woman, five_minutes, music_head]
fresh_tomatoes.open_movies_page(movies)
