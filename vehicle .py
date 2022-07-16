class vehical:  #class for vehicle
    vehical='car'

    def __init__(self,type,color,topspeed,milage):

        self.type=type
        self.color=color
        self.topspeed=topspeed
        self.milage=milage
#objects of vehicle class
verna=vehical("Electric","White","200 km/s","15")
thar=vehical("Petrol","Black","250km/s","13")

print("-->Verna  details:\n")
print("Verna is a",verna.vehical)
print("Type:",verna.type)
print("Color:",verna.color)
print("topspeed:",verna.topspeed)
print("milage:",verna.milage)

dist1=int(input("Enter the disance covered to find how much rupee of fuel consumed:"))
quantityoffuel=(dist1/int(verna.milage))
price=quantityoffuel*97
print(f'if verna travels distance {dist1} then price of fuel consumed will be {price}')


print("\n-->Thar details:\n")
print("Thar is a",thar.vehical)
print("Type:",thar.type)
print("Color:",thar.color)
print("topspeed:",thar.topspeed)
print("milage:",thar.milage)

dist2=int(input("Enter the disance covered to find how much rupee of fuel consumed:"))
quantityoffuel=(dist2/int(thar.milage))
price=quantityoffuel*97
print(f'if Thar travels distance {dist2} then price of fuel consumed will be {price}')




