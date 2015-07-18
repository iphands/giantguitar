import spidev

class Reader(object):

    def __init__(self, channels):
        self.channels = channels
        self.spi = spidev.SpiDev()
        self.spi.open(0,0)

    def read_channel(self, channel):
        adc = self.spi.xfer2([1, (8+channel)<<4, 0])
        data = ((adc[1] & 3) << 8) + adc[2]
        return data

    def convert_volts(self, data, places):
        volts = (data * 3.3) / float(1023)
        volts = round(volts, places)
        return volts

    def fetch(self):
        for ch in self.channels:
            self.channels[ch] = self.read_channel(ch)



    

