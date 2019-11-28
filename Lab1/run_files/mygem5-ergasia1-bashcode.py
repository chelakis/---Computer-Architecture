#Arxitektoniki Ipologiston
#Proto paradoteo
#Parakato vriskontai oi entoles pou etrexa sto gem5 kai ta apotelesmata tous

#1. ektelesi programatos hello world starter
chelakis@chelakis-VirtualBox ~/mygem5> 
build/ARM/gem5.opt -d hw_hello_result_starter configs/example/arm/starter_se.py --cpu="minor" "tests/test-progs/hello/bin/arm/linux/hello"

#result
gem5 Simulator System.  http://gem5.org
gem5 is copyrighted software; use the --copyright option for details.

gem5 compiled Nov 19 2019 14:07:13
gem5 started Nov 23 2019 13:59:09
gem5 executing on chelakis-VirtualBox, pid 4706
command line: build/ARM/gem5.opt -d hw_hello_result_starter configs/example/arm/starter_se.py --cpu=minor tests/test-progs/hello/bin/arm/linux/hello

info: 1. command and arguments: ['tests/test-progs/hello/bin/arm/linux/hello']
Global frequency set at 1000000000000 ticks per second
warn: DRAM device capacity (8192 Mbytes) does not match the address range assigned (1024 Mbytes)
warn: DRAM device capacity (8192 Mbytes) does not match the address range assigned (1024 Mbytes)
0: system.remote_gdb: listening for remote gdb on port 7000
info: Entering event queue @ 0.  Starting simulation...
warn: CP14 unimplemented crn[14], opc1[7], crm[15], opc2[7]
Hello world!
exiting with last active thread context  @  24087000

#2. ektelesi tou script se.py me minorCPU
chelakis@chelakis-VirtualBox ~/mygem5> 
./build/ARM/gem5.opt -d hw_se_minor configs/example/se.py --cpu-type=MinorCPU --caches -c  tests/test-progs/hello/bin/arm/linux/hello

#result
gem5 Simulator System.  http://gem5.org
gem5 is copyrighted software; use the --copyright option for details.

gem5 compiled Nov 19 2019 14:07:13
gem5 started Nov 23 2019 13:58:28
gem5 executing on chelakis-VirtualBox, pid 4673
command line: ./build/ARM/gem5.opt -d hw_se_minor configs/example/se.py --cpu-type=MinorCPU --caches -c tests/test-progs/hello/bin/arm/linux/hello

Global frequency set at 1000000000000 ticks per second
warn: DRAM device capacity (8192 Mbytes) does not match the address range assigned (512 Mbytes)
0: system.remote_gdb: listening for remote gdb on port 7000
**** REAL SIMULATION ****
info: Entering event queue @ 0.  Starting simulation...
warn: CP14 unimplemented crn[14], opc1[7], crm[15], opc2[7]
Hello world!
Exiting @ tick 25502000 because exiting with last active thread context
Simulated exit code not 0! Exit code is 13

#3. ektelesi tou script se.py me atomicCPU
chelakis@chelakis-VirtualBox ~/mygem5> 
./build/ARM/gem5.opt -d hw_se_atomic configs/example/se.py --cpu-type=AtomicSimpleCPU --caches -c  tests/test-progs/hello/bin/arm/linux/hello

#result
gem5 Simulator System.  http://gem5.org
gem5 is copyrighted software; use the --copyright option for details.

gem5 compiled Nov 19 2019 14:07:13
gem5 started Nov 23 2019 14:00:46
gem5 executing on chelakis-VirtualBox, pid 4895
command line: ./build/ARM/gem5.opt -d hw_se_atomic configs/example/se.py --cpu-type=AtomicSimpleCPU --caches -c tests/test-progs/hello/bin/arm/linux/hello

Global frequency set at 1000000000000 ticks per second
warn: DRAM device capacity (8192 Mbytes) does not match the address range assigned (512 Mbytes)
0: system.remote_gdb: listening for remote gdb on port 7000
**** REAL SIMULATION ****
info: Entering event queue @ 0.  Starting simulation...
Hello world!
Exiting @ tick 2915000 because exiting with last active thread context #parathrw oti o atomic einai pio argos apo ton minor
Simulated exit code not 0! Exit code is 13

#4. ektelesi tou script se.py me HPI
chelakis@chelakis-VirtualBox ~/mygem5> 
./build/ARM/gem5.opt -d hw_se_HPI configs/example/se.py --cpu-type=HPI --caches -c  tests/test-progs/hello/bin/arm/linux/hello

#result
gem5 Simulator System.  http://gem5.org
gem5 is copyrighted software; use the --copyright option for details.

gem5 compiled Nov 19 2019 14:07:13
gem5 started Nov 23 2019 14:01:16
gem5 executing on chelakis-VirtualBox, pid 4928
command line: ./build/ARM/gem5.opt -d hw_se_HPI configs/example/se.py --cpu-type=HPI --caches -c tests/test-progs/hello/bin/arm/linux/hello

Global frequency set at 1000000000000 ticks per second
warn: DRAM device capacity (8192 Mbytes) does not match the address range assigned (512 Mbytes)
warn: No functional unit for OpClass SimdDiv 
#error dioti den exoun fortothei oi vivliothikes tou hpi
warn: No functional unit for OpClass SimdReduceAdd
warn: No functional unit for OpClass SimdReduceAlu
warn: No functional unit for OpClass SimdReduceCmp
warn: No functional unit for OpClass SimdFloatReduceAdd
warn: No functional unit for OpClass SimdFloatReduceCmp
warn: No functional unit for OpClass SimdAes
warn: No functional unit for OpClass SimdAesMix
warn: No functional unit for OpClass SimdSha1Hash
warn: No functional unit for OpClass SimdSha1Hash2
warn: No functional unit for OpClass SimdSha256Hash
warn: No functional unit for OpClass SimdSha256Hash2
warn: No functional unit for OpClass SimdShaSigma2
warn: No functional unit for OpClass SimdShaSigma3
warn: No functional unit for OpClass SimdPredAlu
0: system.remote_gdb: listening for remote gdb on port 7000
**** REAL SIMULATION ****
info: Entering event queue @ 0.  Starting simulation...
warn: CP14 unimplemented crn[14], opc1[7], crm[15], opc2[7]
Hello world!
Exiting @ tick 24688500 because exiting with last active thread context
Simulated exit code not 0! Exit code is 13

#5. ektelesi tou script se.py me timingSimpleCPU
chelakis@chelakis-VirtualBox ~/mygem5> 
./build/ARM/gem5.opt -d hw_se_timingsimple configs/example/se.py --cpu-type=TimingSimpleCPU --caches -c  tests/test-progs/hello/bin/arm/linux/hello

#result
gem5 Simulator System.  http://gem5.org
gem5 is copyrighted software; use the --copyright option for details.

gem5 compiled Nov 19 2019 14:07:13
gem5 started Nov 23 2019 14:05:44
gem5 executing on chelakis-VirtualBox, pid 23029
command line: ./build/ARM/gem5.opt -d hw_se_timingsimple configs/example/se.py --cpu-type=TimingSimpleCPU --caches -c tests/test-progs/hello/bin/arm/linux/hello

Global frequency set at 1000000000000 ticks per second
warn: DRAM device capacity (8192 Mbytes) does not match the address range assigned (512 Mbytes)
0: system.remote_gdb: listening for remote gdb on port 7000
**** REAL SIMULATION ****
info: Entering event queue @ 0.  Starting simulation...
Hello world!
Exiting @ tick 28667000 because exiting with last active thread context
Simulated exit code not 0! Exit code is 13

#6. ektelesi tou script se.py me minorCPU kai syxnothta 5ghz
chelakis@chelakis-VirtualBox ~/mygem5> 
./build/ARM/gem5.opt -d hw_se_minor_5ghz configs/example/se.py --cpu-type=MinorCPU --cpu-clock=5GHz  --caches -c  tests/test-progs/hello/bin/arm/linux/hello

#result
gem5 Simulator System.  http://gem5.org
gem5 is copyrighted software; use the --copyright option for details.

gem5 compiled Nov 19 2019 14:07:13
gem5 started Nov 23 2019 14:07:38
gem5 executing on chelakis-VirtualBox, pid 3634
command line: ./build/ARM/gem5.opt -d hw_se_minor_5ghz configs/example/se.py --cpu-type=MinorCPU --cpu-clock=5GHz --caches -c tests/test-progs/hello/bin/arm/linux/hello

Global frequency set at 1000000000000 ticks per second
warn: DRAM device capacity (8192 Mbytes) does not match the address range assigned (512 Mbytes)
0: system.remote_gdb: listening for remote gdb on port 7000
**** REAL SIMULATION ****
info: Entering event queue @ 0.  Starting simulation...
warn: CP14 unimplemented crn[14], opc1[7], crm[15], opc2[7]
Hello world!
Exiting @ tick 22607800 because exiting with last active thread context #pio grigoro apo to default
Simulated exit code not 0! Exit code is 13

#7. ektelesi tou script se.py me minorCPU kai syxnothta 400hz
chelakis@chelakis-VirtualBox ~/mygem5> 
./build/ARM/gem5.opt -d hw_se_minor_400 configs/example/se.py --cpu-type=MinorCPU --cpu-clock=400  --caches -c  tests/test-progs/hello/bin/arm/linux/hello

#result
gem5 Simulator System.  http://gem5.org
gem5 is copyrighted software; use the --copyright option for details.

gem5 compiled Nov 19 2019 14:07:13
gem5 started Nov 23 2019 14:08:09
gem5 executing on chelakis-VirtualBox, pid 3664
command line: ./build/ARM/gem5.opt -d hw_se_minor_400 configs/example/se.py --cpu-type=MinorCPU --cpu-clock=400 --caches -c tests/test-progs/hello/bin/arm/linux/hello

Global frequency set at 1000000000000 ticks per second
warn: DRAM device capacity (8192 Mbytes) does not match the address range assigned (512 Mbytes)
0: system.remote_gdb: listening for remote gdb on port 7000
**** REAL SIMULATION ****
info: Entering event queue @ 0.  Starting simulation...
warn: CP14 unimplemented crn[14], opc1[7], crm[15], opc2[7]
Hello world!
Exiting @ tick 26727500000000 because exiting with last active thread context #poly pio argo apo to default
Simulated exit code not 0! Exit code is 13

#8. entoli apeikonisis diathesimon memory type
chelakis@chelakis-VirtualBox ~/mygem5> 
./build/ARM/gem5.opt configs/example/se.py --list-mem-types

#result
gem5 Simulator System.  http://gem5.org
gem5 is copyrighted software; use the --copyright option for details.

gem5 compiled Nov 19 2019 14:07:13
gem5 started Nov 23 2019 14:12:02
gem5 executing on chelakis-VirtualBox, pid 3861
command line: ./build/ARM/gem5.opt configs/example/se.py --list-mem-types

Available AbstractMemory classes:
	HBM_1000_4H_1x128
	DRAMCtrl
	DDR3_2133_8x8
	HBM_1000_4H_1x64
	GDDR5_4000_2x32
	HMC_2500_1x32
	LPDDR3_1600_1x32
	WideIO_200_1x128
	QoSMemSinkCtrl
	DDR4_2400_8x8
	DDR3_1600_8x8
	DDR4_2400_4x16
	DDR4_2400_16x4
	SimpleMemory
	LPDDR2_S4_1066_1x32

#9. ektelesi tou script se.py me minorCPU kai memory ddr4
chelakis@chelakis-VirtualBox ~/mygem5>  
./build/ARM/gem5.opt -d hw_se_minor_ddr4 configs/example/se.py --cpu-type=MinorCPU --mem-type=DDR4_2400_8x8  --caches -c  tests/test-progs/hello/bin/arm/linux/hello

#result
gem5 Simulator System.  http://gem5.org
gem5 is copyrighted software; use the --copyright option for details.

gem5 compiled Nov 19 2019 14:07:13
gem5 started Nov 23 2019 14:13:34
gem5 executing on chelakis-VirtualBox, pid 3970
command line: ./build/ARM/gem5.opt -d hw_se_minor_ddr4 configs/example/se.py --cpu-type=MinorCPU --mem-type=DDR4_2400_8x8 --caches -c tests/test-progs/hello/bin/arm/linux/hello

Global frequency set at 1000000000000 ticks per second
warn: DRAM device capacity (16384 Mbytes) does not match the address range assigned (512 Mbytes) //vlepoume tin diaforetiki xwritikotita
0: system.remote_gdb: listening for remote gdb on port 7000
**** REAL SIMULATION ****
info: Entering event queue @ 0.  Starting simulation...
warn: CP14 unimplemented crn[14], opc1[7], crm[15], opc2[7]
Hello world!
Exiting @ tick 24855000 because exiting with last active thread context
Simulated exit code not 0! Exit code is 13

#10. ektelesi tou script se.py me minorCPU kai memory ddr3
chelakis@chelakis-VirtualBox ~/mygem5> 
./build/ARM/gem5.opt -d hw_se_minor_ddr3 configs/example/se.py --cpu-type=MinorCPU --mem-type=DDR3_1600_8x8  --caches -c  tests/test-progs/hello/bin/arm/linux/hello
#result
gem5 Simulator System.  http://gem5.org
gem5 is copyrighted software; use the --copyright option for details.

gem5 compiled Nov 19 2019 14:07:13
gem5 started Nov 23 2019 14:14:15
gem5 executing on chelakis-VirtualBox, pid 4012
command line: ./build/ARM/gem5.opt -d hw_se_minor_ddr3 configs/example/se.py --cpu-type=MinorCPU --mem-type=DDR3_1600_8x8 --caches -c tests/test-progs/hello/bin/arm/linux/hello

Global frequency set at 1000000000000 ticks per second
warn: DRAM device capacity (8192 Mbytes) does not match the address range assigned (512 Mbytes) //vlepoume tin diaforetiki xwritikotita
0: system.remote_gdb: listening for remote gdb on port 7000
**** REAL SIMULATION ****
info: Entering event queue @ 0.  Starting simulation...
warn: CP14 unimplemented crn[14], opc1[7], crm[15], opc2[7]
Hello world!
Exiting @ tick 25502000 because exiting with last active thread context
Simulated exit code not 0! Exit code is 13

