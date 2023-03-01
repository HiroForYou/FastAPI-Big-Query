from google.cloud import bigquery

client = bigquery.Client()

view_id = "my-project.my_dataset.my_view"
source_id = "my-project.my_dataset.my_table"
view = bigquery.Table(view_id)

# The source table in this example is created from a CSV file in Google
# Cloud Storage located at
# `gs://cloud-samples-data/bigquery/us-states/us-states.csv`. It contains
# 50 US states, while the view returns only those states with names
# starting with the letter 'W'.
view.view_query = f"SELECT name, post_abbr FROM `{source_id}` WHERE name LIKE 'W%'"

# Make an API request to create the view.
view = client.create_table(view)
print(f"Created {view.table_type}: {str(view.reference)}")