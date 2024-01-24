#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Customer
from classes.many_to_many import Order
from classes.many_to_many import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")

    coffee = Coffee("Vanilla Latte")
    steve = Customer("Steve")
    dima = Customer("Dima")
    order1 = Order(steve, coffee, 2.0)
    order2 = Order(steve, coffee, 4)
    order3 = Order(dima, coffee, 5.0)
    order4 = Order(dima, coffee, 2.0)
    # who = Customer.most_aficionado(coffee)

    # accumulate = {}
    # for order in Order.all:
    #     if order.coffee == coffee:
    #         print('order: ', order)
    #         print('price: ', order.price)

    ipdb.set_trace()
