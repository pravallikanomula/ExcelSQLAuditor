import pandas as pd
import xlsxwriter

def load_excel(filepath):
    return pd.read_excel(filepath, engine='openpyxl')

def compare_dataframes(df_excel, df_sql):
    df_excel = df_excel.fillna('').astype(str)
    df_sql = df_sql.fillna('').astype(str)

    # Sort for consistency
    df_excel_sorted = df_excel.sort_values(by=df_excel.columns.tolist()).reset_index(drop=True)
    df_sql_sorted = df_sql.sort_values(by=df_sql.columns.tolist()).reset_index(drop=True)

    # Compare full rows
    new_rows = df_excel_sorted[~df_excel_sorted.apply(tuple, axis=1).isin(
        df_sql_sorted.apply(tuple, axis=1)
    )]

    missing_rows = df_sql_sorted[~df_sql_sorted.apply(tuple, axis=1).isin(
        df_excel_sorted.apply(tuple, axis=1)
    )]

    # Compare by primary key (e.g., 'CustomerID')
    changed_rows = pd.DataFrame()
    if 'CustomerID' in df_excel.columns:
        merged = df_excel.merge(df_sql, on='CustomerID', suffixes=('_excel', '_sql'))
        diffs = []

        for _, row in merged.iterrows():
            diff = {}
            for col in df_excel.columns:
                if col != 'CustomerID':
                    if row[f"{col}_excel"] != row[f"{col}_sql"]:
                        diff['CustomerID'] = row['CustomerID']
                        diff[f"{col}_excel"] = row[f"{col}_excel"]
                        diff[f"{col}_sql"] = row[f"{col}_sql"]
            if diff:
                diffs.append(diff)
        changed_rows = pd.DataFrame(diffs)

    return new_rows, missing_rows, changed_rows


def generate_audit_report(df_excel, df_sql, output_path, dry_run=False):
    new_rows, missing_rows, changed_rows = compare_dataframes(df_excel, df_sql)

    with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
        new_rows.to_excel(writer, sheet_name='New Rows', index=False)
        missing_rows.to_excel(writer, sheet_name='Missing Rows', index=False)
        changed_rows.to_excel(writer, sheet_name='Changed Rows', index=False)

        workbook = writer.book
        red_format = workbook.add_format({'bg_color': '#FFC7CE', 'font_color': '#9C0006'})
        
        for sheet in ['New Rows', 'Missing Rows', 'Changed Rows']:
            worksheet = writer.sheets[sheet]
            worksheet.set_column(0, 100, 18)
            worksheet.conditional_format(1, 0, 1000, 100, {
                'type': 'text',
                'criteria': 'containing',
                'value': '',
                'format': red_format
            })

    print(f"[✔] Audit report saved to {output_path}")
