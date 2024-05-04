
# Identation check 
# Ποιο ειναι το σωστό ; 
#  Στόχος του προγράμματος ειναι αν το x > 5 να εκτυπώσει hello world 
 
#%%
x = 5  

# if x > 3 : 
#     print("hello world")

# if x > 3:
# print("hello world")

# if x > 3 : 
#       print("hello world")


#%% 

# εδώ θα δούμε την αξία σωσής γραφής κώδικα 
# 2 συνάρτήσεις που κάνουμε το ιδιο πράγμα 

import numpy as np

def fun(x): 
    num_1 = np.sum(x) 
    num_2 = len(x) 
    num_3 = num_1 / num_2 
    return num_3 


def mean(data): 
    # sum of all the data 
    sum_data = np.sum(data)

    # number of data  
    num_of_data = len(data)

    #mean value  
    mean_val = sum_data / num_of_data

    #return mean value 
    return mean_val 

x = [1 , 2 , 3 ]

print(mean(x))  
print(fun(x))
# %% data types 

greetings = 'Hello my name is Jason!'

print(type(greetings)) 
# %% true or false ? 

num = 5 

true_false = num > 5 # αν ήταν >= ;  

print(true_false)
# %%  Convert  ποια θα ειναι η τιμη του Int_num 

float_num = 5.88  

int_num = int(float_num)

print(int_num)

#%% πρόσθεση 

num_1 = 5.99 

num_2 = 1.22 

sum = num_1 + num_2 

print(sum) 

#%% δυνάμεις 

num_1 = 4 

dynami = 3 

apot = num_1 ** dynami 

#%% Ποια θα είναι η τιμή του χ ; 

x = 5 

x += 5 

x **= 2 

#%% Ασκηση 1 ο χρόνος ειναι χρήμα 

"""
Ο ιάσονας κάθε δευτερόλεπτο κερδίζει 13.22 ευρώ. Θα ήθελε να μάθει πόσα
χρήματα κερδίζει σε 7 ώρες 22 λεπτά και 5 δευτερόλεπτα  
"""

wage = 13.22 
hours = 7 * 60 * 60 
minutes = 22 * 60 
sec = 5 

total_sec = hours + minutes + sec

total_wage = wage * total_sec

print(total_wage)

#%% Άσκηση 2 Μας κλέβει το κράτος 

""" 
O Βασίλης θα πάρει τον πρώτο του μισθό ο οποίος θα ανέρχεται 
στα 1543 ευρώ μοικτά. Η εφορία θα του κρατήσει το 18% του μισθού 
του. Πόσα χρήματα θα έχει στα χέρια του ο Βασίλης τελικά;  Πόσα 
χρήματα του κράτησε το κράτος; 
Φτιάξτε ένα πρόγραμμα το οποίο θα μπορεί να Υπολογίζει τα παραπάνω και να τα εμφανιζει 
"""

paycheck = 1543 
tax = 0.18 

kratos = paycheck * tax 
money_vas = paycheck - kratos
print("χρήματα Βασιλη " , money_vas)
print(kratos)
# %% Άσκηση 3 Πόσα έχω για το μήνα ; 

"""
θα θέλαμε να βρίσκουμε γενικά το ποσό των χρημάτων που θα έχει στα 
χέρια του ο πολίτης και το ποσό που κρατάει το κράτος. Μπορείτε 
να φτιάξετε ένα πρόγραμμα που θα ρωτάει το χρήστη το μοικτό μισθό του 
και τον ποσοστό του φόρου και να βγάζει σαν αποτέλεσμα το τελικό 
μισθό του χρήστη ; 

Σημείωση: Προκειμένου να πάρετε απο τον χρήστη πληροφορία θα χρησιμοποιήσετε 
την συνάρτηση input 
num_1 = input("something") 
Προσοχή! ο τύπος της μεταβλητής num_1 ειναι string 
"""

paycheck = input("Πόσα ειναι τα μοικτά χρήματα;")

tax = input("Πόσος είναι ο κράτικός φόρος; (αριθμος πχ για 20% γράψτε 20)")

paycheck = float(paycheck)
tax = float(tax)  
kratos = paycheck * tax / 100 

money = paycheck - kratos

print(money)

# %% Lists 

#empty list 
empty_list = []  

groceries = ['bananas' , 'apples' , 'oranges', 'pears']

#access 
print(groceries[0])

print(groceries[1:4])

#length 
print(len(groceries))

#append 

groceries.append("milk")
print(groceries)  

# insert 
# Σε ποια θέση θα μπει ; 
groceries.insert(2 , "watermelon")
print(groceries)

supermarket = ['meat' , 'chocolate' , 'eggs']

groceries.extend(supermarket)
print(groceries)

# %% remove

groceries.remove('meat')

groceries.pop(0)
# %% Τι θα κάνει αυτή η συνάρτηση  ; 

for item in groceries: 
    print(item)

# %%

min(groceries) 
max(groceries)
# %% Άσκηση Ο χρηματιστής 

'''
έχουμε Μια λίστα με πωλήσεις μιας εταιρίας του τελευταίου χρόνου. Κάθε αντικείμενο της λίστας παρουσιάζει τα έσοδα 
κάθε μήνα. Αυτά βρίσκοντα στην μεταβλητή sales_data. Στόχος είναι 

1. Να βρεθούν τα συνολικά κέρδη της εταιρίας τον προηγούμενο χρόνο - easy 
2. Να βρεθεί η μέση τιμή των κερδών του προηγούμενου χρόνου - easy 
3. Να βρεθούν οι μήνες με τα χαμηλότερα και υψηλότερα έσοδα - easy 
4. Να βρεθεί το ποσοστό αύξησης η μείωσης των κερδών ανα μήνα (απο τον ένα μήνα στον επόμενο) και να αποθηκευτούν σε μια λίστα - hard 
5. Αν το κράτος κρατάει 15.3% των κερδών να βρεθούν τα χρήματα που δίνονται στο κράτος κάθε μήνα, τα συνολικά 
    χρήματα που δώθηκαν τον προηγούμενο χρόνο στο κράτος και τα κέρδη μετά την αφαίρεση του φόρου 
    και να αποθηκευτούν το κάθενα σε μια λίστα - medium 

Σημείωση : Για το ερώτημα 4 βοηθάει η συνάρτηση range(start , stop) όπου λέει στο πρόγραμμα από ποια θέση 
έσως ποιά θέση να κάνει μια πράξη πχ 
for i in range(1 , 4): 
    print(groceries[i])
'''

sales_data = [50000, 60000, 55000, 72000, 68000, 75000, 80000, 85000, 90000, 95000, 100000, 110000]

sum_sales = sum(sales_data)
num_sales = len(sales_data)

mean_sales = sum_sales / num_sales

max_rev = max(sales_data)
min_rev = min(sales_data)

percentages = [] 
for i in range(1 , len(sales_data)):
    percentage = (sales_data[i] - sales_data[i-1]) / sales_data[i-1] 
    percentage = percentage * 100 
    percentages.append(percentage)

kratos = [] 
final_sales = [] 
tax = 0.153
for sales in sales_data:
    taxes = sales * tax
    kratos.append(taxes)
    clean_sale = sales - taxes 
    final_sales.append(clean_sale)

kratos_total = sum(kratos)
print(percentages) 
print(final_sales)
print(kratos)
print(kratos_total)

