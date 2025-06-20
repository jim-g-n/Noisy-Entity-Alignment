import random
import argparse

parser = argparse.ArgumentParser(description='dirty_data_creation')
parser.add_argument('--training_size', type=float, default=0.3)
parser.add_argument('-error_rates', '--error_rates', nargs='+', default=[0])
args = parser.parse_args()
training_size = args.training_size
error_rates = args.error_rates

def loadentfile(fn, num=2):
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

all_aligned_ent = loadentfile('ent_links', 2)

ents_1 = [x[0] for x in all_aligned_ent]
ents_2 = [x[1] for x in all_aligned_ent]

clean_training = random.sample(all_aligned_ent, round(training_size*(len(all_aligned_ent))))
clean_testing = [x for x in all_aligned_ent if x not in clean_training]

with open('./0_' + str(int(10*training_size)) + '/test_links', 'w') as fp:
    fp.write('\n'.join('%s\t%s' % x for x in clean_testing))

for error_rate in error_rates:
    error_rate = float(error_rate)

    to_misalign = random.sample(clean_training, round(error_rate*(len(clean_training))))
    updated_training = [x for x in clean_training if x not in to_misalign]

    for i in range(len(to_misalign)):
        if i%2==0:
            updated_training.append((to_misalign[i][0],random.choice(ents_2)))
        else:
            updated_training.append((random.choice(ents_1),to_misalign[i][1]))

    with open('./0_' + str(int(10*training_size)) + '/train_links_' + str(int(error_rate*100)), 'w') as fp:
        fp.write('\n'.join('%s\t%s' % x for x in updated_training))