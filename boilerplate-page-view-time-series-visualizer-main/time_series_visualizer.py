import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# reads the CSV file, treating the 'date' column as dates and using it as the row labels
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# remove extreme values (too high or too low) to make the data cleaner
lower_cutoff = df['value'].quantile(0.025)  # Only keep values above 2.5% 
upper_cutoff = df['value'].quantile(0.975)  # Only keep values below 97.5%
df = df[(df['value'] >= lower_cutoff) & (df['value'] <= upper_cutoff)]

#--- LINE PLOT ---
def draw_line_plot():
    # sets up the plot size (width=15, height=5)
    fig, ax = plt.subplots(figsize=(15, 5))
    
    # draws a red line showing page views over time
    ax.plot(df.index, df['value'], color='red', linewidth=1)
    
    # adds titles and axis labels
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # saves the plot as an image file
    fig.savefig('line_plot.png')
    return fig

#--- BAR PLOT ---
def draw_bar_plot():
    # makes a copy of the data to avoid accidental changes
    df_bar = df.copy()
    
    # extracts year and month from dates (e.g., 2016-05-01 → year=2016, month=5)
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month

    # calculates average page views per year/month, then reshape for plotting
    df_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # creates a bar plot
    fig = df_grouped.plot(kind='bar', figsize=(10, 8)).figure
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    
    # renames the legend to show full month names (instead of numbers 1-12)
    plt.legend(title='Months', labels=[
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ])

    # saves the plot
    fig.savefig('bar_plot.png')
    return fig

#--- BOX PLOT ---
def draw_box_plot():
    # works with a fresh copy of the data
    df_box = df.copy()
    
    # converts dates into separate columns for year and month (e.g., "Jan", "Feb")
    df_box.reset_index(inplace=True)
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')  # Short month names (Jan-Dec)
    df_box['month_num'] = df_box['date'].dt.month  # Month numbers (1-12)

    # sorts months in calendar order (Jan=1, Feb=2, etc.)
    df_box = df_box.sort_values('month_num')

    # creates two side-by-side box plots
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

    # left plot: Yearly trends (shows growth/decline over years)
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Right plot: Monthly patterns (shows seasonal differences)
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Save the plot
    fig.savefig('box_plot.png')
    return fig