# ETL Project


![Image description](https://www.grazitti.com/assets/2019/08/ETL_Bannera.gif)


The purpose (use) of this project is to provide key data information for future assesment of impact of human activity over earth’s climate, in particular, how oil production relates to increasing temperatures and observed trends in forest wildfires. Focused data gathering on two countries: Brazil and the USA, for years 2000-2013.

<br/>


#### Extraction/Transformation/Loading Process: 
E) Data extraction: CSV files from kaggle.com, Web-scrapped data <br/>
T) Data transformation: Pandas, Splinter and BeautifulSoup <br/>
L) Data load: Generation of SQL database using PostgreSQL and display the content using Flask <br/>

<br/>


#### Jupyter notebooks in this project:

- web-scraping.ipynb = used to extract information from websites and transform
- temp-historical.ipynb = used to import temperature dataset from kaggle and format
- CleanCSV.ipynb = used to clean C02 emissions dataset from kaggle
- database.ipynb = master notebook compiling the data mentioned above
<br/>

#### Flask app
- app.py



#### PostgreSQL
- etl_climate_sqldb.sql

<br/>

#### Project collaborators:
- Lourdes Rodriguez (lourdesrm)
- Luis Santana (lasantanag)
- Luis Casas (cosamagrande)


#### Links/Data Sources:
1.	https://www.indexmundi.com/energy/?product=oil&graph=production

2.	https://www.kaggle.com/srikantsahu/co2-and-ghg-emission-data#emission%20data.csv

3.	https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data#GlobalLandTemperaturesByCountry.csv

4.	http://queimadas.dgi.inpe.br/queimadas/portal-static/estatisticas_paises/

5.	https://www.ncdc.noaa.gov/societal-impacts/wildfires/ytd/0?params[]=acres&params[]=fires&params[]=apf
