import pandas as pd

# xintong
# def line(filepath):
#     names = ['node1_name', 'node2_name']
#     pa = pd.read_csv(filepath, sep='\t', names=names)

#     pa_reverse = pd.read_csv(filepath, sep='\t', names=names)
#     pa_reverse.rename(columns={'node1_name': 'node2_name', 'node2_name': 'node1_name'}, inplace=True)

#     result = pd.concat([pa, pa_reverse], axis=0, sort=False)
#     result.to_csv(filepath.split('.txt')[0] + '_undirected_line.txt', header=False, index=False, sep='\t')

# def line_sum(filepaths):
#     names = ['node1_name', 'node2_name']
#     filepaths = list(map(lambda x: x.split('.txt')[0] + '_undirected_line.txt', filepaths))
#     pd1 = pd.read_csv(filepaths[0], sep='\t', names=names)
#     pd2 = pd.read_csv(filepaths[1], sep='\t', names=names)
#     pd3 = pd.read_csv(filepaths[2], sep='\t', names=names)

#     result = pd.concat([pd1, pd2, pd3], names=names)
#     result.to_csv('line_sum.txt', header=False, index=False, sep='\t')

# if __name__ == '__main__':
#     filepaths = [
#         './paper_author.txt',
#         './paper_conf.txt',
#         './paper_term.txt'
#     ]
#     for filepath in filepaths:
#         line(filepath)
#     line_sum(filepaths)
#     print('ok')




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


if __name__ == '__main__':
    file_tags = [
        ['./paper_author.txt', 'P', 'A'],
        ['./paper_conf.txt', 'P', 'C'],
        ['./paper_term.txt', 'P', 'T']
    ]
    for file_tag in file_tags:
        extract_hin2vec(file_tag[0], file_tag[1], file_tag[2])
