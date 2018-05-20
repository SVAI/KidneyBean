import requests
import json
import pdb

def gene_to_drug(gene_name):

    url = 'http://dgidb.org/api/v2/interactions.json?genes='+gene_name

    # print(url)
    myResponse = requests.get(url)
    gene_list=[]

    # For successful API call, response code will be 200 (OK)
    if(myResponse.ok):

        # Loading the response data into a dict variable
        # json.loads takes in only binary or string variables so using content to fetch binary content
        # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
        jData = json.loads(myResponse.content.decode())

        # print("The response contains {0} properties".format(len(jData)))
        # print("\n")

        drug_names = []
        if len(jData['matchedTerms']) > 0:
            for key in jData['matchedTerms'][0]['interactions']:
                drug_names.append(key['drugName'])

        # print("found {} drugs from dgidb".format(len(drug_names)))
        return(drug_names)

    else:
    # If response code is not ok (200), print the resulting http error code with description
        # print("got network error from dgidb")
        myResponse.raise_for_status()

def main():
    r = gene_to_drug("MET")
    print(r)

if __name__=="__main__":
    main()
