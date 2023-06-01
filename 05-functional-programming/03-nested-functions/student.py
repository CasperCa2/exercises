from util import *


def count_older_than(people, min_age):
    def is_older_than_min_age(people):
        return people.age >= min_age
    return count(people, is_older_than_min_age)


def indices_of_cards_with_suit(cards, suit):
    def equals_to_suit(cards):
        return cards.suit == suit
    return indices_of(cards, equals_to_suit)
