import argparse
import pandas as pd
import numpy as np
from torchkge.sampling import PositionalNegativeSampler
from torchkge.data_structures import KnowledgeGraph

parser = argparse.ArgumentParser(description='dirty_data_creation')
parser.add_argument('-error_rates', '--error_rates', nargs='+', default=[0])
parser.add_argument('--rel_file', type=str)
args = parser.parse_args()
error_rates = args.error_rates
rel_file = args.rel_file

rel_triples = pd.read_csv(rel_file, sep='\t', header = None)
rel_triples.columns = ['from', 'rel', 'to']
rel_triples = rel_triples[['from', 'to', 'rel']]

kg = KnowledgeGraph(rel_triples)
sampler = PositionalNegativeSampler(kg)
n_h, n_t = sampler.corrupt_batch(kg.head_idx, kg.tail_idx, kg.relations)

for error_rate in error_rates:
    error_rate = float(error_rate)
    change_ids = np.random.choice(len(kg), round(error_rate*(len(kg))), replace=False)
    new_head = kg.head_idx.detach().clone()
    new_tail = kg.tail_idx.detach().clone()
    
    new_head[change_ids] = n_h[change_ids]
    new_tail[change_ids] = n_t[change_ids]

    new_triples = KnowledgeGraph(kg={'heads':new_head, 'tails':new_tail, 'relations':kg.relations},ent2ix=kg.ent2ix,rel2ix=kg.rel2ix).get_df()
    new_triples[['from', 'rel', 'to']].to_csv(rel_file + '_' + str(int(error_rate*100)), sep='\t', header=False, index=False)