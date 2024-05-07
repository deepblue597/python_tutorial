#%% dictionaries

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


#%% 

anotherdict = [
   {
   "brand": "Ford",
   "model": "Mustang",
   "year": 1964
   },
   { "brand": "Peugeot",
   "model": "306",
   "year": 1982
   }
]

print(anotherdict[0]["brand"])


#%% If statements 

a  = 5 
b = 20

if b > a : 
   print("b greater than a") 
elif a > b: 
   print("a greater than b")
else: 
   print("a and b equal")


#%% Άσκηση 

"""
Σε ένα νοσοκομείο σαν πρώτη μέρα μας ως γιατροί μας βάζουν να συμπληρώσουμε 
αν ο ασθενής ειναι υπέρβαρος, αν ειναι κανονικός ή αν είναι αδύνατος. 
Πιο συγκεκριμένα μας δίνουν το βάρος και το ύψος και θέλουμε να βρούμε το bmi του ασθενή 
bmi = βάρος/ύψος^2 (σε μέτρα) 
αν το bmi < 20 τότε ο ασθενής ειναι αδύνατος αν ειναι μεταξύ 20 και 30 είναι κανονικός και αν ειναι 
πάνω απο  30 τότε ειναι υπέρβαρος. Γράψτε ένα κώδικα που θα παίρνει το βάρος και το ύψος ενός 
ασθενή και θα βγάζει αν ειναι αδύνατος, κανονικός ή υπέρβαρος 
"""

weight = 90
height = 1.94

bmi = weight/height**2 

if bmi < 20 : 
   print("αδύνατος")
elif bmi < 30: 
   print("Κανονικός")
else: 
   print("υπερβαρος")

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
# %% Άσκηση 2

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
# %% Άσκηση Where is House Μέτρια

"""
Δουλεύετε στο διαγνωστικό τμήμα ενός νοσοκομείου και σας έρχονται 5 ασθενείς. 
Για αυτούς τους ασθενείς έχετε των αιρθμό των λευκών αιμοσφαιρίων, 
των ερυθρών και τον αιματοκρίτη τους. Είναι γνωστό ότι 

1. χαμηλά ερυθρά & χαμηλός αιμτοκρίτης -> Σιδηροπενική αναιμία
2. χαμηλά ερυθρά & χαμηλά λευκά -> Αναιμία χρόνιας νόσου
3. χαμηλά λευκά & υψηλός αιματοκρίτης -> Λοίμωξη ή φλεγμονή
4. υψηλός αιματοκρίτης & ηψυλά ερθρά -> Αφυδάτωση ή αληθή πολυκυτταραιμία

Παρακάτω δίνονται οι φυσιολογικές τιμές και οι τιμές των ασθενών 

Υποθέστε ότι μόνο μια διάγνωση μπορεί να γίνει σε κάθε ασθενή και οι 
ασθένειες πάνε με σειρά μεγαλύτερης προς μικρότερη πιθανότητα (δηλ η σιδηροπενική 
αναιμία είναι η πιο πιθανή νόσος απο τις υπόλοιπες) 


Bonus for home : Αν ήταν όλες ισοπίθανες και μπορούσε ένας ασθενής να έχει πάνω απο 
μια διάγνωση πως θα τη λύνατε ; Δύσκολη. 
"""

# Normal ranges
normal_ranges = {
    "WBC": [4.0, 11.0],
    "RBC": [4.2, 5.4],
    "Hct": [40, 50]
}

# Patient data
patients_data = [
    {"Name": "John", "WBC": 9.5, "RBC": 3.9, "Hct": 35},  # Patient 1
    {"Name": "Jason","WBC": 7.0, "RBC": 4.0, "Hct": 52},  # Patient 2
    {"Name": "Kleopatra","WBC": 12.0, "RBC": 5.5, "Hct": 48},  # Patient 3
    {"Name": "Danae","WBC": 5.5, "RBC": 3.5, "Hct": 38},  # Patient 4
    {"Name": "Omar" ,"WBC": 8.0, "RBC": 4.5, "Hct": 53}   # Patient 5
]


for patient in patients_data: 
   if(patient["RBC"] < normal_ranges["RBC"][0] and  patient["Hct"] < normal_ranges["Hct"][0]):
      print(patient["Name"] , " Σιδηροπενική αναιμία")
