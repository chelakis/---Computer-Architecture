./build/ARM/gem5.opt -d spec_results/final_results/default configs/example/se.py --cpu-type=MinorCPU --caches --l2cache --l1d_size=64kB --l1i_size=32kB --l2_size=2048kB --l1i_assoc=2 --l1d_assoc=2 --l2_assoc=8 --cacheline_size=64 -c spec_cpu2006/401.bzip2/src/specbzip -o "spec_cpu2006/401.bzip2/data/input.program 10" -I 100000000

./build/ARM/gem5.opt -d spec_results/final_results/l2size_512 configs/example/se.py --cpu-type=MinorCPU --caches --l2cache --l1d_size=64kB --l1i_size=32kB --l2_size=512kB --l1i_assoc=2 --l1d_assoc=2 --l2_assoc=8 --cacheline_size=64 -c spec_cpu2006/401.bzip2/src/specbzip -o "spec_cpu2006/401.bzip2/data/input.program 10" -I 100000000

./build/ARM/gem5.opt -d spec_results/final_results/l2size_1024 configs/example/se.py --cpu-type=MinorCPU --caches --l2cache --l1d_size=64kB --l1i_size=32kB --l2_size=1024kB --l1i_assoc=2 --l1d_assoc=2 --l2_assoc=8 --cacheline_size=64 -c spec_cpu2006/401.bzip2/src/specbzip -o "spec_cpu2006/401.bzip2/data/input.program 10" -I 100000000

./build/ARM/gem5.opt -d spec_results/final_results/l2size_4096 configs/example/se.py --cpu-type=MinorCPU --caches --l2cache --l1d_size=64kB --l1i_size=32kB --l2_size=512kB --l1i_assoc=2 --l1d_assoc=2 --l2_assoc=8 --cacheline_size=64 -c spec_cpu2006/401.bzip2/src/specbzip -o "spec_cpu2006/401.bzip2/data/input.program 10" -I 100000000

./build/ARM/gem5.opt -d spec_results/final_results/l1size_1632 configs/example/se.py --cpu-type=MinorCPU --caches --l2cache --l1d_size=32kB --l1i_size=16kB --l2_size=2048kB --l1i_assoc=2 --l1d_assoc=2 --l2_assoc=8 --cacheline_size=64 -c spec_cpu2006/401.bzip2/src/specbzip -o "spec_cpu2006/401.bzip2/data/input.program 10" -I 100000000

./build/ARM/gem5.opt -d spec_results/final_results/l1size_64128 configs/example/se.py --cpu-type=MinorCPU --caches --l2cache --l1d_size=128kB --l1i_size=64kB --l2_size=2048kB --l1i_assoc=2 --l1d_assoc=2 --l2_assoc=8 --cacheline_size=64 -c spec_cpu2006/401.bzip2/src/specbzip -o "spec_cpu2006/401.bzip2/data/input.program 10" -I 100000000

./build/ARM/gem5.opt -d spec_results/final_results/l1assoc1 configs/example/se.py --cpu-type=MinorCPU --caches --l2cache --l1d_size=64kB --l1i_size=32kB --l2_size=2048kB --l1i_assoc=1 --l1d_assoc=1 --l2_assoc=8 --cacheline_size=64 -c spec_cpu2006/401.bzip2/src/specbzip -o "spec_cpu2006/401.bzip2/data/input.program 10" -I 100000000

./build/ARM/gem5.opt -d spec_results/final_results/l1assoc4 configs/example/se.py --cpu-type=MinorCPU --caches --l2cache --l1d_size=64kB --l1i_size=32kB --l2_size=2048kB --l1i_assoc=4 --l1d_assoc=4 --l2_assoc=8 --cacheline_size=64 -c spec_cpu2006/401.bzip2/src/specbzip -o "spec_cpu2006/401.bzip2/data/input.program 10" -I 100000000

./build/ARM/gem5.opt -d spec_results/final_results/l1assoc8 configs/example/se.py --cpu-type=MinorCPU --caches --l2cache --l1d_size=64kB --l1i_size=32kB --l2_size=2048kB --l1i_assoc=8 --l1d_assoc=8 --l2_assoc=8 --cacheline_size=64 -c spec_cpu2006/401.bzip2/src/specbzip -o "spec_cpu2006/401.bzip2/data/input.program 10" -I 100000000

./build/ARM/gem5.opt -d spec_results/final_results/l2assoc2 configs/example/se.py --cpu-type=MinorCPU --caches --l2cache --l1d_size=64kB --l1i_size=32kB --l2_size=2048kB --l1i_assoc=1 --l1d_assoc=1 --l2_assoc=2 --cacheline_size=64 -c spec_cpu2006/401.bzip2/src/specbzip -o "spec_cpu2006/401.bzip2/data/input.program 10" -I 100000000

./build/ARM/gem5.opt -d spec_results/final_results/l2assoc4 configs/example/se.py --cpu-type=MinorCPU --caches --l2cache --l1d_size=64kB --l1i_size=32kB --l2_size=2048kB --l1i_assoc=1 --l1d_assoc=1 --l2_assoc=4 --cacheline_size=64 -c spec_cpu2006/401.bzip2/src/specbzip -o "spec_cpu2006/401.bzip2/data/input.program 10" -I 100000000

./build/ARM/gem5.opt -d spec_results/final_results/l2assoc16 configs/example/se.py --cpu-type=MinorCPU --caches --l2cache --l1d_size=64kB --l1i_size=32kB --l2_size=2048kB --l1i_assoc=1 --l1d_assoc=1 --l2_assoc=16 --cacheline_size=64 -c spec_cpu2006/401.bzip2/src/specbzip -o "spec_cpu2006/401.bzip2/data/input.program 10" -I 100000000

./build/ARM/gem5.opt -d spec_results/final_results/line16 configs/example/se.py --cpu-type=MinorCPU --caches --l2cache --l1d_size=64kB --l1i_size=32kB --l2_size=2048kB --l1i_assoc=1 --l1d_assoc=1 --l2_assoc=8 --cacheline_size=16 -c spec_cpu2006/401.bzip2/src/specbzip -o "spec_cpu2006/401.bzip2/data/input.program 10" -I 100000000

./build/ARM/gem5.opt -d spec_results/final_results/line32 configs/example/se.py --cpu-type=MinorCPU --caches --l2cache --l1d_size=64kB --l1i_size=32kB --l2_size=2048kB --l1i_assoc=1 --l1d_assoc=1 --l2_assoc=8 --cacheline_size=32 -c spec_cpu2006/401.bzip2/src/specbzip -o "spec_cpu2006/401.bzip2/data/input.program 10" -I 100000000

./build/ARM/gem5.opt -d spec_results/final_results/line128 configs/example/se.py --cpu-type=MinorCPU --caches --l2cache --l1d_size=64kB --l1i_size=32kB --l2_size=2048kB --l1i_assoc=1 --l1d_assoc=1 --l2_assoc=8 --cacheline_size=128 -c spec_cpu2006/401.bzip2/src/specbzip -o "spec_cpu2006/401.bzip2/data/input.program 10" -I 100000000
