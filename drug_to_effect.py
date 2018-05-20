import pickle
import requests
import json
import pdb

from requests.exceptions import HTTPError

from gene_to_drug import gene_to_drug

def drug_to_effect(drug_name):

    n = 10
    apikey = 'GLvXwBpL1cZ6G5ia0kDpyMixAKQhH6mWzz46GUeb'
    # url = 'https://api.fda.gov/drug/event.json?search='+drug_name+\
    #         '&limit='+str(n)
    url = 'https://api.fda.gov/drug/event.json?search=patient.drug.medicinalproduct:{}&count=serious'.format(drug_name)

    myResponse = requests.get(url)

    if(myResponse.ok):

        jData = json.loads(myResponse.content.decode())

        if 'error' in jData.keys():
            raise Exception("{} is not a drug in the database".format(
                    drug_name))

        res = jData['results']
        # print("got " + str(len(res)) + " results")
        # pdb.set_trace()
        bad = [r['count'] for r in res if r['term']==1]
        notbad = [r['count'] for r in res if r['term']==2]
        # pdb.set_trace()
        if len(bad)==0 or len(notbad)==0:
            raise Exception("drug {} has too few results".format(drug_name))

        bad = bad[0]
        notbad = notbad[0]
        total = bad + notbad
        risk = bad/total
        var = risk*(1-risk)/total

        print("Risk of drug {} is {}".format(drug_name, risk))
        return(risk, var)

    else:
        myResponse.raise_for_status()

def get_gene_drug_risks(gene_name):
    r = gene_to_drug(gene_name)

    effs = {}
    for d in r:
        er = True
        try:
            s = drug_to_effect(d)
            er = False
            effs[d] = {'risk':s[0], 'var':s[1]}

        except Exception as e:
            print("Error <{}> for drug {}".format(e, d))
            effs[d] = {'error':e}

    print(effs)
    return(effs)

def main():
    gn = "MET"
    eff = get_gene_drug_risks(gn)
    pickle.dump(eff, open("gene_"+gn+"_drug_risks.p", "wb"))

if __name__=="__main__":
    main()
