import os
import pandas as pd
from scipy.stats import fisher_exact


experiments = []


def create_subject():
    table = pd.read_table('geneName.txt')['Unknown']
    subject = gene_list.value_counts().index.tolist()[1:]
    return subject

def create_gene_sets():
    gene_sets = []
    for f in os.listdir('data'):
        if f.endswith('.txt'):
            gene_sets.append(f)
    return gene_sets

def create_gene_set(set_name):
    with open('data/' + set_name) as f:
        gene_set= f.readlines()
    return [line.strip() for line in gene_set]


def create_all_genes():
    with open('all') as f:
        all_genes = f.readlines()
    return [line.strip() for line in all_genes]


def contingency_matrix(subject, gene_set, all_genes):
    a, b, c, d = [], [], [], []
    for gene in subject:
        if gene in gene_set:
            a.append(gene)
        else:
            b.append(gene)
    for gene in gene_set:
        if gene not in subject:
            c.append(gene)
    for gene in all_genes:
        if gene not in subject and gene not in gene_set:
            d.append(gene)
    return a, b, c, d


subject = create_subject()
gene_sets = create_gene_sets()
all_genes = create_all_genes()


for set_name in gene_sets:
    experiment = []
    gene_set = create_gene_set(set_name)
    title = gene_set[0]
    description = gene_set[1]
    genes = gene_set[2:]
    a, b, c, d = contingency_matrix(subject, genes, all_genes)
    experiment.append(title) # 0
    experiment.append(description) # 1
    experiment.append([[a, b], [c, d]]) # 2
    experiment.append([[len(a), len(b)], [len(c), len(d)]]) # 3
    oddsratio, p_value = fisher_exact(experiment[3])
    experiment.append(p_value) # 4
    #print('Genes in subject and in gene set:', len(a))
    #print('Genes in subject and not in gene set:', len(b))
    #print('Genes not in subject and in gene set:', len(c))
    #print('Genes not in subject and not in gene set:', len(d))
    experiments.append(experiment)

