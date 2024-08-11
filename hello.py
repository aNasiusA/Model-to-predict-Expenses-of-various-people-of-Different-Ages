from sklearn.model_selection import train_test_split
import numpy as np

# Sample data
x = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
y = np.array([1, 2, 3, 4, 5])

# Split the data
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

print("X_train:", X_train)
print("X_test:", X_test)
print("y_train:", y_train)
print("y_test:", y_test)
