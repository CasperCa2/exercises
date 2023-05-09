def titles(movies):
    for n in movies:
        return n.title


def titles_and_years(movies):
    return [n.title and n.year for n in movies]


def titles_and_actor_count(movies):
    return [n.title and n.actors for n in movies]
