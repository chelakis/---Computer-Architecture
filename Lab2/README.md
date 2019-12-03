#Αρχιτεκτονική Υπολογιστών

**2o Εργαστήριο** 
**Ομάδα 10: Χελάκης Κωνσταντίνος Μάριος** 

#Ερωτήματα

#Βήμα 1ο:  

##1ο Ερώτημα   
###Βρείτε τα μεγέθη των caches, το associativity κάθε μίας από αυτές και το μέγεθος της cache line  

Για να βρούμε αυτά τα μεγέθη ανοίγουμε σε οποιονδήποτε από τους παραγώμενους φακέλους το αρχείο *config.ini*  

Το μέγεθος της L1 Data cache φαίνεται στο tag *[system.cpu.dcache]* στην μεταβλητή ***size=65536*** (Bytes). Το associativity αναγράφεται στην μεταβλητή ***assoc=2***, η οποία δηλώνει ότι η dcache εχει 2-way set associativity.  

Το μέγεθος της L1 Instruction cache φαίνεται στο tag *[system.cpu.icache]* στην μεταβλητή ***size=32768*** (Bytes). Το associativity αναγράφεται στην μεταβλητή ***assoc=2***, η οποία δηλώνει ότι η icache εχει 2-way set associativity.

Το μέγεθος της cache line βρίσκεται στο tag *[system]*, στην μεταβλητή **cache_line_size=64** και δηλώνει ότι το μέγεθος του cache line ειναι 64 Bytes. 

Το μέγεθος της L2 cache φαίνεται στο στο tag *[system.l2.tags]* στην μεταβλητή ***size=2097152*** (Bytes). Το associativity αναγράφεται στην μεταβλητή ***assoc=8***, η οποία δηλώνει ότι η L2 cache εχει 8-way set associativity.  

##2ο Ερώτημα 
###Καταγράψτε τα αποτελέσματα από διαφορετικά benchmarks (i) χρόνο εκτέλεσης, (ii) CPI, (iii) miss rates 

Εκτελούμε αρχικά τα benchmarks που δόθηκαν στις οδηγίες: 

* **401.bzip2:** Το ακόλουθο benchmark εκτελείται πληκτρολογώντας την παρακάτω εντολή: 

'$ ./build/ARM/gem5.opt -d spec_results/specbzip configs/example/se.py --cpu-type=MinorCPU --caches --l2cache -c spec_cpu2006/401.bzip2/src/specbzip -o "spec_cpu2006/401.bzip2/data/input.program 10" -I 100000000'

Τα αποτελέσματα θα αποκηθευτούν στον φάκελο *speczib*, ο επεξεργαστής που χρησιμοποιείται είναι ο *MinorCPU*.

* **429.mcf:** Το ακόλουθο benchmark εκτελείται πληκτρολογώντας την παρακάτω εντολή: 

'$ ./build/ARM/gem5.opt -d spec_results/specmcf configs/example/se.py --cpu-type=MinorCPU --caches --l2cache -c spec_cpu2006/429.mcf/src/specmcf -o "spec_cpu2006/429.mcf/data/inp.in" -I 100000000'

Τα αποτελέσματα θα αποκηθευτούν στον φάκελο *specmcf*, ο επεξεργαστής που χρησιμοποιείται είναι ο *MinorCPU*.

* **456.hmmer:** Το ακόλουθο benchmark εκτελείται πληκτρολογώντας την παρακάτω εντολή: 

'$ ./build/ARM/gem5.opt -d spec_results/spechmmer configs/example/se.py --cpu-type=MinorCPU --caches --l2cache -c spec_cpu2006/456.hmmer/src/spechmmer -o "--fixed 0 --mean 325 --num 45000 --sd 200 --seed 0 spec_cpu2006/456.hmmer/data/bombesin.hmm" -I 100000000'

Τα αποτελέσματα θα αποκηθευτούν στον φάκελο *spechmmer*, ο επεξεργαστής που χρησιμοποιείται είναι ο *MinorCPU*. 

* **458.sjeng:** Το ακόλουθο benchmark εκτελείται πληκτρολογώντας την παρακάτω εντολή: 

'$ ./build/ARM/gem5.opt -d spec_results/specsjeng configs/example/se.py --cpu-type=MinorCPU --caches --l2cache -c spec_cpu2006/458.sjeng/src/specsjeng-o "spec_cpu2006/458.sjeng/data/test.txt" -I 100000000'

Τα αποτελέσματα θα αποκηθευτούν στον φάκελο *specsjeng*, ο επεξεργαστής που χρησιμοποιείται είναι ο *MinorCPU*.  

* **470.lbm:** Το ακόλουθο benchmark εκτελείται πληκτρολογώντας την παρακάτω εντολή: 

'$ ./build/ARM/gem5.opt -d spec_results/speclibm configs/example/se.py --cpu-type=MinorCPU --caches --l2cache -c spec_cpu2006/470.lbm/src/speclibm -o "20 spec_cpu2006/470.lbm/data/lbm.in 0 1 spec_cpu2006/470.lbm/data/100_100_130_cf_a.of" -I 100000000'

Τα αποτελέσματα θα αποκηθευτούν στον φάκελο *speclibm*, ο επεξεργαστής που χρησιμοποιείται είναι ο *MinorCPU*. 

**Τα αποτελέσματα μετά την εκτέλεση των παραπάνω benchmarks αναγράφονται στον παρακάτω πίνακα:**  

|          |sim_seconds	|CPI	|miss_rate dcache	|miss_rate icache	|miss_rate l2cache |
|---|---|---|---|---|---|
|specbzip	 |0.083982	|1.67965	 |0.014798	|0.00007	|0.282163 |
|specmcf	 |0.064955	|1.299095	 |0.002108	|0.023612	|0.055046 |
|spechmmer |0.059396	|1.187917	 |0.001637	|0.000221	|0.07776  |
|specsjeng |0.513528	|10.270554 |0.121831	|0.0002	  |0.999972 |
|speclibm	 |0.174671	|3.4934	   |0.060972	|0.00094	|0.99944  |

**Διάγραμμα Αποτελεσμάτων**

![Chart 1](/Lab2/Chart1.png)

Από τα παραπάνω αποτελέσματα βλέπουμε ότι όσο αυξάνονται το miss rate της L2 cache (σε μεγαλύτερο βαθμό) και της L1 cache (σε μικρότερο βαθμό) , τόσο αυξάνεται και το CPI. Αυτό είναι λογικό αφού το CPI εξαρτάται από τα miss rates τόσο της L2 cache όσο και των L1 icache και dcache. 

Συνεπώς στα δύο benchmarks με τους μεγαλύτερους χρόνους (sjeng και libm) είναι αυτά που χουν τα περισσότερα L2 miss rates και συνεπώς το μεγαλύτερο CPI. Αυτό συμβαίνει διότι η L2 cache είναι σχετικά πιο αργή από την L1 cache με συνέπεια τα misses να στοιχίζουν πιο πολύ σε χρόνο για το σύστημα μας.

Η L1 cache είναι πιο γρήγορη μνήμη και για αυτό τα misses δεν παίζουν ιδιαίτερο ρόλο στο CPI. Αυτό μπορούμε να το διαπιστώσουμε στα δύο πρώτα benchmarks (bzip και mcf) τα οποία ενώ εμφανίζουν σχετικά μεγαλύτερο miss rate στην dcache και icache, δεν επιρεάζουν σε μεγάλο βαθμό το CPI. 

##3ο Ερώτημα 
###Τρέξτε ξανά τα benchmarks με cpu-clock=1GHz και εντοπίστε τις πληροφορίες για το ρολόι.

