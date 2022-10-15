basic.forever(function () {
    if (mbit_Sensor.Ultrasonic(DigitalPin.P14, DigitalPin.P15) < 2) {
        basic.showIcon(IconNames.Happy)
    } else {
        basic.showIcon(IconNames.Sad)
    }
})
