import pandas as pd

# Read in the spreadsheet data
df = pd.read_excel('your_spreadsheet.xlsx')

# Calculate failure count and total checks
failures = df.loc[(df['Mandatory Control'] == 0) & (df['Sub Control ID'] == 0)]
failure_count = failures.groupby(['Dashboard Family', 'Mandatory Control', 'Sub Control ID', 'Subcontrol'])['Subcontrol'].count().reset_index(name='failure count')
total_checks = df.groupby(['Dashboard Family', 'Mandatory Control', 'Sub Control ID', 'Subcontrol'])['checkstatus'].count().reset_index(name='total checks')

# Merge failure count and total checks dataframes
report_df = pd.merge(failure_count, total_checks, on=['Dashboard Family', 'Mandatory Control', 'Sub Control ID', 'Subcontrol'], how='outer')

# Output the report
print(report_df[['Dashboard Family', 'Mandatory Control', 'Sub Control ID', 'Subcontrol', 'failure count', 'total checks']])
