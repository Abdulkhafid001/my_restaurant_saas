from decimal import Decimal
from django.conf import settings
from naija_kitchen.models import MenuItem


class Cart:
    def __init__(self, request) -> None:
        """Initialize the session cart."""

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, menuitem, quantity=1, override_quantity=False):
        """Add a product to the cart or update it's quantity."""
        menuitem_id = str(menuitem.id)
        if menuitem_id not in self.cart:
            self.cart[menuitem_id] = {
                'quantity': 0,
                'price': str(menuitem.price)
            }
        if override_quantity:
            self.cart[menuitem_id]['quantity'] = quantity
        else:
            self.cart[menuitem_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, menuitem):
        """Remove a product from cart"""
        menuitem_id = str(menuitem.id)
        if menuitem_id in self.cart:
            del self.cart[menuitem_id]
            self.save()

    def __iter__(self):
        """Iterate over the items in the cart and get the menuitems from the database."""
        menuitem_ids = self.cart.keys()
        menuitems = MenuItem.objects.filter(id__in=menuitem_ids)
        cart = self.cart.copy()
        for menuitem in menuitems:
            cart[str(menuitem.id)]['menuitem'] = menuitem
            for item in cart.values():
                item['price'] = Decimal(item['price'])
                item['total_price'] = item['price'] * item['quantity']
                yield item

    def __len__(self):
        """count all items in cart."""
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """get cost of cart items"""
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        """remove cart session"""
        del self.session[settings.CART_SESSION_ID]
        self.save()
