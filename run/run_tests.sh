#!/bin/bash

set -x

n_bod=24000000
n_it=10
out_int=0
out_dir=sim_out
sensei_int=1
part_int=1000000

n_node=${SLURM_JOB_NUM_NODES}
n_dev=4
n_dev_tot=`echo ${n_dev}*${n_node} | bc`

echo "**********************************************************************************"
sensei_xml=data_binning_sync_host.xml
rank_per_dev=1
n=`echo ${n_dev_tot}*${rank_per_dev} | bc`
tasks=`echo ${n_dev}*${rank_per_dev} | bc`
sim_dev=${n_dev}

time srun -N ${n_node} -G ${n_dev_tot} -n ${n} --tasks-per-node ${tasks}  ./newtonpp_nv_omp \
    --n_bodies ${n_bod} --n_its ${n_it} --out_int ${out_int} --out_dir ${out_dir} \
    --sensei_xml ${sensei_xml} --sensei_int ${sensei_int} --part_int ${part_int} \
    --num_devs ${sim_dev}

echo "**********************************************************************************"
sensei_xml=data_binning_sync_matched.xml
rank_per_dev=1
n=`echo ${n_dev_tot}*${rank_per_dev} | bc`
tasks=`echo ${n_dev}*${rank_per_dev} | bc`
sim_dev=${n_dev}

time srun -N ${n_node} -G ${n_dev_tot} -n ${n} --tasks-per-node ${tasks}  ./newtonpp_nv_omp \
    --n_bodies ${n_bod} --n_its ${n_it} --out_int ${out_int} --out_dir ${out_dir} \
    --sensei_xml ${sensei_xml} --sensei_int ${sensei_int} --part_int ${part_int} \
    --num_devs ${sim_dev}

echo "**********************************************************************************"
sensei_xml=data_binning_sync_1dev.xml
rank_per_dev=1
sim_dev=`echo ${n_dev}-1 | bc`
n=`echo ${n_node}*${sim_dev}*${rank_per_dev} | bc`
tasks=`echo ${sim_dev}*${rank_per_dev} | bc`

time srun -N ${n_node} -G ${n_dev_tot} -n ${n} --tasks-per-node ${tasks}  ./newtonpp_nv_omp \
    --n_bodies ${n_bod} --n_its ${n_it} --out_int ${out_int} --out_dir ${out_dir} \
    --sensei_xml ${sensei_xml} --sensei_int ${sensei_int} --part_int ${part_int} \
    --num_devs ${sim_dev}

echo "**********************************************************************************"
sensei_xml=data_binning_sync_2dev.xml
rank_per_dev=1
sim_dev=`echo ${n_dev}-2 | bc`
n=`echo ${n_node}*${sim_dev}*${rank_per_dev} | bc`
tasks=`echo ${sim_dev}*${rank_per_dev} | bc`

time srun -N ${n_node} -G ${n_dev_tot} -n ${n} --tasks-per-node ${tasks}  ./newtonpp_nv_omp \
    --n_bodies ${n_bod} --n_its ${n_it} --out_int ${out_int} --out_dir ${out_dir} \
    --sensei_xml ${sensei_xml} --sensei_int ${sensei_int} --part_int ${part_int} \
    --num_devs ${sim_dev}


echo "**********************************************************************************"



echo "**********************************************************************************"
sensei_xml=data_binning_async_host.xml
rank_per_dev=1
n=`echo ${n_dev_tot}*${rank_per_dev} | bc`
tasks=`echo ${n_dev}*${rank_per_dev} | bc`
sim_dev=${n_dev}

time srun -N ${n_node} -G ${n_dev_tot} -n ${n} --tasks-per-node ${tasks}  ./newtonpp_nv_omp \
    --n_bodies ${n_bod} --n_its ${n_it} --out_int ${out_int} --out_dir ${out_dir} \
    --sensei_xml ${sensei_xml} --sensei_int ${sensei_int} --part_int ${part_int} \
    --num_devs ${sim_dev}

echo "**********************************************************************************"
sensei_xml=data_binning_async_matched.xml
rank_per_dev=1
n=`echo ${n_dev_tot}*${rank_per_dev} | bc`
tasks=`echo ${n_dev}*${rank_per_dev} | bc`
sim_dev=${n_dev}

time srun -N ${n_node} -G ${n_dev_tot} -n ${n} --tasks-per-node ${tasks}  ./newtonpp_nv_omp \
    --n_bodies ${n_bod} --n_its ${n_it} --out_int ${out_int} --out_dir ${out_dir} \
    --sensei_xml ${sensei_xml} --sensei_int ${sensei_int} --part_int ${part_int} \
    --num_devs ${sim_dev}

echo "**********************************************************************************"
sensei_xml=data_binning_async_1dev.xml
rank_per_dev=1
sim_dev=`echo ${n_dev}-1 | bc`
n=`echo ${n_node}*${sim_dev}*${rank_per_dev} | bc`
tasks=`echo ${sim_dev}*${rank_per_dev} | bc`

time srun -N ${n_node} -G ${n_dev_tot} -n ${n} --tasks-per-node ${tasks}  ./newtonpp_nv_omp \
    --n_bodies ${n_bod} --n_its ${n_it} --out_int ${out_int} --out_dir ${out_dir} \
    --sensei_xml ${sensei_xml} --sensei_int ${sensei_int} --part_int ${part_int} \
    --num_devs ${sim_dev}

echo "**********************************************************************************"
sensei_xml=data_binning_async_2dev.xml
rank_per_dev=1
sim_dev=`echo ${n_dev}-2 | bc`
n=`echo ${n_node}*${sim_dev}*${rank_per_dev} | bc`
tasks=`echo ${sim_dev}*${rank_per_dev} | bc`

time srun -N ${n_node} -G ${n_dev_tot} -n ${n} --tasks-per-node ${tasks}  ./newtonpp_nv_omp \
    --n_bodies ${n_bod} --n_its ${n_it} --out_int ${out_int} --out_dir ${out_dir} \
    --sensei_xml ${sensei_xml} --sensei_int ${sensei_int} --part_int ${part_int} \
    --num_devs ${sim_dev}
