from dronekit import connect

vehicle = connect('/dev/ttyAMA0', wait_ready=True)

print('GPS:', vehicle.gps_0)
print('Battery:', vehicle.battery)
print('Altitude:', vehicle.location.global_relative_frame.alt)
print('Mode:', vehicle.mode.name)
