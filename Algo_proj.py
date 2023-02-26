capacityOfCar = int(input("Enter the mileage capacity of the car: "))
cityList = input("Enter the cities: ").split(" ")
distances = input("Enter the distance between the cities: ").split(" ")
distances = [int(num) for num in distances]

if len(distances) != len(cityList) - 1:
    print("Incorrect Input: The vertices should be equal to nodes - 1")
    exit(0)

currentCapacity = capacityOfCar
stops = []
stops.append(cityList[0])

for i in range(len(distances)):
    if currentCapacity >= distances[i]*2:
        currentCapacity -= distances[i]
    else:
        currentCapacity = capacityOfCar
        currentCapacity -= distances[i]
        stops.append(cityList[i])

stops.append(cityList[-1])
print("Car needs to stop  at following cities: " + str(stops))

