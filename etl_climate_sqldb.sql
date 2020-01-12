CREATE TABLE metrics_data(
	id SERIAL PRIMARY KEY,
	Year TEXT,
    US_Wildfire_Count TEXT,
    Brazil_Wildfire_Count TEXT,
    Worldwide_Oil_Production TEXT,
    Oil_Year_Variance TEXT,
    US_Max_Annual_Temp_C TEXT,
    Brazil_Max_Annual_Temp_C TEXT,
    Brazil_C02_Emissions_Ton TEXT,
    US_C02_Emissions_Ton TEXT);
	
SELECT * FROM metrics_data;
