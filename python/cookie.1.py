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

    def bake(self):
        print('Cookie is baking')
        self.status = 'baked'
        
    @property
    def shape(self):
        return self._shape
    
    @shape.setter
    def shape(self, value):
        self._shape = 'Shape of cookie a: ' + value

    


cookie1 = Cookie('star',20,'choco')
cookie2 = Cookie('rexta',10,'butrt')
print(cookie1.shape)
print(cookie2.shape)

cookie1.bake()
print(cookie1.size)