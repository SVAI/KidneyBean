## Convenience functions wrapping the pipeline and incorporating geneName.txt

import pdb
# from matplotlib import pyplot as plt
# import sys
import pandas as pd
import numpy as np

from gene_to_drug import gene_to_drug
from drug_to_effect import get_gene_drug_risks

gn_path = "/tmp/kidneybean/data/geneName.txt"

df = pd.read_csv(gn_path, sep="\t", header=None, names=["index", "gene"])
df = df.drop_duplicates(subset='gene')

N = 3
res = []

for gene in df['gene']:
    if gene == 'Unknown': continue

    # print(gene)
    # drugs = gene_to_drug(gene)
    # if len(drugs) == 0:
        # print("no drugs found for gene {}".format(gene))
    # else:
        # print("{} drugs found for gene {}".format(len(drugs), gene))
 
    eff = get_gene_drug_risks(gene)
    if len(eff) == 0:
        print("no drugs found for gene {}".format(gene))
        continue
    else:
        print("{} drugs found for gene {}".format(len(eff), gene))

    res.append(eff)

print(res)
