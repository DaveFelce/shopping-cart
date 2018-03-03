import unittest
from cart import Cart
from item import Item
from user import User

class CartTests(unittest.TestCase):
    def test_cart_number(self):
        cart1 = Cart()
        cart2 = Cart()
        cart3 = Cart()
        self.assertEqual(cart1.cart_id, 1)
        self.assertEqual(cart2.cart_id, 2)
        self.assertEqual(cart3.cart_id, 3)

    def test_items(self):
        item_shorts = Item(name='shorts', price=20, description='Some nice shorts')
        cart4 = Cart()
        self.assertEqual(cart4.cart_id, 4)
        cart4.add_item(item_shorts, 2)
        shorts = cart4.get_item('shorts')
        self.assertEqual(shorts['num_items'], 2)
        self.assertEqual(shorts['item'].description, 'Some nice shorts')
        cart4.add_item(item_shorts, 3)
        self.assertEqual(shorts['num_items'], 5)

        total_price_shorts = cart4.get_item_total('shorts')
        self.assertEqual(total_price_shorts, 100)

    def test_user(self):
        item_shorts = Item(name='shorts', price=20, description='Some nice shorts')
        item_tshirt = Item(name='tshirt', price=15, description='A nice t-shirt')
        item_vest = Item(name='vest', price=15, description='A nice vest')

        user = User('Mike')
        self.assertIsInstance(user, User)

        cart5 = Cart()
        cart5.add_item(item_shorts, 2)
        cart5.add_item(item_tshirt, 3)
        cart5.add_item(item_vest, 1)
        user.add_cart(cart5)
        retrieved_cart5 = user.get_cart_by_id(cart_id=cart5.cart_id)
        self.assertIsInstance(retrieved_cart5, Cart)
        shorts = retrieved_cart5.get_item('shorts')
        self.assertEqual(shorts['num_items'], 2)

        cart6 = Cart()
        cart6.add_item(item_shorts, 1)
        cart6.add_item(item_tshirt, 2)
        cart6.add_item(item_vest, 3)
        user.add_cart(cart6)
        retrieved_cart6 = user.get_cart_by_id(cart_id=cart6.cart_id)
        self.assertIsInstance(retrieved_cart6, Cart)
        vest = retrieved_cart6.get_item('vest')
        self.assertEqual(vest['num_items'], 3)

        cart5_vest = retrieved_cart5.get_item('vest')
        self.assertEqual(cart5_vest['num_items'], 1)

        self.assertFalse(retrieved_cart5.get_item('pants'))

if __name__ == '__main__':
    unittest.main()


