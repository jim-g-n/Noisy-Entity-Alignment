# Knowledge Graphs in the Real-World: Noisy Data and Embedding-Based Entity Alignment Algorithms

This repository contains the code and data used for performing the experiments and analysis in the paper "Knowledge Graphs in the Real-World: Noisy Data and Embedding-Based Entity Alignment Algorithms".

There are four folders in this repo:
1. `datasets`: Contains the Python scripts used in creating the noisy data used. Also included are links to the original data and the noisy versions used in our experiments.
2. `analysis`: Contains the core results (performance and timing) as text files and Jupyter notebooks for recreating the analysis in the paper. Also included is a link to the full, unprocessed results.
3. `environments`: Contains Python package lists for all steps in the experimentation process.
4. `example_scripts`: Contains scripts that can be used for performing the experiments. This can be adjusted based on which algorithms/datasets one wishes to test.

## Recreating Experiments

The experiments rely on an updated version of the OpenEA library (https://github.com/jim-g-n/OpenEA). Users can follow the instructions there for installing this updated version. Following that, the noisy datasets can be downloaded from [Google Drive](https://drive.google.com/drive/folders/1e2NlKGHGvcHPG7FDIPz_aGCRt19DLdP7?usp=drive_link). These data should be placed in the folder named _datasets_ in the same location as the OpenEA files.

If users have installed OpenEA as described in the associated repo, a single experiment on _dataset-name_ using _algorithm-name_ with a training size of _X_*10%, _seed-perc_ seed alignment noise, _source-perc_ source triple noise, and _target-perc_ target triple noise can be run as follows:

```bash
conda activate openea
cd OpenEA/run
python main_from_args.py ./args/algorithm-name_args_15K.json dataset-name 0_X/ seed-perc source-perc target-perc
```


