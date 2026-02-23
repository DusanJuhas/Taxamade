import re
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

print("----INFO----")
print(f"numpy - ",np.__version__) 
print(f"pandas -",pd.__version__) 
pd.set_option("display.max_rows",20)
pd.set_option("display.width",None)
pd.set_option("display.max_columns",30)
np.set_printoptions(threshold=np.inf, linewidth=np.inf) #switch off linewidth
print("----TAXAMADE----")

found = False
kurz_USD=21.84
kurz_EUR=24.66
print("Jednotný kurz: USD , EUR",kurz_USD,kurz_EUR)

####    parsing CSV do PD tab  ####
def parse_column(col):
    error = 0
    data=oo.dropna(subset=["Směr"],axis=0,how="any")    # only valid column
    data=data.dropna(axis=1,how="all")                  # drop empty column
    data=data.drop("Text FIO",axis=1)                   # drop unused column
    data=data.loc[data["Směr"]==col]               # use only for SELL

    data["Datum obchodu"] = pd.to_datetime(
        data["Datum obchodu"],
        format="%d.%m.%Y %H:%M",  # přesný formát "24.11.2025 17:24"
        errors="coerce"           # neparsovatelné hodnoty -> NaT (něco jako NaN pro datum)
    )
    #conversion to number
    cols = ["Cena", "Počet", "Objem v CZK","Poplatky v CZK","Objem v USD","Poplatky v USD","Objem v EUR","Poplatky v EUR"]                # columns

    for cmn in cols:
        data[cmn] = (
            data[cmn]
            .astype(str)
            .str.replace(",", ".", regex=False)
            .str.replace("\u00A0", "", regex=False)  # NBSP
            .str.replace("\u202F", "", regex=False)  # thin NBSP
            .str.replace(" ", "", regex=False)       # běžná mezera
            .astype(float)
        )
        data[cmn] = data[cmn].fillna(0)                 # NaN to 0
        if (data[cmn].isna().sum())>0:
            print(data[cmn].isna().sum(), "non parsed values") # 0 = OK
            error=error+1

    print("PARSE ERRORS = ",error)
    return data

####  Sumarizace pozic ####
def column_sum(pd):
    pd.loc[pd["Měna"] == "USD", "Objem v CZK"] = pd["Objem v USD"].abs() * kurz_USD
    pd.loc[pd["Měna"] == "USD", "Poplatky v CZK"] = pd["Poplatky v USD"].abs() * kurz_USD
    pd.loc[pd["Měna"] == "EUR", "Objem v CZK"] = pd["Objem v EUR"].abs() * kurz_USD
    pd.loc[pd["Měna"] == "EUR", "Poplatky v CZK"] = pd["Poplatky v EUR"].abs() * kurz_USD
    return pd
###########################

with open("Obchody.csv", "r") as fin, open("fio.csv", "w") as fout:
    for line in fin:
        if not found and line.lstrip().startswith("Datum obchodu"):
            found = True

        if found:
            # Nahradit středníky čárkami
            #line = line.replace(";", ",")          #not needed
            fout.write(line)

oo = pd.read_csv('fio.csv',sep=';',encoding='ANSI') # with semicolon

sell=parse_column("Prodej")
sell.info()
buy=parse_column("Nákup")
#buy.info()

cols_to_sum = ["Počet","Objem v CZK", "Poplatky v CZK","Objem v USD","Poplatky v USD","Objem v EUR","Poplatky v EUR"] 
# groupby nad 2. sloupcem a součet sloupce v def poli
out = sell.groupby(["Symbol","Měna"], as_index=False)[cols_to_sum].sum()
sell=column_sum(out)
#print(sell)           # tabulka 
print("__________________________")
out = buy.groupby(["Symbol","Měna"], as_index=False)[cols_to_sum].sum()
buy=column_sum(out)
#print(buy)           # tabulka 


with pd.ExcelWriter("fio.xlsx") as writer:
    # První tabulka
    sell.to_excel(writer, sheet_name="Report", index=False, startrow=1)

    fmt_default   = writer.book.add_format({"num_format": '#,##0.00'})
    # Nadpis mezi tabulkami
    worksheet = writer.sheets["Report"]
    worksheet.write(0, 0, "Výpis prodej")
    
    # Najdi indexy sloupců a nastav formáty na celý sloupec
    cols = {name: idx for idx, name in enumerate(sell.columns)}
    for name in cols_to_sum:
        if name in cols:
            col = cols[name]
            worksheet.set_column(col, col, 12, fmt_default)

    # Druhá tabulka pod první (např.  df1 má 100 řádků)
    start2 = len(sell) + 4
    worksheet.write(start2, 0, "Výpis nákup")

    buy.to_excel(writer, sheet_name="Report", index=False, startrow=start2+1)



pole = sell.to_numpy()
pole2=buy.to_numpy()
with open('output.txt', 'w') as outfile:
    outfile.write(str(pole)) 

uniq, inv = np.unique(pole[:,2], return_inverse=True)   
# 3) Sečteme 3. sloupec podle skupin v 2. sloupci
sums = np.zeros(len(uniq), dtype=float)
np.add.at(sums, inv, pole[:, 3])

#print(uniq,inv,sums)

print("__________________________")
# Výsledek: dvojice (unikátní_hodnota, součet)
#for u, s in zip(uniq, sums):
   # print(u, s)




