# ====== Last watched Movie test data ======
'Planet Hulk'
'Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.'


# ====== Import Libraries ======
# Import spacy
import spacy
nlp = spacy.load('en_core_web_md')


# ====== The beginning of the class ======
class Movie:

    def __init__(self, name, description):
        pass
        self.name = name
        self.description = description

    # === Methods ===
    def get_name(self):
        pass
        '''
        return the name for the given Movie
        '''
        return self.name

    def get_description(self):
        pass
        '''
        return the description for the given Movie
        '''
        return self.description


# ====== Functions outside the class ======
def import_movies (file):

    pass
    '''
    The import movies function open the file provided, reads the data and 
    creates a Movie object with each line of data and stores this in the movies list.
    If the file does not exist it will error

    :param file: The file to be processed

    :return: the movies list
    '''
    movies = []

    while True:
        try:
            with open(file, 'r') as file:

                # Process the rest of the lines, creating a shoe object for each one
                for line in file:
                    data = line.split(':')
                    movies.append(Movie(data[0],data[1]))
            break

        # Display an error if the file isn't found
        except FileNotFoundError:
            print ('File Not Found!')
            break

    return movies


def recommend_movie (name,description):
    '''
    The recommend movies function takes the name and description of a movie
    and compares the description with the description of each of the movies 
    in the list of movies the import movie function returned.
    It then determines which movie is the closest match

    :param name: The name of the movie to be compared
    :param description: The description of the movie to be compared

    :return: a string detailing the recommended movie to watch
    '''
    last_watched = Movie(name,description)
    next_movie = ''
    highest_score = 0

    # loop through each movie and get the description
    for movie in import_movies ('movies.txt'):
        token = nlp(movie.get_description())

        # compare each description with the description provided
        for token_ in last_watched.get_description():
                token_ = nlp(token_)

                # if the match is higher then the current highest match
                # updated the recommned movie and match score
                if token.similarity(token_) > highest_score:
                    highest_score = token.similarity(token_)
                    next_movie = movie.get_name()

    return f'If you liked {last_watched.get_name()} then you will enjoy {next_movie}\
 it has a {round((highest_score*100),2)} match'

# ====== Program ======
# Ask the user to enter the name and description of the last fill the watched
last_watched_name = input('Enter the name of the movie you last watched: ')
last_watched_description = [input('Enter the description of the movie you last watched: ')]

# pass this to the recommend_movie and print the result
print(recommend_movie (last_watched_name,last_watched_description))
