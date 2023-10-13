import math

def gravity_acceleration(distance):
    earth_mass = 5.976 * 10**24  # kg
    G = 6.674 * 10**(-11)
    grav = G * (earth_mass / (distance**2))  # m/s^2
    return grav

def drag(density, vel, drag_coe, area):
    return 0.5 * density * vel**2 * drag_coe * area

def weight(mass, grav):
    return mass * grav

def density(pressure, temperature_C):
    return pressure / (0.2869 * (temperature_C + 273.15))

def pressure_troposphere(temperature_C):
    return 101.29 * ((temperature_C + 273.15) / 288.08)**5.256

def temperature_troposphere(height):
    return 15.04 - 0.00649 * height

def pressure_low_stratosphere(height):
    return 22.65 * math.exp(1.73 - 0.000157 * height)

def temperature_stratosphere(height):
    return -131.21 + 0.00299 * height

def pressure_stratosphere(height):
    return 2.488 * ((temperature_stratosphere(height) + 273.1) / 216.6)**(-11.388)

def thrust_function(time):
    return  -1000*math.e**(-0.01*(time))

def totalSpeed(speedX, speedY):
    return (speedX**2 + speedY**2)**0.5

def derivative(time):
    dx = 0.000001
    deriv = (thrust_function(time + dx) - thrust_function(time)) / dx
    return deriv

def force_angle(time):
    theta = math.atan(derivative(time))
    return theta

def main():
    # Create files
    with open("Infocambio_cinematico.csv", "w") as fpt, open("Infocambio_dinamico.csv", "w") as fpt2:
        fpt.write("Seconds, instMass, instFuel, Acceleration, Acceleration X, Acceleration Y, Total Speed, Speed X, Speed Y, Height, Delta X, Gravitational Acceleration\n")
        fpt2.write("Seconds, instWeight, Thrust, ThrustX, ThrustY, Air Resistance, density\n")

        # Variables
        thrusts = 34500000 # N
        thrustX = 0
        thrustY = thrusts
        mass = 140000 # kg
        fuel = 2050000 # kg
        fuelrate = 10000.0  # kg per sec
        instMass = mass + fuel
        earthRadius = 6371000  # m
        acceleration = 0  # m/s^2
        speedX = 0
        height = 0  # m
        coorX = 0
        air_density = 0
        drag_coe = 0.47
        cros_sectional_area = 9 * 3.14159
        Drag = 0
        time = 900


        for i in range(0, time + 1):
            # Weight change
            if i != 0:
                thrustX = thrusts * math.cos(force_angle(i))
                thrustY = thrusts * math.sin(force_angle(i))
                instMass = mass - fuel
                fuel = fuel - fuelrate

                if fuel < 1:
                    fuel = 0
                    fuelrate = 0

                instMass = mass + fuel

            if height <= 11000:
                air_density = density(pressure_troposphere(temperature_troposphere(height)), temperature_troposphere(height))
            if 11000 < height <= 25000:
                air_density = density(pressure_low_stratosphere(height), -56.46)
            if height > 25000:
                air_density = density(pressure_stratosphere(height), temperature_stratosphere(height))

            if fuel != 0:
                if i == 0:
                    speedX = 0
                    speedY = 0
                    height = 0
                else:
                    height = height + speedY + acceleration / 2
                    speedY = speedY + accelerationY
                    coorX = coorX + speedX + accelerationX/2
                    speedX = speedX + accelerationX
                Drag = drag(air_density, totalSpeed(speedX, speedY), drag_coe, cros_sectional_area)
                accelerationY = (thrustY - weight(instMass, gravity_acceleration(height + earthRadius)) - Drag*math.sin(force_angle(i))) / instMass
                accelerationX = (thrustX - Drag*math.cos(force_angle(i))) / instMass
            else:
                thrusts = 0
                height = height + speedY + accelerationY / 2
                speedY = speedY + accelerationY
                coorX = coorX + speedX + accelerationX/2
                speedX = speedX + accelerationX
                
                accelerationX = -drag(air_density, speedX, drag_coe, cros_sectional_area)*math.cos(force_angle(i))
                if speedY > 0:
                    accelerationY = (-weight(mass, gravity_acceleration(height + earthRadius)) - drag(air_density, speedY, drag_coe, cros_sectional_area)*math.sin(force_angle(i))) / mass
                if speedY <= 0:
                    accelerationY = (-weight(mass, gravity_acceleration(height + earthRadius)) + drag(air_density, speedY, drag_coe, cros_sectional_area)*math.sin(force_angle(i))) / mass

            if height < 0:
                break
            else:
                fpt.write(f"{i}, {instMass}, {fuel}, {totalSpeed(accelerationX, accelerationY)},{accelerationX}, {accelerationY},{totalSpeed(speedX, speedY)} , {speedX}, {speedY}, {height}, {coorX}, {gravity_acceleration(height + earthRadius)}\n")
                fpt2.write(f"{i}, {weight(instMass, gravity_acceleration(height + earthRadius))}, {thrusts}, {thrustX}, {thrustY}, {Drag}, {air_density}\n")

if __name__ == "__main__":
    main()
