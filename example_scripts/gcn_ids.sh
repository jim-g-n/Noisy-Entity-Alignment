#!/bin/bash -l
for align_error in 0 10 20 30 40 50
do
    for source_error in 0 10 20 30 40
    do
        for target_error in 0 10 20 30 40
        do
            conda run -p /home/user/anaconda3/envs/openea --cwd /home/user/OpenEA/run python main_from_args.py ./args/gcnalign_args_15K.json IDS15K 0_1/ $align_error $source_error $target_error > "gcnalign_ids_1_${align_error}_${source_error}_${target_error}.txt"
        done
    done
done
for align_error in 0 10 20 30 40 50
do
    for source_error in 0 10 20 30 40
    do
        for target_error in 0 10 20 30 40
        do
            conda run -p /home/user/anaconda3/envs/openea --cwd /home/user/OpenEA/run python main_from_args.py ./args/gcnalign_args_15K.json IDS15K 0_2/ $align_error $source_error $target_error > "gcnalign_ids_2_${align_error}_${source_error}_${target_error}.txt"
        done
    done
done
for align_error in 0 10 20 30 40 50
do
    for source_error in 0 10 20 30 40
    do
        for target_error in 0 10 20 30 40
        do
            conda run -p /home/user/anaconda3/envs/openea --cwd /home/user/OpenEA/run python main_from_args.py ./args/gcnalign_args_15K.json IDS15K 0_3/ $align_error $source_error $target_error > "gcnalign_ids_3_${align_error}_${source_error}_${target_error}.txt"
        done
    done
done
for align_error in 0 10 20 30 40 50
do
    for source_error in 0 10 20 30 40
    do
        for target_error in 0 10 20 30 40
        do
            conda run -p /home/user/anaconda3/envs/openea --cwd /home/user/OpenEA/run python main_from_args.py ./args/gcnalign_args_15K.json IDS15K 0_4/ $align_error $source_error $target_error > "gcnalign_ids_4_${align_error}_${source_error}_${target_error}.txt"
        done
    done
done
for align_error in 0 10 20 30 40 50
do
    for source_error in 0 10 20 30 40
    do
        for target_error in 0 10 20 30 40
        do
            conda run -p /home/user/anaconda3/envs/openea --cwd /home/user/OpenEA/run python main_from_args.py ./args/gcnalign_args_15K.json IDS15K 0_5/ $align_error $source_error $target_error > "gcnalign_ids_5_${align_error}_${source_error}_${target_error}.txt"
        done
    done
done
