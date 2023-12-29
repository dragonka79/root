# A cars változó értéke 100 legyen
cars = 100
# a space_in_a_car változó értéke 4 mint float
space_in_a_car = 4
#a drives változó értéke 30
drivers = 30
# a passengers változó értéke 90
passengers = 90
# a cars_not_driven változó értéke egyenlő a kocsik számának és a
#vezetők számának különbsége
cars_not_driven =cars - drivers
# a cars_driven változó legyen egyenlő a drivers változóval
cars_driven = drivers
#carpool_capacity változó egyenlő a cars_driven és a space_in_a_car
#változó szorzatával
carpool_capacity = cars_driven * space_in_a_car
#average_passengers_per_car változó egyenlő a passengers törve a
#cars_driven változóval
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
print("We need to put about", int(average_passengers_per_car), "in each car.")

print(cars - passengers)
print(cars < passengers/space_in_a_car)
print(cars*space_in_a_car/drivers*passengers)
print((cars*space_in_a_car)/(drivers*passengers))
