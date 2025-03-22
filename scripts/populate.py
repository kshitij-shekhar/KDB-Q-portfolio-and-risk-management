"""Populate the database"""

from qpython import qconnection

# Establish connection to kdb+
q = qconnection.QConnection(host='localhost', port=5000)
q.open()

# Define data to insert
users_data = [
    ("u001", "Kshitij", "trader"),
    ("u002", "Jim", "trader"),
]

portfolios_data = [
    ("p001", "Tech Growth Fund", "Kshitij", "Technology"),
    ("p002", "Climate Impact Fund", "Jim", "Climate Change"),
]

holdings_data = [
    ("p001", "AAPL", 50, 175.30, 175.50, 10.0),
    ("p001", "MSFT", 40, 320.75, 321.10, 15.2),
    ("p001", "GOOGL", 30, 2700.50, 2712.00, 8.5),
    ("p001", "AMZN", 25, 3300.00, 3315.00, 5.4),
    ("p001", "META", 20, 290.10, 291.50, 7.3),
    ("p001", "NVDA", 35, 645.20, 648.00, 10.1),
    ("p001", "AMD", 45, 105.30, 106.40, 12.2),
    ("p001", "TSM", 50, 125.75, 126.90, 9.8),
    ("p001", "INTC", 60, 53.40, 54.00, 14.6),
    ("p001", "ORCL", 30, 92.50, 93.10, 6.9),
    ("p002", "TSLA", 20, 920.50, 910.20, 200.0),
    ("p002", "PLUG", 35, 25.10, 26.00, 18.5),
    ("p002", "NEE", 40, 78.90, 79.50, 11.3),
    ("p002", "SEDG", 30, 290.25, 292.10, 7.2),
    ("p002", "ENPH", 25, 170.50, 172.00, 5.6),
    ("p002", "FSLR", 50, 105.30, 107.00, 9.4),
    ("p002", "RUN", 60, 45.40, 46.00, 12.8),
    ("p002", "BE", 45, 18.75, 19.20, 15.9),
    ("p002", "SPWR", 35, 24.50, 25.00, 8.7),
    ("p002", "JKS", 20, 50.75, 51.50, 10.2),
]

# Insert data into tables
q.sync('insert[`users]', users_data)
q.sync('insert[`portfolios]', portfolios_data)
q.sync('insert[`holdings]', holdings_data)

print("Data inserted successfully!")

# Close connection
q.close()