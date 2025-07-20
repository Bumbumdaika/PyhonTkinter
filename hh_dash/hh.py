import requests
import pandas as pd

# url = 'https://api.hh.ru/vacancies'
# params = {
#     'text': 'NAME:программист',
#     'area': 22,
#     'page':0,
#     'per_page':100
# }

def get_hh_df(params):
    r = requests.get(url='https://api.hh.ru/vacancies',params=params)
    r_json = r.json()
    df = pd.DataFrame(columns=['name','salary_from','salary_to','company'])
    for i in r_json['items']:
        title = i['name']
        try:
            salary_from = int(i['salary']['from'])
        except:
            salary_from = 'NULL'
        try:
            salary_to = int(i['salary']['to'])
        except:
            salary_to = -1
        emp = i['employer']['name']
        df.loc[len(df)] = [title,salary_from,salary_to,emp]
    df=df.sort_values(by='salary_to',ascending=False)
    return df