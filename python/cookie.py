class Cookie():
    def __init__(self, shape, size, cookie_type):
        self.shape = shape
        self.size = size
        self.cookie_type = cookie_type
        self.status = 'raw'
    
    def __str__(self):
        return 'My %s cookie' % (self.cookie_type)

    def __lt__(self, other):
        return self.size < other.size
    
    def __gt__(self, other):
        return self.size > other.size

    @property
    def shape(self):
        return self._shape
    
    @shape.setter
    def shape(self, value):
        self._shape = 'Shape of cookie a: ' + value

    def bake(self):
        print('Cookie is baking')
        self.status = 'baked'

class Brownie(Cookie):
    def __init__(self, shape, size, cookie_type, chocochips):
        Cookie.__init__(self, shape, size, cookie_type)
        self.chocochips = chocochips

    def __lt__(self, other):
        return self.chocochips < other.chocochips
    
    def __gt__(self, other):
        return self.chocochips > other.chocochips

    def eat(self):
        print('YUM YUM')
        self.chocochips -= 1

brownie1 = Brownie('round', 20, 'Chololate', 10)
brownie2 = Brownie('round', 15, 'Chololate', 15)
print(brownie1.shape)
brownie1.bake()
brownie1.eat()
print(brownie1.chocochips)

print(brownie1 > brownie2)

# c1 = Cookie('star', '20', 'Chololate')
# c1.eat()

