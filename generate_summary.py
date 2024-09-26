import pandas as pd
import glob
import plotly.express as px
import plotly.graph_objects as go

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
summary_metrics['Positive %'] = round((summary_metrics['Positive Plays'] / summary_metrics['Total Plays']) * 100,2)
summary_metrics['Neutral %'] = round((summary_metrics['Neutral Plays'] / summary_metrics['Total Plays']) * 100,2)
summary_metrics['Negative %'] = round((summary_metrics['Negative Plays'] / summary_metrics['Total Plays']) * 100,2)

# Reset index for proper CSV formatting
summary_metrics.reset_index(inplace=True)

# Step 3: Generate play type counts by week
play_type_counts_by_week = master_df.groupby(['Week', 'Play Type']).size().unstack(fill_value=0)
total_plays_per_type = play_type_counts_by_week.sum(axis=0)
play_type = play_type_counts_by_week.loc[:, total_plays_per_type.sort_values(ascending=False).index]

# Step 5: Save to CSVs
summary_metrics.to_csv('data/summary_data.csv', index=False)
play_type.to_csv('data/play_type.csv')
