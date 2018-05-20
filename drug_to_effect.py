import requests
import json
import pdb

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
        pdb.set_trace()
        risk = bad/total
        var = risk*(1-risk)/total

        print("Risk of drug {} is {}".format(drug_name, risk))
        return(risk)

    else:
        myResponse.raise_for_status()

def main():
    r = gene_to_drug("MET")
    effs = []
    for d in r:
        s = drug_to_effect(d)
        effs.append(s)
    print(effs)

if __name__=="__main__":
    main()
