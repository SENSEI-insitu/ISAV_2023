#!/bin/bash

# module load cmake
# module swap PrgEnv-gnu PrgEnv-nvidia
# module swap gpu cpu
# module swap nvidia/22.7 nvidia/23.1

set -x

rm -rfI /pscratch/sd/l/loring/sensei-install-nvhpc_cuda_omp/*


cmake -DCMAKE_CXX_COMPILER=`which nvc++` \
    -DSENSEI_ENABLE_PYTHON=OFF \
    -DBUILD_TESTING=ON -DCMAKE_BUILD_TYPE=Release \
    -DSENSEI_ENABLE_CUDA=ON -DSENSEI_ENABLE_OPENMP=ON \
    -DSENSEI_CUDA_ARCHITECTURES=80 \
    -DSENSEI_OPENMP_ARCH=cc80 -DCMAKE_CUDA_ARCHITECTURES=80 \
    -DCMAKE_INSTALL_PREFIX=/pscratch/sd/l/loring/sensei-install-nvhpc_cuda_omp \
    ../SENSEI

make -j10
make -j10 install
