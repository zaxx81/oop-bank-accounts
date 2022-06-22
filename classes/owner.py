import csv
import os.path

class Owner:
  
  def __init__(self, id,name_last,name_first,address_street,address_city,address_state) -> None:
    self.id = int(id)
    self.name_last = name_last
    self.name_first = name_first
    self.address_street = address_street
    self.address_city = address_city
    self.address_state = address_state

  def __str__(self) -> str:
    return f'{self.id} {self.name_last}, {self.name_first}'

  # Class Methods
  def all_owners():
    owners = []
    
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../support/owners.csv")
    with open(path) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            owners.append(Owner(*row))

    return owners
