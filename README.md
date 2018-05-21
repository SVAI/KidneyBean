KidneyBean
---
 is a colab aimed at moving the needle on p1RCC (kidney cancer)

## Get started
To get this codebase,
1. install git (e.g. apt-get install git)
2. git clone https://github.com/SVAI/KidneyBean.git

## What this does
1. Given a .vcf (difference between cancer and non-cancer genome)
2. Find the class of genes most representative of the disease
3. Select the drugs known to interact with those genes
4. Determine reported adverse effects associated with those drugs
5. Recommend drug research targets

## How we recommend drug research targets
Given a gene enrichment set over the variants called between a type 1 renal papilary carcinoma tumor, we extract drugs from gdidb.org which are known to interact with these genes. Furthermore, we extract risk profiles for the selected drugs from the FDA's adverse event reporting database. Sorting the dgi-suggested genes by these risk profiles, we suggest research candidates.
