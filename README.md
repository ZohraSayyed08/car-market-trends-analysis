# Car Market Trends Analysis with Car Dekho Data

DIY Project 4 - Data Analytics 
VOIS & Vodafone Idea Foundation Data Analytics Internship (via Edunet Foundation, VOIS for Tech LMS)

## Overview
Exploratory data analysis of a used-car listings dataset (Car Dekho) to understand
pricing trends by fuel type, transmission, seller type, and car age.

## Dataset
299 cleaned records (from an original 301), 9 columns:
Car_Name, Year, Selling_Price, Present_Price, Kms_Driven, Fuel_Type,
Seller_Type, Transmission, Owner

## Data Cleaning Steps
1. Removed 2 exact duplicate rows
2. Checked for missing values (none found)
3. Verified category label consistency across Fuel_Type, Seller_Type, Transmission
4. Stripped stray whitespace from 5 `Car_Name` entries
5. Flagged one extreme outlier (500,000 km on a 2008 scooter) - kept in the
   dataset but excluded from the km-driven chart to avoid distortion

## Key Findings
- Diesel cars sell for 3x the price of Petrol/CNG cars on average
- Manual transmission dominates the listings (260 vs 39 automatic)
- Selling price correlates strongly with present (ex-showroom) price (r = 0.876)
- Selling price weakly decreases with car age (r = -0.234)
- Most listed model: Honda City (26 listings)

## Files
- `Car_Dekho_Data.csv` - original raw dataset
- `cleaned_data.csv` - cleaned dataset used for analysis
- `analysis.py` - full cleaning + analysis + chart-generation script
- `chart1-5*.png` - output visualizations

## Tools Used
Python, Pandas, Matplotlib, Seaborn, Google Colab
