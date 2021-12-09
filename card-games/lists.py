def get_rounds(number):
    """

     :param number: int - current round number.
     :return: list - current round and the two that follow.
    """
    nums=[number, number+1, number+2]
    return nums


def concatenate_rounds(rounds_1, rounds_2):
    """

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    nums=rounds_1+rounds_2
    return nums


def list_contains_round(rounds, number):
    """

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """
    for i in rounds:
        if i==number:
            return True
    return False

def card_average(hand):
    """
    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """

    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - is approximate average the same as true average?
    """

    fullav=sum(hand) / len(hand)
    guest1=(hand[0]+hand[len(hand)-1]) / 2
    guest2= hand[int((len(hand) - 1)/2)]
    if fullav in (guest1, guest2):
        return True
    return False

def average_even_is_average_odd(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    odd=hand[0::2]
    even=hand[1::2]
    odda=sum(odd)/len(odd)
    evena=sum(even)/len(even)
    if odda==evena:
        return True
    return False


def maybe_double_last(hand):
    """

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[len(hand)-1]==11:
        hand[len(hand)-1]=22
    return hand
