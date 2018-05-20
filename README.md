KidneyBean
---
 is a colab aimed at moving the needle on p1RCC (kidney cancer)

## Get started
To get this codebase,
1. install git (e.g. apt-get install git)
2. git clone https://github.com/ekalosak/KidneyBean.git

## What this does
1. Given a .vcf (difference between cancer and non-cancer genome)
2. Find the class of genes most representative of the disease
3. Select the drugs known to interact with those genes
4. Determine reported adverse effects associated with those drugs
5. Recommend drug research targets

## How we recommend drug research targets
Given the list of drugs and their properties (e.g. adverse effects, action
category), TODO: design machine learning method
