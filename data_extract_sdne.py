import pandas as pd
import numpy as np

def extract_hin2vec(filepath, first_tag, second_tag):
    names = ['node1_name', 'node2_name']
    pa = pd.read_csv(filepath, sep='\t', names=names)
    pa.insert(1, 'node1_type', first_tag)
    pa.insert(3, 'node2_type', second_tag)
    pa.insert(4, 'edge_type', first_tag + '-' + second_tag)

    pa_reverse = pd.read_csv(filepath, sep='\t', names=names)
    pa_reverse.rename(columns={names[0]: names[1], names[1]: names[0]}, inplace=True)
    pa_reverse.insert(1, 'node1_type', second_tag)
    pa_reverse.insert(3, 'node2_type', first_tag)
    pa_reverse.insert(4, 'edge_type', second_tag + '-' + first_tag)

    result = pd.concat([pa, pa_reverse], axis=0, sort=False)
    filepath = filepath.split('.txt')
    result.to_csv(filepath[0] + '_undirected_hin2vec.txt', header=False, index=False, sep='\t')

def extract_sdne(filepath):

    vertices = set()
    edges = set()
    with open(filepath, 'r') as f:
        for line in f.readlines():
            line = line.strip().split('\t')
            line = list(map(int, line))

            vertices.add(line[0])
            vertices.add(line[1])
    
    index2ver = dict()
    ver2index = dict()
    vertices = sorted(vertices)
    for i, v in enumerate(vertices):
        index2ver[i] = v
        ver2index[v] = i
    
    lines = []
    with open(filepath, 'r') as f:
        for line in f.readlines():
            line = line.strip().split('\t')
            line = list(map(int, line))
            line = [ver2index[line[0]], ver2index[line[1]]]
            lines.append(line)

            # edges comput
            first_order = (line[0], line[1])
            second_order = (line[1], line[0])
            if first_order not in edges and second_order not in edges:
                edges.add(first_order)

    df = pd.DataFrame(np.array(lines))
    dest_filepath = 'sdne_' + filepath
    df.to_csv(dest_filepath, header=False, index=False, sep='\t')
    print('file : {}, vertices : {}, edges : {}'.format(dest_filepath, len(vertices), len(edges)))

if __name__ == '__main__':
    filepaths = [
        'paper_author.txt',
        'paper_conf.txt',
        'paper_term.txt'
    ]
    for filepath in filepaths:
        extract_sdne(filepath)
