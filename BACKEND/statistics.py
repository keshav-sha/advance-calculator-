import statistics
#here we are importing the statistics module, which provides functions for calculating mathematical statistics of numeric data.
# This module will be used in the StatisticsCalculator class to perform various statistical calculations such as mean, median, mode, variance, and standard deviation.

class StatisticsCalculator:
# This class provides static methods for performing various statistical calculations on a list of numbers.

    @staticmethod
    def mean(numbers):
        return statistics.mean(numbers)
# here we are defining a static method called mean that takes a list of numbers as input and returns 
# the mean (average) of those numbers using the mean function from the statistics module.

    @staticmethod
    def median(numbers):
        return statistics.median(numbers)
# here we are defining a static method called median that takes a list of numbers as input and returns
# the median (middle value) of those numbers using the median function from the statistics module.

    @staticmethod
    def mode(numbers):
        try:
            return statistics.mode(numbers)
        except statistics.StatisticsError:
            return "No unique mode found"
# here we are defining a static method called mode that takes a list of numbers as input and returns
# the mode (most common value) of those numbers using the mode function from the statistics module

    @staticmethod
    def variance(numbers):
        return statistics.variance(numbers)
# here we are defining a static method called variance that takes a list of numbers as input and returns
# the variance (measure of how far the numbers are spread out) of those numbers using the
    
    @staticmethod
    def standard_deviation(numbers):
        return statistics.stdev(numbers)
# here we are defining a static method called standard_deviation that takes a list of numbers as input and returns
# the standard deviation (measure of the amount of variation or dispersion of a set of values)

    @staticmethod
    def minimum(numbers):
        return min(numbers)
# here we are defining a static method called minimum that takes a list of numbers as input and returns
# the minimum (smallest) value from that list using the built-in min function.

    @staticmethod
    def maximum(numbers):
        return max(numbers)
# here we are defining a static method called maximum that takes a list of numbers as input and returns
# the maximum (largest) value from that list using the built-in max function.

    @staticmethod
    def value_range(numbers):
        return max(numbers) - min(numbers)
# here we are defining a static method called value_range that takes a list of numbers as input and returns
# the range (difference between the maximum and minimum values) of those numbers.
