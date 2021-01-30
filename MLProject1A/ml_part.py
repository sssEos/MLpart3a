import requests
import pandas as pd
url ="https://data.gov.sg/api/action/datastore_search?resource_id=f9dbfc75-a2dc-42af-9f50-425e4107ae84&limit=100000"
result = requests.get(url).json()
# Try out the following codes
# Try to understand the result and figure out how is the data stored in json.


print(result.keys())
print(result["result"].keys)
# print(result['result']['records'])


#
# def read_url(url):
#     result = requests.get(url).json()
# Try out the following codes
# Try to understand the result and figure out how is the data
# stored in json.
#     print(result.keys())
#     print(result['success'])
df1 = pd.DataFrame(result['result']['records'])
print(df1[(df1.year=='2019')&(df1.level_2=='90 Years & Over')])

