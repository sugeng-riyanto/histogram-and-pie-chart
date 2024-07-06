import pandas as pd
import numpy as np

# Generate a sample DataFrame
data = {
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Values': np.random.randint(10, 100, size=5),
    'Frequency': np.random.randint(1, 10, size=5)
}

df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel('sample_data.xlsx', index=False)
