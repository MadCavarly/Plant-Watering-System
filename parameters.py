class Parameters:
    def __init__(self, check_time=1800, soil_moisture= 25):
        self.check_time = check_time
        self.soil_moisture_limit= soil_moisture
    
    def calculate_parameters(self, soil_moisture, air_humidity, temperature):
        if(temperature>30 and air_humidity<30):
            self.soil_moisture_limit = 35
        elif(temperature<18):
            self.soil_moisture_limit = 15
        else:
            self.soil_moisture_limit = 25
