import pandas as pd

# Read original ISO-8859-1 file
with open('Most Streamed Spotify Songs 2024.csv', 'r', encoding='windows-1252') as f:
    content = f.read()

# Write to a new UTF-8 encoded file
with open('spot_streams.csv', 'w', encoding='utf-8') as f:
    f.write(content)

df = pd.read_csv('spot_streams.csv', encoding='utf-8')