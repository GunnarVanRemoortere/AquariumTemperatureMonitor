class DS18B20Class:

    @staticmethod
    def read_temp_raw():
        sensor_file = '/sys/bus/w1/devices/w1_bus_master1/28-0316616335ff/w1_slave'
        with open(sensor_file, 'r') as f:
            lines = f.readlines()
            return lines

    def read_temp(self):
        lines = self.read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            return lines[1]

    def convert_temp(self):
        full_line = self.read_temp()
        temp = full_line[29:]
        temp = temp[0:2] + "." + str(round(int(temp[3:]), 1)) + "\N{DEGREE SIGN}C"
        return temp

    def geefTemperaturen(self):
        temperaturen = self.convert_temp()
        return temperaturen