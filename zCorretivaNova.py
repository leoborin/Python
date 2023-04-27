import pandas as pd
import requests
import json


dados = "Vazio"
cursor = 0
cursorstr = str(cursor)
regional = "SPC"
print("inicio")
print(cursor)
# criando dataframe
url2 = "https://pcmbm.com/api/1.1/obj/tabela_orc?api_token=df62e55f93df6ba73240fd0cfa9c95cb&cursor=0&constraints=[{\"key\":\"regional\",\"constraint_type\":\"text%20contains\",\"value\":\""+regional+"\"}]"
base2 = pd.read_json(url2)
dados = base2['response']['results']
Tabela_Final_Corretivas = pd.DataFrame(dados)
print(url2)
print(regional)
cursor = 100
# listando regionais
url3 = "https://pcmbm.com/api/1.1/obj/tabela_regional?api_token=df62e55f93df6ba73240fd0cfa9c95cb"
base3 = pd.read_json(url3)
Bs_Regional = base3['response']['results']
Tabela_Regional = pd.DataFrame(Bs_Regional)
regionais = Tabela_Regional['regional']

# loop regionais
for regional in regionais:
    print("regional atual:")
    print(regional)
    print("-----------")
# loop Cursor '&cursor'
    while dados != []:
        print(regional)
        print(cursor)
        cursorstr = str(cursor)
        url2 = "https://pcmbm.com/api/1.1/obj/tabela_orc?api_token=df62e55f93df6ba73240fd0cfa9c95cb&cursor="+cursorstr + \
            "&constraints=[{\"key\":\"regional\",\"constraint_type\":\"text%20contains\",\"value\":\""+regional+"\"}]"
        base2 = pd.read_json(url2)
        cursor += 100
        dados = base2['response']['results']
        df = pd.DataFrame(dados)
        Tabela_Final_Corretivas = pd.concat([Tabela_Final_Corretivas, df])
        print(url2)
        total_linha_df = len(Tabela_Final_Corretivas)
        print(total_linha_df)
    cursor = 0
    dados = "Vazio"


# Estrutura Principal

# Tabela_Final_Preventivas = Tabela_Ext_Preventivas()
# Tabela_Final_Preventivas.to_csv("tb_final_preventivas.csv")

Tabela_Final_Corretivas["Created Date"] = pd.to_datetime(
    Tabela_Final_Corretivas["Created Date"])
Tabela_Final_Corretivas['ano'] = Tabela_Final_Corretivas["Created Date"].dt.year
Tabela_Final_Corretivas = Tabela_Final_Corretivas.loc[Tabela_Final_Corretivas['ano'] > 2022]

Tabela_Final_Corretivas["Created Date"] = Tabela_Final_Corretivas["Created Date"].dt.date

Tabela_Final_Corretivas.to_excel("./Drive/tb_final_corretivas.xlsx")

print("successful")
