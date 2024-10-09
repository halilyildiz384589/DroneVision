from dronekit import connect, VehicleMode
import time

#Pixhawk bağlantı adresini belirttik (örneğin, "/dev/ttyAMA0" veya "udp:127.0.0.1:14550")
connection_string = '/dev/ttyAMA0'

vehicle = connect(connection_string, wait_ready=True, baud=57600)

esc1, esc2, esc3, esc4 = 1660, 1940, 1280, 1940

# Ana döngü
try:
    while True:

        # her bir motor kanalının anlık pwm değeri
        vehicle.channels.overrides['1'] = esc1
        vehicle.channels.overrides['2'] = esc2
        vehicle.channels.overrides['3'] = esc3
        vehicle.channels.overrides['4'] = esc4

        # Her bir ana çıkış pini için PWM değerlerini ekrana yazdırın
        print("Main Out 1 PWM: {}".format(vehicle.channels.overrides['1']))
        print("Main Out 2 PWM: {}".format(vehicle.channels.overrides['2']))
        print("Main Out 3 PWM: {}".format(vehicle.channels.overrides['3']))
        print("Main Out 4 PWM: {}".format(vehicle.channels.overrides['4']))

        # Belirli bir aralıkta güncelleme yapmak için bekleyin (örneğin, 0.2 saniye)
        time.sleep(0.2)

except KeyboardInterrupt:
    # Ctrl+C'ye basıldığında programı sonlandırın
    pass

finally:
    # Bağlantıyı kapatın
    vehicle.close()
