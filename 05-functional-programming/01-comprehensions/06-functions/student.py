def movie_count(movies,director):
    return len([movie for movie in movies if movie.director == director])

def longest_movie_runtime_with_actor(movies,actor):
    return max([movie.runtime for movie in movies if actor in movie.actors])

def has_director_made_genre(movies,director,genre):
    return any([movie for movie in movies if movie.director == director if genre in movie.genres ])

def is_prime(n): 
    return all(n % x != 0 for x in range(2,n)) and n>=2

def is_increasing(ns):
    return all([ k >= n for  (n,k) in zip(ns,ns[1:])])

def count_matching(xs,ys):
    return sum([x==y for x,y in zip(xs,ys)])

def weighted_sum(ns,weigths):
    return sum([n* weigth for n,weigth in zip(ns,weigths)])

def alternating_caps(string):
    return "".join([char.upper() if index%2 == 0  else char.lower() for index,char in enumerate(string)])

def find_repeated_words(sentence):
    import re
    words = [word.lower() for word in re.findall("[A-Za-z]+",sentence)]
    return {word1 for word1,word2 in zip(words,words[1:]) if word1 == word2}