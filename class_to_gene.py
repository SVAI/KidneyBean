import requests
import json
# from exception import LookupError
import pdb

def class_to_gene(class_name):

    classes = []
    with open("gene_categories.json", "r") as f:
        classes = json.load(f)

    if not class_name in classes:
        raise LookupError("class " + class_name + " not valid")

    url = 'http://dgidb.org/api/v2/genes_in_category.json?category=' +\
        class_name

    myResponse = requests.get(url)
    gene_list=[]

    # For successful API call, response code will be 200 (OK)
    if(myResponse.ok):

        # Loading the response data into a dict variable
        # json.loads takes in only binary or string variables so using content
        # to fetch binary content Loads (Load String) takes a Json file and
        # converts into python data structure (dict or list, depending on JSON)
        jData = json.loads(myResponse.content.decode())

        # pdb.set_trace()
        # for key in jData['matchedTerms'][0]['interactions']:
        #     print(key['interactions'])

        return(jData)

    else:
    # If response code is not ok (200), print the resulting http error code with
    # description
        myResponse.raise_for_status()

def main():
    r = class_to_gene("TUMOR SUPPRESSOR")
    print(r)

if __name__=="__main__":
    main()
