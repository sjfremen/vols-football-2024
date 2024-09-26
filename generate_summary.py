import pandas as pd
import glob

# Step 1: Load all Week CSV files
all_files = glob.glob('data/Week*.csv')
dfs = []

for filename in all_files:
    df = pd.read_csv(filename)
    # You may want to add a 'Week' column based on the filename if needed
    week_number = filename.split('/')[-1].replace('Week', '').replace('.csv', '')
    df['Week'] = f'Week{week_number}'
    dfs.append(df)

# Step 2: Concatenate all dataframes into one
master_df = pd.concat(dfs, ignore_index=True)

# Step 3: Calculate summary metrics for Tennessee
summary_metrics = master_df[master_df['Offense'] == 'Tennessee'].groupby('Week').apply(lambda df: pd.Series({
    'Total Plays': len(df),
    'Positive Plays': len(df[df['Yards Gained'] > 0]),
    'Neutral Plays': len(df[df['Yards Gained'] == 0]),
    'Negative Plays': len(df[df['Yards Gained'] < 0]),
}))

# Step 4: Calculate percentages
summary_metrics['Positive %'] = (summary_metrics['Positive Plays'] / summary_metrics['Total Plays']) * 100
summary_metrics['Neutral %'] = (summary_metrics['Neutral Plays'] / summary_metrics['Total Plays']) * 100
summary_metrics['Negative %'] = (summary_metrics['Negative Plays'] / summary_metrics['Total Plays']) * 100

# Reset index for proper CSV formatting
summary_metrics.reset_index(inplace=True)

# Step 5: Save to CSV
summary_metrics.to_csv('data/summary_data.csv', index=False)

# Create a bar chart for Total Plays by Week
fig = px.bar(df, x='Week', y='Total Plays', title='Total Plays by Week')

# Save the figure as an HTML file
fig.write_html('plots/total_plays_by_week.html')
