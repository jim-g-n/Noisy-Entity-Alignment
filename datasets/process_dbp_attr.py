def update_attr(file_name):
    with open(file_name) as file:
        lines = [line.rstrip() for line in file]
    upd_attr = []
    for line in lines:
        triple = line[1:-2]
        triple = triple.replace('> <', '\t')
        triple = triple.replace('> "', '\t"')
        upd_attr.append(triple)
    return upd_attr

upd_attr = update_attr('attr_triples_1')
with open('upd_attr_1', mode='wt', encoding='utf-8') as myfile:
    myfile.write('\n'.join(upd_attr))

upd_attr = update_attr('attr_triples_2')
with open('upd_attr_2', mode='wt', encoding='utf-8') as myfile:
    myfile.write('\n'.join(upd_attr))