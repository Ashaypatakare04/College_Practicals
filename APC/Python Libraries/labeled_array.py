import numpy as np

data = np.array([
    ('A', 25),
    ('B', 50),
    ('C', 75)
    ],dtype=[('Label','U10'), ('Value', 'i4')]
)
print(data)
print(data['Label'])
print(data['Value'])