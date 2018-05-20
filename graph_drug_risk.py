import pickle
import pdb
# from ggplot import *
from matplotlib import pyplot as plt
import sys
import pandas as pd
import numpy as np

def main():
    nm = sys.argv[1]
    gene_name = nm.split("_")[1]
    d = pickle.load(open(nm, "rb"))
    drugs = list(d.keys())

    risk = [d[r]['risk'] for r in drugs]
    var = [d[r]['var'] for r in drugs]

    df = pd.DataFrame({'drug':drugs, 'risk':risk, 'var':var})
    df = df.dropna()
    df = df.sort_values(by='risk')
    n = len(df)

    # p = ggplot(df, aes(x='drug', y='risk', size='var')) + geom_point()
    # p = ggplot(df, aes(x='drug', y='risk')) + geom_point()
    # p.show()
    # return(p)

    error_config = {'ecolor': '0.3'}
    bar_width = 0.35
    fig, ax = plt.subplots()
    ix = np.arange(n)

    plt.bar(ix, df['risk'], bar_width,
            yerr=df['var'], error_kw=error_config)

    ax.set_title("Risks of various drugs associated with {}".format(gene_name))
    ax.set_xticks(ix + bar_width / 2)
    ax.set_xticklabels(df['drug'])

    plt.xticks(rotation=90)
    plt.tight_layout()

    plt.show()

if __name__=="__main__":
    main()
