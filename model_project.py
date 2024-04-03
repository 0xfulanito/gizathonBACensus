from scipy.stats import pearsonr
from sklearn.linear_model import LinearRegression
import numpy as np
from census import Census
from us import states
import pandas as pd
import requests
import zipfile
RELATIVE_PATH = f'./data/'

def df_oep(fipscode):
 dataframes = []

 for year in [2015,2016,2017,2018,2019,2020,2021,2022,2023]:
     try:
         if year in [2015,2016,2017]:
             # Obtén los datos de población por condado para el año actual
             #print(year)
             path = f'{RELATIVE_PATH}{year}_OEP_County-Level_Public_Use_File.zip'
             file = f'{year}_OEP_County-Level_Public_Use_File.xlsx'
             sheet = "(1) Consumer Type"
             archive = zipfile.ZipFile(path, 'r')
             xlfile = archive.open(file)
             if year == 2016:
                 df2 = pd.read_excel(xlfile,sheet_name= sheet)[['County FIPS Code','State ',
                 'Total Number of Consumers Who Have Selected a Marketplace Plan']].rename(columns={'Total Number of Consumers Who Have Selected a Marketplace Plan': 'Cnsmr',
                                                                                                   'State ': 'State'})
                 df2['yrs'] = f'yrs_{year}'
                 df2 = df2.iloc[:-1,:]
             else:
                  df2 = pd.read_excel(xlfile,sheet_name= sheet)[['County FIPS Code','State',
                 'Total Number of Consumers Who Have Selected a Marketplace Plan']].rename(columns={'Total Number of Consumers Who Have Selected a Marketplace Plan': 'Cnsmr'})
                  df2['yrs'] = f'yrs_{year}'
                  df2 = df2.iloc[:-1,:]                    

         if year in [2018]:
             # Obtén los datos de población por condado para el año actual
             #print(year)
             path = f'{RELATIVE_PATH}OE{year}_County_PUF_20180404.zip' 
             file = f'OE{year}_County_PUF_20180404.xlsx'
             sheet = "(1) Enrollment Status"
             archive = zipfile.ZipFile(path, 'r')
             xlfile = archive.open(file) 
             df2 = pd.read_excel(xlfile,sheet_name= sheet)[['County FIPS Code', 'State',
             'Total Number of Consumers Who Have Selected an Exchange Plan']].rename(columns={'Total Number of Consumers Who Have Selected an Exchange Plan': 'Cnsmr'})
             df2['yrs'] = f'yrs_{year}'
             df2 = df2.iloc[:-1,:]

         elif year in [2019,2022]:
             #print(year)
             path = f'{RELATIVE_PATH}{year} OEP County-Level Public Use File.zip'
             file = f'{year} OEP County-Level Public Use File.xlsx'
             sheet = "(1) Enrollment Status"
             archive = zipfile.ZipFile(path, 'r')
             xlfile = archive.open(file)
             if year == 2019:
                 df2 = pd.read_excel(xlfile,sheet_name= sheet)[['County FIPS Code','State',
                 'Total Number of Consumers Who Have Selected an Exchange Plan']].rename(columns={'Total Number of Consumers Who Have Selected an Exchange Plan': 'Cnsmr'})
                 df2['yrs'] = f'yrs_{year}'
                 df2 = df2.iloc[:-1,:]
             else:
                 df2 = pd.read_excel(xlfile,sheet_name= sheet)[['County FIPS Code','State',
                 'Number of Consumers with a Marketplace Plan Selection']].rename(columns={'Number of Consumers with a Marketplace Plan Selection': 'Cnsmr'})
                 df2['yrs'] = f'yrs_{year}'
                 df2 = df2.iloc[:-1,:]
                
         elif year in [2020]:
             #print(year)
             path = f'{RELATIVE_PATH}{year} OEP County-Level Public Use File.zip'
             file = f'{year} OEP County-Level Public Use File.csv'
             sheet = "2020 OEP County-Level Public Us"    
             archive = zipfile.ZipFile(path, 'r')
             xlfile = archive.open(file)
             df2 = pd.read_csv(xlfile)[['Cnty_FIPS_Cd','State_Abrvtn','Cnsmr']].rename(columns={'Cnty_FIPS_Cd':'County FIPS Code','State_Abrvtn': 'State'})
             df2['yrs'] = f'yrs_{year}'
             df2 = df2.iloc[:-1,:]

         elif year in [2023]:
             #print(year)
             path = f'{RELATIVE_PATH}{year} OEP County-Level Public Use File.zip'
             file = f'{year} OEP County-Level Public Use File.xlsx'
             sheet = "(1) by Enrollment Status" 
             archive = zipfile.ZipFile(path, 'r')
             xlfile = archive.open(file)
             df2 = pd.read_excel(xlfile,sheet_name= sheet)[['County FIPS Code', 'State',
             'Number of Consumers with a Marketplace Plan Selection']].rename(columns={'Number of Consumers with a Marketplace Plan Selection': 'Cnsmr'})
             df2['yrs'] = f'yrs_{year}'
             df2 = df2.iloc[:-1,:]

         elif year in [2021]:
             #print(year)
             path = f'{RELATIVE_PATH}{year} OEP County-Level Public Use File_0.zip'
             file = f'{year} OEP County-Level Public Use File.csv'
             archive = zipfile.ZipFile(path, 'r')
             xlfile = archive.open(file)
             df2 = pd.read_csv(xlfile)[['County_FIPS_Cd','State_Abrvtn','Cnsmr']].rename(columns={'County_FIPS_Cd':'County FIPS Code','State_Abrvtn': 'State'})
             df2['yrs'] = f'yrs_{year}'
             df2 = df2.iloc[:-1,:]

     except Exception as e:
         # Manejo de la excepción sin detener el ciclo
         print("Ocurrió un error:", str(e))

     df = pd.DataFrame(df2)
     dataframes.append(df)

 df_final = pd.concat(dataframes, axis=0)
 df_final['yrs'] = df_final['yrs'].str[-4:]
 df_final = df_final[df_final['County FIPS Code'] == fipscode]
 return df_final


def population(fipscode):
    df_pop1 = pd.read_csv(f'{RELATIVE_PATH}co-est2020__.csv',encoding='latin-1').iloc[:,[3,4,5,8,9,10,11,12,13,14,15,16,17,18,19]]
    df_pop2 = pd.read_csv(f'{RELATIVE_PATH}co-est2023-alldata.csv',encoding='latin-1').iloc[:,[3,4,5,9,10,11]]

    df_pop1['COUNTY'] = df_pop1['COUNTY'].apply(lambda x: f'00{x}' if 1 <= x <= 9
                                    else f'0{x}' if 10 <= x <= 99
                                    else x)
    df_pop1['STATE'] = df_pop1['STATE'].apply(lambda x: f'0{x}' if 1 <= x <= 9
                                     else x)
    df_pop1['County FIPS Code'] = df_pop1['STATE'].astype(str) +''+df_pop1['COUNTY'].astype(str)

    df_pop1 = pd.melt(
    df_pop1,
    id_vars=["County FIPS Code", "STNAME"],
    value_vars=['POPESTIMATE2015','POPESTIMATE2016','POPESTIMATE2017','POPESTIMATE2018','POPESTIMATE2019',
                'POPESTIMATE042020'],
    var_name="yrs",
    value_name="Population",
                      )
    df_pop1['yrs'] = df_pop1['yrs'].str[-4:]


    df_pop2['COUNTY'] = df_pop2['COUNTY'].apply(lambda x: f'00{x}' if 1 <= x <= 9
                                    else f'0{x}' if 10 <= x <= 99
                                    else x)

    df_pop2['STATE'] = df_pop2['STATE'].apply(lambda x: f'0{x}' if 1 <= x <= 9
                                     else x)

    df_pop2['County FIPS Code'] = df_pop2['STATE'].astype(str) +''+df_pop2['COUNTY'].astype(str)

    df_pop2 = pd.melt(
    df_pop2,
    id_vars=["County FIPS Code", "STNAME"],
    value_vars=['POPESTIMATE2021','POPESTIMATE2022','POPESTIMATE2023'],
    var_name="yrs",
    value_name="Population",
                     )
    df_pop2['yrs'] = df_pop2['yrs'].str[-4:]   

    df_pop = pd.concat([df_pop1,df_pop2], axis=0)
    df_maximos = df_pop.groupby(['STNAME','yrs']).agg({'Population':'max'}).reset_index()
    df_pop = df_pop.merge(df_maximos, on=['STNAME','yrs','Population'], how='left', indicator=True)
    df_pop = df_pop.query('_merge != "both"')[['County FIPS Code','STNAME','yrs','Population']]
    df_pop = df_pop[df_pop['County FIPS Code'] == fipscode]
    return df_pop


### build population dataframe to county 01001 and oep dataframe
mdf_pop = population('01001')
mdf_oep = df_oep('01001')
### Esto se corre sólo para ver que funcionan las funciones

### this function build dataframe use on the model
def build_df(fipscode):
    x = population(fipscode)[['yrs','Population']]
    y = df_oep(fipscode)[['yrs','Cnsmr']]
    y['Cnsmr'] = pd.to_numeric(y['Cnsmr'].astype(str).str.replace(',', ''))

    #x = pd.to_numeric(x1['Population'].astype(str).str.replace(',', ''))
    #y = pd.to_numeric(y1['Cnsmr'].astype(str).str.replace(',', ''))
    df_model = pd.merge(x, y, on='yrs')

    return df_model

## run last function
df_reg = build_df('01001')

## Ajustar el modelo a los datos del dataframe df_reg
model = LinearRegression()
x = np.array(df_reg['Population']).reshape(-1, 1)
y = df_reg['Cnsmr']
model.fit(x, y)

## Dato para realizar el pronóstico
x_proy = np.array([72281]).reshape(-1, 1)

model.predict(X = x_proy)

from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

# Define the initial types for the ONNX model
initial_type = [('float_input', FloatTensorType([None, x.shape[1]]))]

# Convert the scikit-learn model to ONNX
onnx_model = convert_sklearn(model, initial_types=initial_type)

# Save the ONNX model to a file
with open("census_lr.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())