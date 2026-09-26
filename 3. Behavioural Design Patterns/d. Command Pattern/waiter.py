from order import Order

class Waiter:
    def take_order(self,order:Order):
        order.execute()