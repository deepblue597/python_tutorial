# Lesson 3 Classes

## Class

H python όπως και πολλές άλλες γλώσσες ειναι μια αντικειμενοστρεφής γλώσσα το οποίο σημαίνει ότι σχεδόν οτιδήποτε υπάρχει στην Pyton ειναι ένα αντικείμενο.
Για να δημιουργήσουμε ένα αντικείμενο χρειαζόμαστε μια κλάση, ένα σετ απο οδηγίες με πράγματα δηλαδή που περιέχονται μέσα σε μια κλάση.
Μπορεί αυτό να ειναι μεταβλητές ή και συναρτήσεις της κλάσης.

### Create a class

Για να δημιουργήσεις μια κλάση στην Python χρησιμποιείς την λέξη class:

```
class Person:
    name = "Jason"
```

### Create object

Για την δημιουργία ενός Object χρησιμοποιούμε το όνομα της κλάσης

```
Player1 = Person()
print(Player1.name)
```

### `__init__()` function

Ο τρόπος που δημιουργούμε μέχρι τώρα τις κλάσεις δεν ειναι βολικός. Το να δίνουμε στατικά τιμές στις μεταβλητές μας, δεν είναι χρήσιμο και δεν βοηθάει στην δημιουργία πολλών Object με διαφορετικές τιμές στις μεταβλητές αυτές. Γι'αυτό στις κλάσεις υπάρχει η συνάρτηση `__init__()` η οποία τρέχει πάντα κατά τη δημιουργία ενός αντικειμένου. Διαμέσου της μπορούμε να θέσουμε τιμές στις μεταβλητές μας και να ορίσουμε ότιδήποτε άλλο θέλουμε να αρχικοποιηθεί όταν δημιουργούμε ένα αντικείμενο.

Σημείωση: Με την συνάρτηση `__init()__` χρησιμοποιούμε και την μεταβλητή self που θα την δούμε παρακάτω. Για την ώρα μας ενδιαφέρει η κατανόηση του τρόπου γραφής και όχι τι σημαίνει η μεταβλητή self.

### `__str__()` function

Η συνάρτηση `__str__()` καθορίζει τι θα εμφανίζει το αντικείμενο της κλάσης όταν εμφανίζεται σαν string.
Στην περιίπτωση που δεν έχει οριστεί θα εμφανιστεί η κλάση του αντικειμένου και η θέση του μέσα στην μνήμη του υπολογιστη.

### object methods

Μια κλάση μπορεί να περιέχει και μεθόδους οι οποίες θα μπορούν να καλεσθούν από όλα τα αντικείμενα της κλάσης

### self parameter

H μεταβλητή self χρησιμοποιείται για να μπορούμε να έχουμε πρόσβαση στις μεταβλητές του εκάστοτες αντικειμένου. Μπορεί να μην ονομάζεται self αλλά χρησιμοποιείται σαν κανόνας αυτή η λέξη. Θα πρέπει όμως να βρίσκεται πάντα ως πρώτη μεταβλητή σε κάθε συνάρτηση αν θέλουμε να την χρησιμοποιήσουμε.

### modify object properties

Για να αλλάξουμε ένα τη μεταβλητή ενός αντικειμένου μπορούμε να το κάνουμε γράφοντας

```
p1.age = 34
```

### delete object properties

### delete objects
