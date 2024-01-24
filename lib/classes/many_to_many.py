class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3 and not hasattr(self, 'name'):
            self._name = name
        else:
            raise ValueError("Coffee name must be a string more than 2 characters, and can't be changed after it is initialized.")

    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list({order.customer for order in Order.all if order.coffee == self})
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        orders = self.orders()
        count = len(orders)
        if count == 0:
            return 0
        
        sum = 0
        for order in orders:
            sum += order.price
        return sum / count


class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise ValueError('Customer name must be a string between 1 and 15 characters inclusive.')
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        return list({order.coffee for order in Order.all if order.customer == self})
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        accumulate = {}
        for order in Order.all:
            if order.coffee == coffee:
                accumulate[order.customer] = accumulate.get(order.customer, 0) + order.price
        
        res_customer = None
        res_customer_sum = -1
        for customer in accumulate:
            if accumulate[customer] > res_customer_sum:
                res_customer = customer
                res_customer_sum = accumulate[customer]

        return res_customer
    
class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        type(self).all.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if isinstance(price, int):
            price = float(price)
        if isinstance(price, float) and 1.0 <= price <= 10.0 and not hasattr(self, 'price'):
            self._price = price
        else:
            raise ValueError("Price must be a float between 1.0 an 10.0 inclusive, and can't be changed after it is initialized.")
            
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise ValueError('Customer must be an instance of Customer class')
        
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            raise ValueError('Coffee must be an instance of Coffee class')
    

