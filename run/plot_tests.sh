#!/bin/bash

set -x

n_bod=100000
n_it=1000000
out_int=500
out_dir=sim_plot
sensei_int=500
part_int=100

n_node=${SLURM_JOB_NUM_NODES}
n_dev=4
n_dev_tot=`echo ${n_dev}*${n_node} | bc`
rank_per_dev=1


echo "**********************************************************************************"
sensei_xml=data_binning_plot.xml
n=`echo ${n_dev_tot}*${rank_per_dev} | bc`
tasks=`echo ${n_dev}*${rank_per_dev} | bc`
sim_dev=${n_dev}

time srun -N ${n_node} -G ${n_dev_tot} -n ${n} --tasks-per-node ${tasks}  ./newtonpp_nv_omp \
    --n_bodies ${n_bod} --n_its ${n_it} --out_int ${out_int} --out_dir ${out_dir} \
    --sensei_xml ${sensei_xml} --sensei_int ${sensei_int} --part_int ${part_int} \
    --num_devs ${sim_dev} --dt 1e4
