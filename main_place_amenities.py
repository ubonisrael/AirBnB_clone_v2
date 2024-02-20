#!/usr/bin/python3
""" Test link Many-To-Many Place <> Amenity
"""
from models import storage
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity

# creation of a State
state = State()
state.name = "Massachussets"
state.save()

# creation of a City
city = City()
city.state_id=state.id
city.name="Boston"
city.save()

# creation of a User
user = User()
user.email="eli@snow.com"
user.password="elipwd"
user.save()

# creation of 2 Places
place_1 = Place()
place_1.user_id=user.id
place_1.city_id=city.id
place_1.name="House 5"
place_1.save()

place_2 = Place()
place_2.user_id=user.id
place_2.city_id=city.id
place_2.name="House 6"
place_2.save()

# creation of 3 various Amenity
amenity_1 = Amenity()
amenity_1.name="TV"
amenity_1.save()
amenity_2 = Amenity()
amenity_2.name="Fridge"
amenity_2.save()
amenity_3 = Amenity()
amenity_3.name="Swimming Pool"
amenity_3.save()

# link place_1 with 2 amenities
place_1.amenities.append(amenity_1)
place_1.amenities.append(amenity_2)

# link place_2 with 3 amenities
place_2.amenities.append(amenity_1)
place_2.amenities.append(amenity_2)
place_2.amenities.append(amenity_3)

print("==========")
print(place_2.amenities)
print("==========")

storage.save()

print("OK")
