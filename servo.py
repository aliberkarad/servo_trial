"""
      SERVO_MOTOR APPLICATION_3
"""
# kütüphaneler
import RPi.GPIO as GPIO
import time

# GPIO pinlerini nümerik olarak kullanım
GPIO.setmode(GPIO.BOARD)

# GPIO 11. pini çıkış olarak ve servo için pwm başlatmak
GPIO.setup(11,GPIO.OUT)
servo = GPIO.PWM(11,50) # 50Hz pwm olarak kuruluyor

servo.start(0) # servo pwm sıfır olarak başlatılıyor

try:
    while True:
        #döndürme açısı sormak
        angle = float(input('Açı Giriniz 0 & 180: '))
        servo.ChangeDutyCycle(2+(angle/18))
        time.sleep(0.5)
        servo.ChangeDutyCycle(0)

finally:
    #tüm sistemleri temizleme
    servo.stop()
    GPIO.cleanup()
    print("BITTI")