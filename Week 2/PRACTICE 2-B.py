
# coding: utf-8

# In[3]:


def convertcurrencies(from_currency = "USD",to_currency = "JOD",amount = 1):
    if from_currency == "USD":
        if to_currency == "JOD":
            return amount * 0.71
        elif to_currency == "TRY":
            return amount * 5.56
        else:
            print ("The Currency is Invalid")
    elif from_currency == "JOD":
        if to_currency == "USD":
            return amount * 1.41
        elif to_currency == "TRY":
            return amount * 7.88
        else:
            print ("The Currency is Invalid")
    elif from_currency == "TRY":
        if to_currency == "JOD":
            return amount * 0.13
        elif to_currency == "USD":
            return amount * 0.18
        else:
            print ("The Currency is Invalid")

print(convertcurrencies("JOD","TRY",50))

