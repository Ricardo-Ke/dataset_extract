import pandas as pd
import numpy as np
import re
import os
import json

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
    
    whitespace_or_tab = filepath.find('BlogCatalog') > -1 or filepath.find('hetrec') > -1 or filepath.find('YELP') > -1
    # with open(filepath, 'r') as f:
    # for line in f.readlines():
    for line in open(filepath, 'r'):
        line = line.strip()
        if whitespace_or_tab:
            # regex = re.compile('\s+')
            # line = regex.split(line)
            line = line.split()
        else:
            line = line.split('\t')
            line = [line[0], line[1]]
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
    # with open(filepath, 'r') as f:
    for line in open(filepath, 'r'):
        line = line.strip()
        if whitespace_or_tab:
            # regex = re.compile('\s+')
            # line = regex.split(line)
            line = line.split()
        else:
            line = line.strip().split('\t')
            line = [line[0], line[1]]
        line = list(map(int, line))

        line = [ver2index[line[0]], ver2index[line[1]]]
        lines.append(line)

        # edges comput
        first_order = (line[0], line[1])
        second_order = (line[1], line[0])
        if first_order not in edges and second_order not in edges:
            edges.add(first_order)

    if not os.path.exists('./sdne'):
        os.mkdir('./sdne')
    df = pd.DataFrame(np.array(lines))
    dest_filepath = 'sdne/sdne_' + filepath.split('/')[-1]
    # df.to_csv(dest_filepath, header=False, index=False, sep='\t')

    dest_index2ver_filepath = dest_filepath.split('.txt')[0] + '_index2ver.txt'
    with open(dest_index2ver_filepath, 'w') as fout:
        json.dump(index2ver, fout)

    print('file : {}, vertices : {}, edges : {}'.format(dest_filepath, len(vertices), len(edges)))
    print('序列化为 {}'.format(dest_index2ver_filepath))
if __name__ == '__main__':
    filepaths = [
        # 'paper_author.txt',
        # 'paper_conf.txt',
        # 'paper_term.txt'
        './BlogCatalog-dataset/blogcatalog/blogcatalog_edges.txt',
        './dblp/AA.txt',
        './hetrec2011/IMDB/movie_MM.txt',
        './YELP/res_res.txt'
    ]
    for filepath in filepaths:
        extract_sdne(filepath)
