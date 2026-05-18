from dronekit import connect, VehicleMode
import time

vehicle = connect('/dev/ttyAMA0', wait_ready=True, baud=57600)

print('Drone Connected')

vehicle.mode = VehicleMode('GUIDED')
vehicle.armed = True

while not vehicle.armed:
    print('Waiting for arming...')
    time.sleep(1)

print('Drone Armed')
