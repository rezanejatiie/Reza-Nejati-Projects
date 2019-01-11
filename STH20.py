def readtemp():
    from machine import Pin, I2C
    from time import sleep
    D1 = Pin(0)  # SCL, GPIO0
    D2 = Pin(2)  # SDA, GPIO2
    ADDRESS = 64
    FREQUENCY = 10000
    try:
      i2c = I2C(scl=D1, sda=D2, freq=FREQUENCY)
      i2c.writeto(ADDRESS, b'\xF3')
      sleep(0.1)
      raw = i2c.readfrom(ADDRESS, 2)
      t = (raw[0] << 8) + raw[1]
      temp = -46.85 + (175.72 * (t / 65536))
      return temp
    except Exception as err:
      temp = 55
      return temp


def readumid():
    from machine import Pin, I2C
    from time import sleep
    D1 = Pin(0)  # SCL, GPIO0
    D2 = Pin(2)  # SDA, GPIO2
    ADDRESS = 64
    FREQUENCY = 10000
    try:
      i2c = I2C(scl=D1, sda=D2, freq=FREQUENCY)
      i2c.writeto(ADDRESS, b'\xF5')
      sleep(0.1)
      raw = i2c.readfrom(ADDRESS, 2)
      h = (raw[0] << 8) + raw[1]
      humid = -6 + (125 * (h / 65536))
      return humid
    except Exception as err:
      humid = 100
      return humid
