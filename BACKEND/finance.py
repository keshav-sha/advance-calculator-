import math
# here we can add more financial calculations as needed 

class FinanceCalculator:
# This class provides static methods for performing various financial calculations.

    @staticmethod
    def simple_interest(principal: float, rate: float, time: float):
        return (principal * rate * time) / 100
# here we are defining a static method called simple_interest that takes three parameters: principal, rate, and time.
# It calculates the simple interest using the formula (principal * rate * time) / 100 and returns the result.
  
    @staticmethod
    def compound_interest(principal: float, rate: float, time: float):
        amount = principal * ((1 + rate / 100) ** time)
        return amount - principal
# here we are defining a static method called compound_interest that takes three parameters: principal, rate, and time.
# It calculates the compound interest using the formula principal * ((1 + rate / 100) ** time) and returns the result after subtracting the principal.
   
    @staticmethod
    def emi(principal: float, annual_rate: float, months: int):
        monthly_rate = annual_rate / (12 * 100)

        if monthly_rate == 0:
            return principal / months

        emi = (
            principal
            * monthly_rate
            * ((1 + monthly_rate) ** months)
        ) / (((1 + monthly_rate) ** months) - 1)

        return round(emi, 2)
# here we are defining a static method called emi that takes three parameters: principal, annual_rate, and months.
# It calculates the Equated Monthly Installment (EMI) using the formula for EMI and returns the result rounded to two decimal places. 
# If the monthly rate is zero, it simply divides the principal by the number of months.

    @staticmethod
    def gst(amount: float, gst_percent: float):
        gst_amount = amount * gst_percent / 100
        total = amount + gst_amount

        return {
            "gst": round(gst_amount, 2),
            "total": round(total, 2)
        }
# here we are defining a static method called gst that takes two parameters: amount and gst_percent.
# It calculates the GST amount using the formula amount * gst_percent / 100 and adds it to the original amount to get the total. 
# It returns a dictionary containing the GST amount and the total amount, both rounded to two decimal places.
   
    @staticmethod
    def discount(price: float, discount_percent: float):
        discount = price * discount_percent / 100

        return {
            "discount": round(discount, 2),
            "final_price": round(price - discount, 2)
        }
# here we are defining a static method called discount that takes two parameters: price and discount_percent.
# It calculates the discount amount using the formula price * discount_percent / 100 and subtracts it from the original price to get the final price. 
# It returns a dictionary containing the discount amount and the final price, both rounded to two decimal places.
  
    @staticmethod
    def profit_loss(cost_price: float, selling_price: float):

        if selling_price > cost_price:
            return {
                "type": "Profit",
                "amount": round(selling_price - cost_price, 2)
            }

        elif cost_price > selling_price:
            return {
                "type": "Loss",
                "amount": round(cost_price - selling_price, 2)
            }

        return {
            "type": "No Profit No Loss",
            "amount": 0
        }
# here we use or define the staticmethod to check the cost_price and selling_price 
# if the selling_price is more than the cost_price , it displays profit.
# if the cost_price more than the selling_price , it displa