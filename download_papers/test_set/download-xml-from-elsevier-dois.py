import pandas as pd
import requests
import time
import os

#Sets the current working directory to be the same as the file
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# define headers for Elsevier API
headers = {
           'X-ELS-APIKey': 'PLACEHOLDER',
           'Accept': 'text/xml'
           }

# define test set Elsevier DOIs
dois_df = pd.read_csv('OA-and-pub-info.csv')
dois = dois_df[dois_df['Publisher'] == 'Elsevier BV']['DOI'].to_list()

print(f'Beginning to save XML files for {len(dois)} Elsevier DOIs...')

for i in range(len(dois)):

    # define doi
    doi = dois[i]

    # define endpoint URL
    url_doc = 'https://api.elsevier.com/content/article/doi/' + doi

    # retrieve document information
    try: 
        sr = requests.get(url=url_doc,headers=headers)
    except Exception as e:
        print('Error:', e)
        continue

    #time.sleep(0.1)
    # print(sr) # check response code

    # save as an XML file
    with open(f'XMLs/Elsevier/{doi.replace("/","_")}.xml', 'w', encoding='utf-8') as file:
        file.write(sr.text)

    print(f'Saved XML {i}')
