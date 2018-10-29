
# coding: utf-8

# In[7]:


jorStates = ["Irbid","Ajloun","Jerash","Mafraq","Balqa","Amman",
                "Zarqa","Madaba","Karak","Tafilah","Ma'an","Aqaba"]


jorStates.sort ()

for state in jorStates:
    if len(state) == 5:
        print(state)

print ("---------------------------")

for state in jorStates:
    if state[0] == "A":
        print(state)

