import csv

# Open the CSV file and read its contents into a list of dictionaries
with open('input.csv', 'r', encoding='utf8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# Create dictionaries to hold the failure and total check counts
failure_count = {}
total_checks = {}

# Iterate over the rows and update the failure and total check counts
for row in rows:
    dashboard_family = row['Dashboard Family']
    mandatory_control = row['Mandatory Control']
    sub_control_id = row['Sub Control ID']
    sub_control = row['Subcontrol']
    rule_name = row['Rule Name']
    check_status = row['checkstatus']

    # Update the failure count
    if check_status == '0':
        key = (dashboard_family, mandatory_control, sub_control_id, sub_control, rule_name)
        failure_count[key] = failure_count.get(key, 0) + 1

    # Update the total check count
    key = (dashboard_family, mandatory_control, sub_control_id, sub_control, rule_name)
    total_checks[key] = 1

# Count the number of distinct groups for each combination of Dashboard Family, Mandatory Control, Subcontrol, and Rule Name
total_checks_count = {}
for key in total_checks:
    dashboard_family, mandatory_control, sub_control_id, sub_control, rule_name = key
    group_key = (dashboard_family, mandatory_control, sub_control_id, sub_control)
    total_checks_count[group_key] = total_checks_count.get(group_key, 0) + 1

# Write the output CSV file
with open('output.csv', 'w', newline='', encoding='utf8') as f:
    writer = csv.writer(f)
    writer.writerow(['Dashboard Family', 'Mandatory Control', 'Subcontrol', 'Rule Name', 'Failure Count', 'Total Checks'])
    for key, value in failure_count.items():
        dashboard_family, mandatory_control, sub_control_id, sub_control, rule_name = key
        group_key = (dashboard_family, mandatory_control, sub_control_id, sub_control)
        total_checks = total_checks_count.get(group_key, 0)
        writer.writerow([dashboard_family, mandatory_control, sub_control, rule_name, value, total_checks])
