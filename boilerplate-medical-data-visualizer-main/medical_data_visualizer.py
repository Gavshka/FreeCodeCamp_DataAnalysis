import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# reads the dataset into a pandas DataFrame
df = pd.read_csv('medical_examination.csv')

# adds a new column for overweight status, using BMI formula and setting threshold at 25
df['overweight'] = ((df['weight'] / ((df['height'] / 100) ** 2)) > 25).astype(int)

# converts cholesterol and glucose columns: 1 = high, 0 = normal
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# this function creates a bar plot for categorical data
def draw_cat_plot():
    # melt the dataframe to have 'variable' and 'value' columns for plotting
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']
    )

    # group by cardio, variable, and value, then get counts for each combination
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).size()
    df_cat = df_cat.rename(columns={'size': 'total'})

    # creates a bar plot to show the total counts by variable, split by cardio status
    g = sns.catplot(
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        data=df_cat,
        kind='bar'
    )
    g.set_axis_labels('variable', 'total')
    g.set_titles('{col_name}')  # title for each subplot

    fig = g.fig
    fig.savefig('catplot.png')
    return fig

# this function creates a heatmap of correlation between numerical variables
def draw_heat_map():
    # cleans the data by removing outliers in height, weight, and blood pressure
    df_heat = df[(
        df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) & 
        (df['height'] <= df['height'].quantile(0.975)) & 
        (df['weight'] >= df['weight'].quantile(0.025)) & 
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # calculates the correlation matrix of the cleaned data
    corr = df_heat.corr()

    # creates a mask to only show the lower triangle of the correlation matrix
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # creates and customize the heatmap
    fig = plt.figure(figsize=(12, 10))
    ax = sns.heatmap(
        corr,
        mask=mask,  # only show lower triangle
        annot=True,  # annotate with correlation values
        fmt='.1f',  # format annotations to 1 decimal
        center=0,  # center color scale at 0
        square=True,  # make the plot square
        linewidths=.5,  # line width between cells
        cbar_kws={'shrink': 0.5}  # shrink the color bar a bit
    )

    fig.savefig('heatmap.png')
    return fig
