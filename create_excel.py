import pandas as pd

data = {
    "CustomerID": [1, 2, 3, 4],
    "FirstName": ["Alice", "Bob", "Carol", "Diana"],
    "LastName": ["Smith", "Johnson", "Williams", "Miller"],
    "Email": [
        "alice@example.com",
        "bob@example.com",
        "carol@example.com",
        "diana@example.com"
    ]
}

df = pd.DataFrame(data)
df.to_excel("customers_test.xlsx", index=False)
print("✅ Excel file 'customers_test.xlsx' created.")
