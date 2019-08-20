Actual_Price = int(input("Enter the Price:  "))
Discount = int(input("Enter the Discount % :"))
Discount_Percentage = Discount/100
Reduced_Amount =round(Discount_Percentage * Actual_Price,2)
Amount_after_discount = Actual_Price - Reduced_Amount
print("The Reduced_Amount   is :",Reduced_Amount)
print("The Discount Percentage  is :",Discount_Percentage)
print ("Amount_after_discount:",Amount_after_discount)