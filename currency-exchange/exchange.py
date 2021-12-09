def exchange_money(budget, exchange_rate):
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    money_exchanged=budget/exchange_rate
    return money_exchanged


def get_change(budget, exchanging_value):
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: int - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    money_left=budget-exchanging_value
    return money_left


def get_value_of_bills(denomination, number_of_bills):
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """
    billval=denomination*number_of_bills
    return billval


def get_number_of_bills(budget, denomination):
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """
    billnum=int(budget/denomination)
    return billnum


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    exchangable=int((budget/((exchange_rate*(spread/100))+exchange_rate))/denomination)
    exc=exchangable*denomination
    return exc


def non_exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int non-exchangeable value.
    """
    exchangable=int((budget/((exchange_rate*(spread/100))+exchange_rate))/denomination)
    exc=exchangable*denomination
    notexchangable=int(int(budget/((exchange_rate*(spread/100))+exchange_rate))-exc)
    return notexchangable

print(exchange_money(127.5, 1.2))
print(get_change(127.5, 120))
print(get_value_of_bills(5, 128))
print(get_number_of_bills(127.5, 5))
print(exchangeable_value(127.25, 1.20, 10, 20))
print(non_exchangeable_value(127.25, 1.20, 10, 20))
