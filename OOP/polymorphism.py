class Product : 
    
    
    def __init__(self,name,price,product_code) -> None:
        self.name = name 
        self.price = price 
        self.product_code = product_code 
    
    
    def explain_product(self): 
        return f'{self.name} - {self.price} - {self.product_code}'
    

# pr = Product('T-Shirt',200,'213913')
# print(pr.explain_product())

class Clothes(Product) : 
    
    def __init__(self, price, product_code,size,brand) -> None:
        super().__init__( price, product_code)
        self.size = size 
        self.brand = brand 
    
    def explain_product(self):
        return f'Colethes Detail is : name : {self.name} brand {self.brand}  size {self.size}'
    
     

class Electronics(Product): 
    def __init__(self, name, price, product_code,standard) -> None:
        super().__init__(name, price, product_code)
        self.standard = standard 
    
    def explain_product(self):
        return f''
    
# class Furniture(Product) : 
#     pass 
