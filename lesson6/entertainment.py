import movie
import open_movie

toy_story = movie.Movie('Toy Story',
                        'A story of a toy',
                        'http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
                        'https://youtube.com/watch?vwyZH85NQC4')

toy_story2 = movie.Movie('Toy Story 2',
                        'A story of a toy',
                        'http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
                        'https://youtube.com/watch?vwyZH85NQC4')

#toy_story.show_trailer()

#open_movie.open_page([toy_story, toy_story2])
print(toy_story.__doc__)
print(toy_story2.__doc__)
