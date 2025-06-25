## Data

This folder contains the code used to create the noisy data. The two original datasets are IDS15K (OpenEA: https://github.com/nju-websoft/OpenEA) [1] and DBP15K (JAPE: https://github.com/nju-websoft/JAPE) [2].

The `create_dirty_align_data.py` file takes as input training size and a list of error rates, and produces a set of (dirty) training and test data based on an `ent_links` file. The `create_dirty_triple_.py` files take as input a relational triple filename and error rates to produce dirty triples. Additionally, the `process_dbp_attr.py` file converts the original versions of the attributes files for the DBP15K dataset to a format useable by OpenEA.

The data used in our experiments are available to download at: https://drive.google.com/drive/folders/1e2NlKGHGvcHPG7FDIPz_aGCRt19DLdP7?usp=sharing

#### References

[1] Sun, Z., Zhang, Q., Hu, W., Wang, C., Chen, M., Akrami, F. and Li, C., 2020. A benchmarking study of embedding-based entity alignment for knowledge graphs. arXiv preprint arXiv:2003.07743.

[2] Sun, Z., Hu, W. and Li, C., 2017, October. Cross-lingual entity alignment via joint attribute-preserving embedding. In International semantic web conference (pp. 628-644). Cham: Springer International Publishing.
