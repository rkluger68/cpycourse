# inherit.py

# Suppose a pretty old-school webshop selling physical products.


# Superclass for all products.
class Product:
    number_of_products = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self._register()

    # Implementation shared by subclasses.
    def _register(self):
        """Increase the product counter and set unique product id.
        """
        # A very naive product count and product id implementation.
        Product.number_of_products += 1
        # Simply use the current count as product instance ID.
        self.product_id = f'Product-{self.number_of_products}'

    def overview(self):
        """Return a short overview text describing the product.
        """
        return f'{self.name}:\n{self.description[:79]}'


# Derived subclasses.
class Book(Product):

    def __init__(self, name, description, author, isbn):
        # Explicitly call base class constructor (initializer).
        super().__init__(name, description)
        self.author = author
        self.isbn = isbn

    # Book overrides superclass methodd.
    def overview(self):
        return f'{self.name} ({self.author}):\n{self.description[:79]}'


class CD(Product):

    def __init__(self, name, description, artist, tracklist):
        # Explicitly call base class constructor (initializer).
        super().__init__(name, description)
        self.artist = artist
        self.tracklist = tracklist

    # CD overrides superclass methodd.
    def overview(self):
        tracks = '\n'.join(
            f'{i+1:2}. {track}' for (i, track) in enumerate(self.tracklist))
        return f'{self.artist}: {self.name}\n{self.description[:79]}\n{tracks}'


if __name__ == '__main__':
    # User our fancy classes to populate our shop's inventory.
    inventory = [
        Book(
            "Advanced Python Wizardry", "All of Python's secrets",
             author="Peter Y. Thonista", isbn="978-3-7657-3278-2"
            ),
        CD(
            "The Very Best of", "Best of 1991-2023", "The Pythonics",
            tracklist=('Python Shuffle', 'Snake Boogie',
                       'Green is the New Black', 'Hisses & Kisses')
            )
        ]

                  
    for item in inventory:
        print(f'\n{item.name} product_id={item.product_id}')
        print(item.overview())

    # Are we ready for the competition?
    print(f'\nCurrently available products in inventory: '
          f'{Product.number_of_products}')
