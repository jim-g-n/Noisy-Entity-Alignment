#!/bin/bash -l
python create_dirty_triple_data.py --error_rate 0.1 --rel_file rel_triples_1
python create_dirty_triple_data.py --error_rate 0.2 --rel_file rel_triples_1
python create_dirty_triple_data.py --error_rate 0.3 --rel_file rel_triples_1
python create_dirty_triple_data.py --error_rate 0.4 --rel_file rel_triples_1
python create_dirty_triple_data.py --error_rate 0.1 --rel_file rel_triples_2
python create_dirty_triple_data.py --error_rate 0.2 --rel_file rel_triples_2
python create_dirty_triple_data.py --error_rate 0.3 --rel_file rel_triples_2
python create_dirty_triple_data.py --error_rate 0.4 --rel_file rel_triples_2