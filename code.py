# --------------
from csv import reader

# Read the data file and store it as a list 'movies'
opened_file = open(path, encoding="utf8")
read_file = reader(opened_file)
movies = list(read_file)
# The first row is header. Extract and store it in 'movies_header'.
movies_header=movies[0]

# Subset the movies dataset such that the header is removed from the list and store it back in movies
movies=movies[1:]

def explore_data(dataset, start, end, rows_and_columns=False):
    data=dataset[start:end]
    for row in data:
        print(row)
        print('\n')
explore_data(movies,4553,4553)

# Delete wrong data
del movies[4553]

explore_data(movies,0,5)

#identifying duplicate movies
def duplicate_and_unique_movies(dataset, index_):
    unique_movie=[]
    duplicate_movie=[]
    for movie in dataset:
        name=movie[index_]
        if name in unique_movie:
            duplicate_movie.append(name)
        else:
            unique_movie.append(name)
    print("No of duplicate movies:",len(duplicate_movie))
    print('\n')
    print("Examples of duplicate movies",duplicate_movie[:5])
duplicate_and_unique_movies(movies,-2)

# Create a dictionary, 'reviews_max' that will have the name of the movie as key, and the maximum number of reviews as values.

reviews_max={}
for movie in movies:
     name=movie[-2]
     reviews=movie[-3]
     if name in reviews_max and reviews_max[name]<reviews:
         reviews_max[name]=reviews
     elif name not in reviews_max:
         reviews_max[name]=reviews
print(len(movies))
print(len(reviews_max))

# Create a list 'movies_clean', which will filter out the duplicate movies and contain the rows with maximum number of reviews for duplicate movies, as stored in 'review_max'. 
movies_clean=[]
movies_name=[]
for data in movies:
    name=data[-2]
    reviews=data[-3]
    if reviews_max[name]==reviews and name not in movies_name  :
        movies_clean.append(data)
        movies_name.append(name)
print(len(movies_clean))
print(len(movies_name))

# Creating movies_lang(), extract all the english movies and store it in movies_en.

def movies_lang(dataset, index_, lang_):
    movies_=[]
    for movie in movies:
        lang=movie[index_]
        if lang==lang_:
            movies_.append(movie)
    print(len(movies_))
    return movies_
    
movies_en=movies_lang(movies_clean,3,"en")       
 
 #Create the rate_bucket function to see the movies with rating higher than 8.
def rate_bucket(dataset, rate_low, rate_high):
    high_rated_movies=[]
    for movie in dataset:
        rating=float(movie[-4])
        if ((rating>=rate_low)and (rating<=rate_high)):
            high_rated_movies.append(movie)
    print(len(high_rated_movies))
    return high_rated_movies
high_rated_movies=rate_bucket(movies_en,8,10)





