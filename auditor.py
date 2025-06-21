from excel_utils import load_excel, generate_audit_report
from db_utils import fetch_sql_data

excel_path = "templates/client-data.xlsx"
df_excel = load_excel(excel_path)
df_sql = fetch_sql_data("Customers")
generate_audit_report(df_excel, df_sql, output_path="audit_report.xlsx")
