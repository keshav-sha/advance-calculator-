class UnitConverter:
# here we are defining a class called UnitConverter that contains static methods for converting between different units of measurement. 
# Each method takes a float value as input and returns the converted value.'
# it used for converting between different units of measurement such as length, weight, temperature, time, and data storage.

    @staticmethod
    def meter_to_kilometer(value: float):
        return value / 1000
# here we are defining a static method called meter_to_kilometer that 
# takes a float value as input and returns the equivalent value in kilometers by dividing the input value by 1000.

    @staticmethod
    def kilometer_to_meter(value: float):
        return value * 1000
# here we are defining a static method called kilometer_to_meter that 
# takes a float value as input and returns the equivalent value in meters by multiplying the input value by 1000.

    @staticmethod
    def meter_to_centimeter(value: float):
        return value * 100
# here we are defining a static method called meter_to_centimeter that
# takes a float value as input and returns the equivalent value in centimeters by multiplying the input value by 100.

    @staticmethod
    def centimeter_to_meter(value: float):
        return value / 100
# here we are defining a static method called centimeter_to_meter that 
# takes a float value as input and returns the equivalent value in meters by dividing the input value by 100.

    @staticmethod
    def kilogram_to_gram(value: float):
        return value * 1000
# here we are defining a static method called kilogram_to_gram that 
# takes a float value as input and returns the equivalent value in grams by multiplying the input value by 1000.

    @staticmethod
    def gram_to_kilogram(value: float):
        return value / 1000
# here we are defining a static method called gram_to_kilogram that 
# takes a float value as input and returns the equivalent value in kilograms by dividing the input value by 1000.

    @staticmethod
    def celsius_to_fahrenheit(value: float):
        return (value * 9 / 5) + 32
# here we are defining a static method called celsius_to_fahrenheit that
# takes a float value as input and returns the equivalent value in Fahrenheit by using the formula (value * 9 / 5) + 32.    

    @staticmethod
    def fahrenheit_to_celsius(value: float):
        return (value - 32) * 5 / 9
# here we are defining a static method called fahrenheit_to_celsius that
# takes a float value as input and returns the equivalent value in Celsius by using the formula (value - 32) * 5 / 9.
    
    @staticmethod
    def hours_to_minutes(value: float):
        return value * 60
# here we are defining a static method called hours_to_minutes that
# takes a float value as input and returns the equivalent value in minutes by multiplying the input value by 60.

    @staticmethod
    def minutes_to_hours(value: float):
        return value / 60
# here we are defining a static method called minutes_to_hours that
# takes a float value as input and returns the equivalent value in hours by dividing the input value by 60.

    # Data Storage
    @staticmethod
    def mb_to_gb(value: float):
        return value / 1024
# here we are defining a static method called mb_to_gb that
# takes a float value as input and returns the equivalent value in gigabytes by dividing the input value by 1024.

    @staticmethod
    def gb_to_mb(value: float):
        return value * 1024
# here we are defining a static method called gb_to_mb that
# takes a float value as input and returns the equivalent value in megabytes by multiplying the input value by 1024.