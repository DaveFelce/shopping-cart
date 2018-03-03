from itertools import count

class Cart:
    new_id = count(1)

    def __init__(self):
        self.items = {}
        self.cart_id = Cart.new_id.__next__()

    def add_item(self, item, num_items):
        if item.name in self.items:
            self.items[item.name]['num_items'] += num_items
        else:
            self.items[item.name] = {'item': item, 'num_items': num_items}

    def get_item(self, item_name):
        return self.items.get(item_name)

    def delete_item(self, item_name):
        return self.items.pop(item_name)

    def get_item_total(self, item_name):
        item = self.get_item(item_name)
        total = item['num_items'] * item['item'].price
        return total
