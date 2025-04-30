import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # reads sea level data from CSV file
    df = pd.read_csv('epa-sea-level.csv')

    # sets up the plot size (width=10, height=6 inches)
    plt.figure(figsize=(10, 6))
    
    # plots the raw data points (years vs sea levels)
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], 
                label='Original Data', alpha=0.5)

    #--- FIRST TREND LINE (1880-2050) ---
    # calculates best-fit line using ALL data
    res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    # generate years from 1880 to 2050 for prediction
    x_pred1 = pd.Series(range(1880, 2051))
    # calculates predicted sea levels using slope and intercept
    y_pred1 = res1.slope * x_pred1 + res1.intercept
    # plots the line in red
    plt.plot(x_pred1, y_pred1, 'r', label='Best Fit: 1880–2050')

    #--- SECOND TREND LINE (2000-2050) ---
    # Filter data to only use years 2000 and later
    df_recent = df[df['Year'] >= 2000]
    # calculates new best-fit line using recent data only
    res2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    # Generate years from 2000 to 2050
    x_pred2 = pd.Series(range(2000, 2051))
    # calculates new predictions
    y_pred2 = res2.slope * x_pred2 + res2.intercept
    # plots this line in green
    plt.plot(x_pred2, y_pred2, 'g', label='Best Fit: 2000–2050')

    #--- FINAL TOUCHES ---
    # Label the axes and add title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    # Show legend to identify each line
    plt.legend()

    plt.savefig('sea_level_plot.png')
    return plt.gca()