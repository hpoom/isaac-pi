from gpiozero import PWMOutputDevice
from time import sleep

BUZZERPIN = 12

buzzer = PWMOutputDevice(BUZZERPIN)
buzzer.frequency = 5000
buzzer.value = 0.0
def buzz (frequency, period) :
    buzzer.frequency= frequency
    buzzer.value = 0.5
    sleep(period)
    buzzer.value = 0.0
	
while True:
    buzz(3000, 2)
    sleep(1)
