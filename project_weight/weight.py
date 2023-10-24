import time
import sys

EMULATE_HX711=False
#값 보정
referenceUnit = 474 

if not EMULATE_HX711:
    import RPi.GPIO as GPIO
    #HX711 라이브러리 임포트
    from hx711 import HX711
else:
    from emulated_hx711 import HX711
    
#시스템 종료
def exit():
    sys.exit()
 
# GPIO 핀번호 (앞: DT, 뒤: SCK)   
hx=HX711(20,16)

hx.set_reading_format("MSB","MSB")
hx.set_reference_unit(referenceUnit)


hx.reset()
hx.tare()
print("start")

def weight_start():
    while True:
        try:
            val=hx.get_weight(5)
            round_val=round(val, 0)
            print(round_val)
            
            hx.power_down()
            hx.power_up()
            time.sleep(0.001)
        except(KeyboardInterrupt, SystemExit):
            exit()
            
weight_start()