
#%% 

# For loops 

sgpt = [ 30 , 12 , 22 , 100 , 123 , 500 , 19]

for value in sgpt : 
    print(value)

# %% in range 

for i in range(10): 
    print(i , " times that we run the in range")

for i in range(1 , 11): 
    print(i , " times that we run the function")

# Τι θα εκτυπώσει ο παρακάτω κώδικας; Συμπληρώστε το κείμενο
for i in range(0 , 10 , 2): 
    print(i , "")
# %% Άσκηση 1 

"""
Σε μια γενική εξέταση αίματος ξέρουμε ότι ο ασθενής έχει πρόβλημα με τα ηπατικά (τρανσαμινάσες)
οι οποίες βρίσκονται στις θέσεις 4 εως 8 (και την 8) του παρακάτω πίνακα. Θέλουμε ένα 
πρόγραμμα που να παρουσιάζει μόνο αυτές τις τιμές.
"""

patient = [ 30 , 12 , 22 , 100 , 123 , 500 , 19, 200 , 12 , 11]


for i in range(3 , 8): 
    print(patient[i])


#%% 

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

# %% Τι θα εκτυπώνει στις δύο print η συνάρτηση ; 

patients = [[1 , 3 , 11] , [22 , 44 , 22] , [11 , 111 , 234]  ]

for patient in patients:
   print(patient) 
   for value in patient: 
      print(value)
# %%
