altitude = 10000
speed = 250
propulsion = "Propeller"

print(altitude < 1000 and speed > 100)

print((propulsion == "Jet" or propulsion == "Turboprop") and speed < 300 and altitude > 20000)

print(not (speed > 400 and propulsion == "Propeller"))

print((altitude > 500 and speed > 100) or not propulsion == "Propeller")