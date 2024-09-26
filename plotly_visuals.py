import pandas as pd
import plotly.graph_objects as go

# Load your summary data
summary_metrics = pd.read_csv('data/summary_data.csv')

# Round relevant columns to two decimal places
summary_metrics['Total Plays'] = summary_metrics['Total Plays'].round(2)
summary_metrics['Positive Plays'] = summary_metrics['Positive Plays'].round(2)
summary_metrics['Neutral Plays'] = summary_metrics['Neutral Plays'].round(2)
summary_metrics['Negative Plays'] = summary_metrics['Negative Plays'].round(2)
summary_metrics['Positive %'] = summary_metrics['Positive %'].round(2)
summary_metrics['Neutral %'] = summary_metrics['Neutral %'].round(2)
summary_metrics['Negative %'] = summary_metrics['Negative %'].round(2)

# Create a Plotly table
fig_table = go.Figure(data=[go.Table(
    header=dict(values=list(summary_metrics.columns),
                 fill_color='#4D4D4D',  # Dark Grey
                 align='center',
                 font=dict(color='white', size=18, family='Arial'),
                 height=40),
    cells=dict(values=[summary_metrics[col] for col in summary_metrics.columns],
               fill_color='#F2F2F2',  # Light Grey
               align='center',
               font=dict(color='black', size=16, family='Arial'),
               height=30)
)])

# Update layout
fig_table.update_layout(title='Play Count', title_x=0.5)

# Save the table figure as an HTML file
fig_table.write_html('plots/summary_table.html')

fig_table.show()
