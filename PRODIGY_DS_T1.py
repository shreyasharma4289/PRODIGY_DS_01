# Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
# Step 2: Input dataset directly into the DataFrame
data = {
    'Name': ['Amit', 'Bhavish', 'Charlie', 'Dev', 'Steve', 'Rahul', 'Grace'],
    'Age': [25, 30, None, 22, 35, None, 30],
    'Category': ['A', 'B', 'A', 'B', 'A', 'B', 'A']
}

df = pd.DataFrame(data)
# Step 3: Basic Data Cleaning
# Check for missing values
print("Missing values before cleaning:\n", df.isnull().sum())

# Option: Fill missing values with the median of 'Age' column
median_age = df['Age'].median()  # Calculate the median
df['Age'] = df['Age'].fillna(median_age)

# Check for missing values after cleaning
print("\nMissing values after cleaning:\n", df.isnull().sum())

# Remove duplicates (if any)
df = df.drop_duplicates()

# Step 4: Visualize Data

# Example 1: Plot a histogram of the 'Age' column
plt.figure(figsize=(8, 5))
plt.hist(df['Age'], bins=5, color='skyblue', edgecolor='black')
plt.title('Histogram of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Example 2: Plot a bar chart of 'Category' counts
category_counts = df['Category'].value_counts()

plt.figure(figsize=(8, 5))
category_counts.plot(kind='bar', color='salmon', edgecolor='black')
plt.title('Category Count')
plt.xlabel('Category')
plt.ylabel('Count')
plt.show()
