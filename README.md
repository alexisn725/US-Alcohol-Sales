# US Alcohol Sales - Code Kentucky Data 1

This project uses a data set provided by the US government as part of their Surveillance Reports from the *National Institute on Alcohol Abuse and Alcoholism.* The link can be found here:  

https://pubs.niaaa.nih.gov/publications/surveillance-covid-19/COVSALES.htm

The data set provided was used to create the Surveillance Report: **Alcohol Sales During the COVID-19 Pandemic** and contains per capita alcohol sales between the years of 2017 - 2021 of beer, wine, and spirits during the Covid-19 pandemic for 13 states so far. The NIAAA also created several charts of their own on the data; if you're interested in viewing more I would definitely take a look. 

I downloaded the .xlsx data file provided by the researchers and converted that into a CSV file for ease. Once that was done, I was able to analyze the data to find the total gallons of alcohol sold by state, the total gallons of alcohol sold by year, and the total gallons of alchol grouped by state and type of beverage. There are expressions written for the user to also find out data calculations on their own as well. 


This project was completed by mostly using Jupyter Notebook, but US_Alcohol_Sales.ipynb or US_Alcohol_Sales-3.py should work with any editor. 

The required modules to run this data file is included in the requirements.txt file.

## Requirement 1: Read data in
- The .xlsx was downloaded separately as a local CSV file, and read into a dataframe.

## Requirement 2: Manipulate and clean your data
- I sorted out the rows for the Years column to separate and drop years 2017 and 2018 since I wanted to focus solely on Covid years. 
- I then dropped the last two columns, PerCapita3Yr and PctChange, since they were mostly empty of data. 
- I dropped the rows with null entries using dropna().
- I renamed the FIPS column to State, so that it was more clear.
- I converted the Gallons column into an integer, and State and Beverage into strings.
- I then replaced the data in the State and Beverage columns.

## Requirement 3: Analyze your Data
- I created expressions to: 
    - see total amount of gallons sold between years of 2019 - 2021
    - see total amount of gallons sold, filtered by year
    - see total amount of gallons sold, filtered by state
    - see total amount of gallons sold, filtered by beverage
    - see a function that shows the total amount of gallons sold, filtered by year, state, and type of beverage
    - find average gallons sold per year
    - find average gallons sold per type of beverage
    - find average gallons sold per state
    - find gallons per capita, multiplying those two columns
    - find the smallest value of gallons
    - find the median value of gallons
-most of these have user input that allows the user to determine which value they want to see the total of

## Requirement 4: Visualize your Data
- Using Matplotlib: 
    - created a bar graph for total gallons sold in each state
    - created a pie chart to show the total alcohol sales percentages, by year
    - created a bar graph that shows the total gallons grouped by state and type of beverage
    

## Requirement 5: Interpret your data and graphical output
- The project shows that the two larger states in this data set purchased the most alcohol (Texas and Florida).
- The pie chart shows that while 2019 and 2020 had higher percentages of sales, it dipped drastically in 2021. I'm not sure what the underlying causes of that sales loss is, but it does suggest that the US bought a lot of alcohol during the peak of the pandemic. 
- The final chart shows that the majority of alcohol sales are in fact beer purchases, not wine or spirits. In most states beer sold the most, while spirits and wine were similar in number. The beer sales for Texas and Florida also echo their large majority of total gallons in the first chart. 


Thank you for viewing!
