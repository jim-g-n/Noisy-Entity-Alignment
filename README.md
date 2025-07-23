# Knowledge Graphs in the Real-World: Noisy Data and Embedding-Based Entity Alignment Algorithms

This repository contains the code and data used for performing the experiments and analysis in the paper "Knowledge Graphs in the Real-World: Noisy Data and Embedding-Based Entity Alignment Algorithms".

There are four folders in this repo:
1. `datasets`: Contains the Python scripts used in creating the noisy data used. Also included are links to the original data and the noisy versions used in our experiments.
2. `analysis`: Contains the core results (performance and timing) as text files and Jupyter notebooks for recreating the analysis in the paper. Also included is a link to the full, unprocessed results.
3. `environments`: Contains Python package lists for all steps in the experimentation process.
4. `example_scripts`: Contains scripts that can be used for performing the experiments. This can be adjusted based on which algorithms/datasets one wishes to test.

## Recreating Experiments

The experiments rely on an updated version of the OpenEA library (https://anonymous.4open.science/r/OpenEA-6F3C/README.md). Users can follow the instructions there for installing this updated version. Following that, the noisy datasets can be downloaded from [figshare](https://figshare.com/s/ba4dc2a7f95261593e94). These data should be placed in the folder named _datasets_ in the same location as the OpenEA files. Relational triples files can be copied from the relevant folder. 

If users have installed OpenEA as described in the associated repo, a single experiment on _dataset-name_ using _algorithm-name_ with a training size of _X_*10%, _seed-perc_ seed alignment noise, _source-perc_ source triple noise, and _target-perc_ target triple noise can be run as follows:

```bash
conda activate openea
cd OpenEA/run
python main_from_args.py ./args/algorithm-name_args_15K.json dataset-name 0_X/ seed-perc source-perc target-perc
```

Users can change the scripts found in the `example_scripts` folder to run multiple experiments. For example, the `gcn_ids.sh` bash script will run all GCN-Align experiments on IDS15K. Simply changing either the args or dataset in this script will allow for running experiments on other algorithms and datasets. To test the different negative sampling methods, simply copy the `rel_triples_x` files from the relevant folders in the datasets.
