import pandas as pd
import re

# Step 1: Read original file with windows-1252 encoding
with open('Most Streamed Spotify Songs 2024.csv', 'r', encoding='windows-1252') as f:
    content = f.read()

# Step 2: Remove weird/unprintable characters
# Keep printable characters and basic punctuation
clean_content = re.sub(r'[^\x20-\x7E\n\r,]', '', content)

# Step 3: Save cleaned content in UTF-8
cleaned_path = 'spot_streams_cleaned.csv'
with open(cleaned_path, 'w', encoding='utf-8') as f:
    f.write(clean_content)

# Step 4: Load it into pandas
df = pd.read_csv(cleaned_path)
df.head()
