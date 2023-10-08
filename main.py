import requests as request


class Products():
    def __init__(self):
        pass

    def get_Products(self):
        response = request.get("https://fakestoreapi.com/products")
        return response.json()

    def get_product(self,id):
        for product in self.get_Products():
            if product["id"] == id:
                return product

class Buyers(Products):
    def getProductSold(self):
        products = self.get_Products()
        for product in self.get_Products():
            print(f"Product {product} Sold Successfully.")

    def getListProducts(self,*args,**kwargs):
        list_products = []
        for a in range(1,20):
            list_products.append(self.get_product(a))
        # Using **kwargs to print information about specific products
        for key, value in kwargs.items():
            try:
                print(f"{key}: {list_products[value - 1]}")
            except IndexError:
                print(f"Product {value} not found.")
            finally:
                pass
        # Using *args to print information about all products
        for arg in args:
            try:
                print(f"Product {arg}: {list_products[arg - 1]}")
            except IndexError:
                print(f"Product {arg} not found.")
            finally:
                pass
            




prod  =  Buyers()
# prod.getProductSold()
prod.getListProducts(id=5,title=3,price='15.99')

