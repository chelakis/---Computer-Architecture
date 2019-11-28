# Arx.Yp.2019Ex1.Chelakis
**Πρώτο παραδοτέο του εργαστηρίου της Αρχιτεκτονικής Υπολογιστών**

# Ερωτήματα
## 1. Ποιες είναι βασικές παράμετροι που έχει περάσει στον gem5 για το σύστημα προς εξομοίωση;

Το παράδειγμα μας δίνει αρχικά 3 επιλογές για τύπο CPU, τον atomic, τον minor και τον hpi. Ο atomic CPU φαίνεται να μην περιλαμβάνει κάποια μνήμη cache καθώς στα ορισματά του οι μεταβλητές είναι None. Στον minorCPU "φορτώνονται" μαζί με τον CPU οι icache, dcache, η walk cache και η L2 cache.
Το μέγεθος της cache στην συνέχεια δηλώνεται 64 bit. 
Στην συνέχεια φαίνεται να δηλώνεται η τάση και η συχνότητα λειτουργίας του επεξεργαστή (3.3V και 1 GHz).
Έπειτα ορίζεται το cluster του CPU το οποίο περιλαμβάνει τους πυρήνες, 2 private L1 caches και 1 shared L2 cache (στην περίπτωση minorCPU).
Στη στνέχεια ιεραρχούνται οι μνήμες cache και συνδέονται με την κύρια μνήμη. 
Η κύρια μνήμη οριοθετείται στον φυσικό χώρο.
Τέλος καλούνται οι κατάλληλες συναρτήσεις για την εκτέλεση του προγράμματος.

Κάποιες από τις τροποποιήσημες μεταβλητές στο αρχείο se.py είναι:  
*-cpu:* υποδεικνύει τον τύπο του kernel που χρησιμοποιείται μεταξύ atomic, minor, hpi.  
*-cpu-freq:* υποδεικνύει την συχνότητα ρολογιού του επεξεργαστή.  
*-num-cores:* υποδεικνύει τον αριθμό των πυρήνων του επεξεργαστή CPU.  
*-mem-type:* υποδεικνύει τον τύπο της RAM του συστήματος.  
*-mem-rank:* υποδεικνύει την ιεραρχία της μνήμης.  
*-mem-size:* υποδεικνύει το συνολικό μέγεθος της μνήμης RAM.  

## 2. Αρχεία config.ini και config.json;
Στο αρχείο config.ini (περιλαμβάνεται στο repository) μπορούμε να δούμε τις αποθηκευμένες τιμές και χαρακτηριστικά συστήματος που δημιούργησε ο gem5 στην προσομοίωση.
Ξεκινόντας από τις πρώτες γραμμές βλέπουμε ορισμένα χαρακτηριστικά όπως:
**cache_line_size=64:** Μέγεθος μνήμης cache
**mem_mode=timing:** Η κύρια μνήμη είναι σε λειτουργία timing
**mem_ranges=0:2147483647:** Φυσικές διευθύνσεις μνήμης
**[system.cpu_cluster.cplus]**
**type=MinorCPU:** Τύπος επεξεργαστή
**children=branchPred dcache dtb dtb_walker_cache executeFuncUnits icache interrupts isa itb_walker_cache tracer workload:&& Υπο-κλάσεις της κλάσης cpu (περιλαμβάνει τις cache)
**[dcache.tags]**
**entry_size=64:** μέγεθος κάθε λέξης που αποθηκευεται
**size=32768** μέγεθος dcache σε bit (λογικα)
***[icache.tags]***
**entry_size=64:** μέγεθος κάθε λέξης που αποθηκευεται
**size=49152** μέγεθος dcache σε bit (λογικα)

## 3. Πληροφορίες για άλλα μοντέλα CPU;

### MinorCPU (source: http://www.gem5.org/docs/html/minor.html)
Ο επεξεργαστής minor είναι ένα επεξεργαστικό μοντέλο το οποίο χρησιμοποιείται για να προσομοιώσει επεξεργαστές με αυστηρή ιεράρχηση των πράξεων στην εκτέλεση τους. 
Επίσης υπάρχουν εργαλεία για την προβολή των εντολών σε κάθε θέση τους μέσα στο σύστημα. 

### TimingSimpleCPU (source: http://gem5.org/SimpleCPU)
Ο επεξεργαστής Timing Simple είναι μία έκδοση επεξεργαστικής μονάδας που αφήνει την προσπέλαση στην μνήμη για συγκεκριμένα και καθορισμένα χρονικά διαστήματα.

### AtomicSimpleCPU 
Ο επεξεργαστής Atomic είναι μια έκδοση επεξεργαστικής μονάδας στον οποίο η πράξη που εκτελείται εκτιμά πόσο χρόνο θα χρειαστεί να εκτελεστεί και εκτελείται για τον χρόνο αυτό χωρίς να μπορεί να διακοπεί. (Η atomic λειτουργία με αυτόν τον τρόπο δεν μπορεί να συνυπάρχει με την Timing)

## 3a. Εκτέλεση προγράμματος στον gem5
### Εκτέλεση αρχείου se.py με MinorCPU
**Εντολή:** *./build/ARM/gem5.opt -d hw_se_minor configs/example/se.py --cpu-type=MinorCPU --caches -c  tests/test-progs/hello/bin/arm/linux/hello*

**Αποτέλεσμα:** Hello world! Exiting @ tick 25502000

### Εκτέλεση αρχείου se.py με AtomicCPU
**Εντολή:** *./build/ARM/gem5.opt -d hw_se_atomic configs/example/se.py --cpu-type=AtomicSimpleCPU --caches -c  tests/test-progs/hello/bin/arm/linux/hello*

**Αποτέλεσμα:** Hello world! Exiting @ tick 2915000  
*Παρατηρώ ότι ο atomic είναι πιο αργός από τον minor*

### Εκτέλεση αρχείου se.py με TimingSimpleCPU
**Εντολή:** *./build/ARM/gem5.opt -d hw_se_timingsimple configs/example/se.py --cpu-type=TimingSimpleCPU --caches -c  tests/test-progs/hello/bin/arm/linux/hello*

**Αποτέλεσμα:** Hello world!Exiting @ tick 28667000  
*Παρατηρώ ότι ο timing simple είναι πιο γρήγορος από τον atomic και πιο αργός από τον minor. Το αποτέλεσμα είναι αναμενόμενο καθώς ο minor χρησιμοποιεί 4-stage pipeline. Έτσι τα δεδομένα μπορούν να "φορτωθούν" πιο γρήγορα στον επεξεργαστή*

### Εκτέλεση αρχείου se.py με MinorCPU και συχνότητα 5GHz
**Εντολή:** *./build/ARM/gem5.opt -d hw_se_minor_5ghz configs/example/se.py --cpu-type=MinorCPU --cpu-clock=5GHz  --caches -c  tests/test-progs/hello/bin/arm/linux/hello*

**Αποτέλεσμα:** Hello world! Exiting @ tick 22607800  
*Πιο γρήγορος από τον default minorCPU αφού χρειάστηκε λιγότερο χρόνο ολοκλήρωσης*

### Εκτέλεση αρχείου se.py με MinorCPU και συχνότητα 400Hz
**Εντολή:** *./build/ARM/gem5.opt -d hw_se_minor_400 configs/example/se.py --cpu-type=MinorCPU --cpu-clock=400  --caches -c  tests/test-progs/hello/bin/arm/linux/hello*

**Αποτέλεσμα:** Hello world! Exiting @ tick 26727500000000  
*Πολύ πιο αργός από τον default minorCPU αφού χρειάστηκε πολύ περισσότερο χρόνο ολοκλήρωσης*

### Εκτέλεση αρχείου se.py με MinorCPU και μνήμη DDR4
*./build/ARM/gem5.opt -d hw_se_minor_ddr4 configs/example/se.py --cpu-type=MinorCPU --mem-type=DDR4_2400_8x8  --caches -c  tests/test-progs/hello/bin/arm/linux/hello*

**Αποτέλεσμα:** Hello world! Exiting @ tick 24855000  
*Ελάχιστα πιο γρήγορη ολοκλήρωση με την μνήμη DDR4. Υποθέτω ότι επειδή είναι πιο γρήγορη τεχνολογία είναι και πιο γρήγορη.*

### Εκτέλεση αρχείου se.py με MinorCPU και μνήμη DDR3
*./build/ARM/gem5.opt -d hw_se_minor_ddr3 configs/example/se.py --cpu-type=MinorCPU --mem-type=DDR3_1600_8x8  --caches -c  tests/test-progs/hello/bin/arm/linux/hello*

**Αποτέλεσμα:** Hello world! Exiting @ tick 25502000  
*Ίδιος χρόνος ολοκλήρωσης με το default. Λογικά η default μνήμη RAM είναι τύπου DDR3.*

# **Τα αρχεία stats βρίσκονται στους αντίστοιχους φακέλους στον φακελο run_files**  
# **Ότι έτρεξα στο terminal του linux καθώς και ότι μου επέστρεψε βρίσκεται στο αρχείο bashcode**
