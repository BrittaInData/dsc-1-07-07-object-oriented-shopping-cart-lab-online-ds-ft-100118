import numpy as np

class ShoppingCart:
    
    ## initialize a shopping cart with a total (_total) which starts at 0, an empty list of items (_items)
    ## and an optional employee discount (_employee_discount): datatype None
    
    def __init__(self, employee_discount=None):
        self._total = 0
        self._items = []
        self._employee_discount = employee_discount

        
    ## (1) instance methods using properties  
    # ... for total
    def get_total(self):
        return self._total        
    def set_total(self, new_total):
        self._total = new_total
    total = property(get_total, set_total) 
    
    # ... for items
    def get_items(self):
        return self._items        
    def set_items(self, list_of_items):
        self._items = list_of_items
    items = property(get_items, set_items)  
    
    # ... for employee_discount
    def get_employee_discount(self):
        return self._employee_discount        
    def set_employee_discount(self, new_discount):
        self._employee_discount = new_discount
    employee_discount = property(get_employee_discount, set_employee_discount) 
    
    
    ## (2) other instance methods
    def add_item(self, article, price, quantity=1):
        for i in list(range(quantity)):
            self._items.append({"Article" : article, "Price" : price})
            self.total += price
        return self.total
    
    # Preparing method for median and mean: extracting the price(s) for a particular article
    def get_all_prices(self):
        return [x['Price'] for x in self._items]   
    def mean_item_price(self):
        return np.mean(self.get_all_prices()) 
    def median_item_price(self):
        return np.median(self.get_all_prices())
    
    def apply_discount(self):
        if self.employee_discount:
            disc_perc = self.employee_discount / 100
            disc_total = self.total * (1 - disc_perc)
            return disc_total
        else:
            return "Sorry, there is no discount to apply to your cart :("
        
    def item_names(self):
        return [x['Article'] for x in self._items]
    
    def void_last_item(self):
        if self._items:
            last_item = self._items.pop()
        else:
            return "There are no items in your cart!"
        self.total -= last_item['Price']