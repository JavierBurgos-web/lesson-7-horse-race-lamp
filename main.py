def on_forever():
    if mbit_Sensor.ultrasonic(DigitalPin.P14, DigitalPin.P15) < 10:
        basic.show_icon(IconNames.HAPPY)
    else:
        basic.show_icon(IconNames.SAD)
basic.forever(on_forever)
