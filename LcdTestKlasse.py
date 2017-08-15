from LCD import Lcd
from time import sleep
from RPi import GPIO

rs = 20
e = 16
D7 = 27
D6 = 22
D5 = 5
D4 = 6

instance_lcd = Lcd(e, rs, D7, D6, D5, D4)

try:
    instance_lcd.init_display(blink_cusror=False)
    instance_lcd.write_word("Hey")
    instance_lcd.move_to_second_line()
    instance_lcd.write_word("Kenny!")
    sleep(10)
    instance_lcd.clear_display()

finally:
    GPIO.cleanup()
