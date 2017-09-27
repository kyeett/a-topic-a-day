import random
import pandas as pd

class Base(object):

    attributes_names = ['age','sex','location','color','label']

    def __init__(self):
        self.attributes = [0, 20, 0, 10, "-"]

    def repr(self):
        return self.attributes


class A(Base):

    def __init__(self):
        super(A, self).__init__()
        self.attributes[1] = random.randint(-10, 20)
        self.attributes[4] = "A"


class B(Base):

    def __init__(self):
        super(B, self).__init__()
        self.attributes[0] = random.randint(10, 20)
        self.attributes[2] = random.randint(60, 80)
        self.attributes[4] = "B"


class C(Base):

    def __init__(self):
        super(C, self).__init__()
        self.attributes[0] = random.randint(2, 20)
        self.attributes[2] = random.randint(0, 20)
        self.attributes[3] = random.randint(0, 2)
        self.attributes[4] = "C"

# Generate random training set
dataset = [random.choice([A(), B(), C()]).attributes for _ in range(100)]

# Create arrays for the features and the response variable
df = pd.DataFrame(dataset, columns=Base.attributes_names)
y = df['label'].values
X = df.drop('label',axis=1).values

# Import KNeighborsClassifier from sklearn.neighbors
from sklearn.neighbors import KNeighborsClassifier


# Create a k-NN classifier with 6 neighbors
knn = KNeighborsClassifier(n_neighbors=6)

# Fit the classifier to the data
knn.fit(X, y)

# Predict label
a_type_attributes = A().attributes[:-1]
b_type_attributes = B().attributes[:-1]
c_type_attributes = C().attributes[:-1]

predicted = knn.predict([a_type_attributes, b_type_attributes, c_type_attributes])
print(predicted)
