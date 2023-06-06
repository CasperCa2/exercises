from util import *

def count_older_than(people,min_age):
    def older_than(person):
        return person.age >= min_age
    return count(people,older_than)


def indices_of_cards_with_suit(cards,suit):
    def equal_suit(card):
        return card.suit == suit
    
    return indices_of(cards,equal_suit)