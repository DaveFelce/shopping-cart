from cart import Cart
from item import Item
from user import User

def main():

    item_shorts = Item(name='shorts', price=10, description='Some nice shorts')
    item_tshirt = Item(name='tshirt', price=20, description='A nice t-shirt')
    item_pants = Item(name='pants', price=30, description='Lovely pants')

    # create user
    user = User('Eric')
    # create a new cart
    cart = Cart()
    user.add_cart(cart)

    # Eric does some shopping
    cart.add_item(item_shorts, 4)
    cart.add_item(item_tshirt, 2)
    cart.add_item(item_pants, 3)

    # we want to display his cart
    retrieved_cart = user.get_cart_by_id(cart_id=cart.cart_id)
    print(retrieved_cart)

    pants = retrieved_cart.get_item('pants')
    print(pants)

    cart2 = Cart()
    cart2.add_item(item_shorts, 1)
    cart2.add_item(item_tshirt, 2)
    cart2.add_item(item_pants, 3)
    user.add_cart(cart2)

    retrieved_cart2 = user.get_cart_by_id(cart_id=2)

    tshirt = retrieved_cart2.get_item('tshirt')
    print(tshirt)

    tshirt_total = cart2.get_item_total('tshirt')
    print(tshirt_total)

if __name__ == '__main__':
    main()
