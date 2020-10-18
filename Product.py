class Product:
  def __init__(self, name, price,unit):
    self.name = name
    self.price = price
    self.unit = unit

  def toString(self):
    print(self.name +' '+ self.price + ' ' +self.unit)