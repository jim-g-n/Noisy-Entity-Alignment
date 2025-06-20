import random
import argparse

parser = argparse.ArgumentParser(description='dirty_data_creation')
parser.add_argument('--error_rate', type=float, default=0)
parser.add_argument('--rel_file', type=str)
args = parser.parse_args()
error_rate = args.error_rate
rel_file = args.rel_file

def loadentfile(fn, num=3):
	print('loading a file...' + fn)
	ret = []
	with open(fn, encoding='utf-8') as f:
		for line in f:
			th = line[:-1].split('\t')
			x = []
			for i in range(num):
				x.append(th[i])
			ret.append(tuple(x))
	return ret

all_triples = loadentfile(rel_file)
all_ents = list(set([x[0] for x in all_triples] + [x[2] for x in all_triples]))
to_make_noisy = random.sample(all_triples, round(error_rate*(len(all_triples))))
updated_triples = [x for x in all_triples if x not in to_make_noisy]

for i in range(len(to_make_noisy)):
    updated_triples.append((to_make_noisy[i][0],to_make_noisy[i][1],random.choice(all_ents)))

with open(rel_file + '_' + str(int(error_rate*100)), 'w') as fp:
    fp.write('\n'.join('%s\t%s\t%s' % x for x in updated_triples))