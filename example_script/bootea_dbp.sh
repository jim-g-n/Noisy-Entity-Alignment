#!/bin/bash -l
for align_error in 0 10 20 30 40 50
do
    for source_error in 0 10 20 30 40
    do
        for target_error in 0 10 20 30 40
        do
            conda run -p /home/user/anaconda3/envs/openea --cwd /home/user/OpenEA/run python main_from_args.py ./args/bootea_args_15K.json DBP15K 0_3/ $align_error $source_error $target_error > "bootea_dbp_3_${align_error}_${source_error}_${target_error}.txt"
        done
    done
done
