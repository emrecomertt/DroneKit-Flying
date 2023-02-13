from dronekit import connect,VehicleMode,LocationGlobalRelative
import time

# Drone bağlantısı 
vehicle=connect("127.0.0.1:14550")

# kalkış fonksiyonu belirleme

def arm_and_takeoff(target_alt):
    print("arming motors...")

    while not vehicle.is_armable:
        time.sleep(1)
    vehicle.mode=VehicleMode("GUIDED")
    vehicle.armed=True

    print("TakeOff")
    vehicle.simple_takeoff(target_alt)

    while True:
        altitude=vehicle.location.global_relative_frame.alt

        if altitude>=target_alt-1:
            print("Altitude reached")
            break

        time.sleep(1)

#-----Ana program----
arm_and_takeoff(10)

#---set the default speed
vehicle.airspeed=7
#--- go to wpl 
print("go to wpl")

wpl=LocationGlobalRelative(-35.36228522, 149.16508596,10)
# wpl2=LocationGlobalRelative(-35.36268151 ,149.16522961,10)
vehicle.simple_goto(wpl)
time.sleep(5)
# vehicle.simple_goto(wpl2)


time.sleep(30)
# coming back 

print("coming backk")
vehicle.mode=VehicleMode("RTL")

time.sleep(20)

vehicle.close()
