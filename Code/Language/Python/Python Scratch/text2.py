# edit in your free time for understanding

# Put your code here
start = float(input("Enter the purchase price: "))
# Algorithm
"""

"""
print("Month   Starting Balance   Interest to Pay     Principal to Pay   Ending Balance ")
while start > 0:
    month = 1
    #start = (180.00) # Starting Payment
    a = start*00.01 #Interest
    princ = (0.05*start-a) #Principal
    monthpay = (0.05*start) # Monthly Payment
    endpay = float(start-princ) # End balance = Starting Payment - Principal
    print(month ,'  %.2f  ' % start,'%.2f  ' % a,'%.2f  ' % princ,'%.2f  ' % monthpay,'%.2f ' % endpay )

print("-------------")
for i in range(1,month+24):
    #print(i,"  ",end="")
    print(month ,'  %.2f  ' % start,'%.2f  ' % a,'%.2f  ' % princ,'%.2f  ' % monthpay,'%.2f ' % endpay )
    month+=1
    start = endpay - princ

    !!
    #Broken code, loops infinately.
