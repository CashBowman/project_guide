# -*- coding: utf-8 -*-
"""project_guide.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1x7tKQlInFemCUiIhEjg2jIOBlTwfCTjC

# Bash
"""

mkdir ...
# Create a virtual environment
python -m venv .venv # creates a venv folder
.venv/Scripts/Activate.ps1
pip install -r requirements.txt

"""# Imports"""

# USUALS:
import pandas as pd
import datetime

import yfinance as yf

import numpy as np

import matplotlib.pyplot as plt

import os

import seaborn as sns

import pyplot as px

# SCIKIT LEARN:
import sklearn as skl
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# TENSORFLOW:
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import *
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.losses import MeanSquaredError
from tensorflow.keras.metrics import RootMeanSquaredError
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import load_model

# Gradient Boosting:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
import xgboost as xgb
from lightgbm import LGBMClassifier
import lightgbm as lgb
import optuna
from catboost import CatBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import roc_auc_score, roc_curve, auc
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

"""# Pandas"""

# 🐼 Pandas Cheatsheet

## 1. Basics

### Import Pandas
import pandas as pd

### Load CSV
df = pd.read_csv('filename.csv')

### Show Top Rows
df.head()

### Show Bottom Rows
df.tail()

### Get Shape (rows, columns)
df.shape

### Show Column Names
df.columns

### Show Data Types
df.dtypes

---

## 2. Column & Row Selection

### Select Column
df['col']
df.col  # if no spaces in column name

### Select Multiple Columns
df[['col1', 'col2']]

### Select Row by Integer Position
df.iloc[3]

### Select Row by Label
df.loc[3]

### Boolean Filter
df[df['col'] > 100]

### Filter with Multiple Conditions
df[(df['col1'] > 50) & (df['col2'] == 'A')]

---

## 3. Sorting & Indexing

### Sort by Column
df.sort_values('col')

### Sort by Multiple Columns
df.sort_values(['col1', 'col2'], ascending=[True, False])

### Set Index
df.set_index('col', inplace=True)

### Reset Index
df.reset_index(drop=True, inplace=True)

---

## 4. Data Cleaning

### Rename Columns
df.rename(columns={'old': 'new'}, inplace=True)

### Drop Missing Rows
df.dropna(inplace=True)

### Fill Missing Values
df['col'].fillna(0, inplace=True)

### Replace Values
df['col'].replace({'old_val': 'new_val'}, inplace=True)

---

## 5. Creating & Modifying Columns

### Create New Column
df['new_col'] = df['a'] + df['b']

### Apply Function to Column
df['col'] = df['col'].apply(lambda x: x.upper())

### Bin Column
df['bin'] = pd.cut(df['col'], bins=3)

---

## 6. Grouping & Aggregation

### Groupby Mean
df.groupby('group_col')['val_col'].mean()

### Groupby Multiple Aggs
df.groupby('group_col').agg({'val1': 'mean', 'val2': 'sum'})

### Pivot Table
df.pivot_table(index='group', columns='type', values='value', aggfunc='sum')

---

## 7. Joining & Merging

### Merge Two DataFrames
pd.merge(df1, df2, on='key', how='inner')

### Concatenate (Stack Vertically)
pd.concat([df1, df2], axis=0)

### Concatenate (Join Side-by-Side)
pd.concat([df1, df2], axis=1)

---

## 8. Exporting Data

### Save to CSV
df.to_csv('filename.csv', index=False)

### Save to Excel
df.to_excel('filename.xlsx', index=False)

---

## 9. Common Summary Functions

### Describe (Summary Stats)
df.describe()

### Unique Values
df['col'].unique()

### Value Counts
df['col'].value_counts()

### Check for Nulls
df.isnull().sum()

### Correlation Matrix
df.corr()

"""# Pytorch"""

# 🔥 PyTorch Cheatsheet

## 1. Setup & Basics

### Import PyTorch
import torch
import torch.nn as nn
import torch.nn.functional as F

### Check Version
torch.__version__

### Manual Seed
torch.manual_seed(42)

---

## 2. Tensor Operations

### Create Tensor from Data
x = torch.tensor([[1., 2.], [3., 4.]])

### Random Tensor (Normal)
x = torch.randn(4, 3)

### Zeros / Ones
z = torch.zeros(2, 5)
o = torch.ones(2, 5)

### Shape & Reshape
x.shape
x = x.view(-1, 6)

### Concatenate
y = torch.cat((a, b), dim=0)

### Element-wise Math
out = x * y + 10

---

## 3. CUDA / MPS Devices

### Select Device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

### Move Tensor to GPU
x = x.to(device)

---

## 4. Autograd & Gradients

### Require Gradients
x = torch.randn(3, 3, requires_grad=True)

### Compute y and Backprop
y = (x ** 2).sum()
y.backward()
x.grad

### Disable Gradient Context
with torch.no_grad():
    pred = model(x)

---

## 5. Neural Networks (nn Module)

### Define Model
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(784, 256)
        self.fc2 = nn.Linear(256, 10)
    def forward(self, x):
        x = F.relu(self.fc1(x))
        return self.fc2(x)

model = Net().to(device)

### Loss & Optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

---

## 6. Data Loading

### Custom Dataset
from torch.utils.data import Dataset, DataLoader

class MyDataset(Dataset):
    def __init__(self, X, y):
        self.X, self.y = X, y
    def __len__(self):
        return len(self.X)
    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

train_loader = DataLoader(MyDataset(X_train, y_train), batch_size=64, shuffle=True)

---

## 7. Training Loop

for epoch in range(epochs):
    model.train()
    for inputs, targets in train_loader:
        inputs, targets = inputs.to(device), targets.to(device)
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()
    print(f'Epoch {epoch}: {loss.item():.4f}')

---

## 8. Evaluation

model.eval()
correct = total = 0
with torch.no_grad():
    for x, y in test_loader:
        pred = model(x.to(device)).argmax(1)
        correct += (pred == y.to(device)).sum().item()
        total += y.size(0)

print(f'Accuracy: {100*correct/total:.2f}%')

---

## 9. Save / Load Model

### Save Weights
torch.save(model.state_dict(), 'model.pt')

### Load Weights
model.load_state_dict(torch.load('model.pt'))
model.eval()

---

## 10. Utilities

### Gradient Clipping
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)

### AMP / Mixed Precision
from torch.cuda.amp import autocast, GradScaler
scaler = GradScaler()
with autocast():
    output = model(inputs)

### Count Parameters
total = sum(p.numel() for p in model.parameters())
print(f'Total params: {total:,}')

"""# Plotly"""

### Scatter Plot
fig = px.scatter(df, x='x_col', y='y_col', color='category', size='size_col', hover_name='label')
fig.show()

### Line Plot
fig = px.line(df, x='date', y='value', color='series', markers=True)
fig.show()

### Area Plot
fig = px.area(df, x='date', y='sales', color='segment', groupnorm='fraction')
fig.show()

### Bar Chart
fig = px.bar(df, x='category', y='total', color='subgroup', text_auto=True)
fig.update_layout(barmode='group')
fig.show()

### Treemap
fig = px.treemap(df, path=['continent','country'], values='pop')
fig.show()

### Sunburst
fig = px.sunburst(df, path=['continent','country','city'], values='pop')
fig.show()

---

## 2. Distribution Plots

### Histogram
fig = px.histogram(df, x='age', nbins=30, color='gender', marginal='box')
fig.show()

### Box Plot
fig = px.box(df, x='group', y='metric', points='all')
fig.show()

### Violin Plot
fig = px.violin(df, y='score', x='method', color='method', box=True, points='all')
fig.show()

### Strip Plot
fig = px.strip(df, x='condition', y='value', color='condition', jitter=0.3)
fig.show()

### 2D Density Heatmap
fig = px.density_heatmap(df, x='x', y='y', nbinsx=40, nbinsy=40, color_continuous_scale='Viridis')
fig.show()

### 2D Density Contour
fig = px.density_contour(df, x='feat1', y='feat2', color='cluster')
fig.show()

---

## 3. Categorical Comparisons

### Polar Bar
fig = px.bar_polar(df, r='frequency', theta='direction', color='season')
fig.show()

### Funnel Chart
fig = px.funnel(df, x='stage', y='users')
fig.show()

### Funnel Area
fig = px.funnel_area(df, names='stage', values='users')
fig.show()

### Parallel Categories
fig = px.parallel_categories(df, dimensions=['gender','class','pass'])
fig.show()

### Parallel Coordinates
fig = px.parallel_coordinates(df, color='target', dimensions=df.columns[2:])
fig.show()

---

## 4. Geographic Charts

### Choropleth Map
fig = px.choropleth(df, locations='iso_alpha', color='gdpPercap', hover_name='country', projection='natural earth')
fig.show()

### Geo Scatter
fig = px.scatter_geo(df, lat='lat', lon='lon', color='group', size='pop')
fig.show()

### Geo Line
fig = px.line_geo(df, lat='lat', lon='lon', color='route_id')
fig.show()

---

## 5. Timeline & Stage Diagrams

### Timeline (Gantt Chart)
fig = px.timeline(df, x_start='start', x_end='finish', y='task', color='owner')
fig.update_yaxes(autorange='reversed')
fig.show()

### Icicle
fig = px.icicle(df, path=['phase','subphase','task'], values='hours')
fig.show()

---

## 6. 3D Plots

### 3D Scatter
fig = px.scatter_3d(df, x='x', y='y', z='z', color='label', symbol='label')
fig.show()

### 3D Line
fig = px.line_3d(df, x='x', y='y', z='z', color='trial')
fig.show()

### Volume Plot
fig = px.volume(vol_array)  # vol_array is a 3D NumPy array
fig.show()

---

## 7. Useful Plotly Utilities

### Update Layout
fig.update_layout(title='My title', xaxis_title='X', yaxis_title='Y', template='plotly_white')

### Update Marker
fig.update_traces(marker=dict(size=10, opacity=0.7))

### Save to HTML
fig.write_html('figure.html', include_plotlyjs='cdn')

### Set Default Renderer
import plotly.io as pio
pio.renderers.default = 'notebook'

---

## 🔧 One-time Setup

```python
import plotly.express as px
import plotly.io as pio

pio.renderers.default = 'notebook'  # makes fig.show() unnecessary
px.defaults.template = 'plotly_white'
px.defaults.width = 800
px.defaults.height = 500

"""# Langchain"""

# 🦜 LangChain Cheatsheet (Python)

## 1. Setup & Initialization

### Install LangChain
pip install langchain openai

### Load Environment Variables
from dotenv import load_dotenv
load_dotenv()

### Import Core Modules
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

---

## 2. Basic LLM Usage

### Initialize LLM
llm = OpenAI(temperature=0.7, openai_api_key=os.getenv("OPENAI_API_KEY"))

### Simple Prompt Completion
prompt = "What is the capital of France?"
response = llm(prompt)
print(response)

---

## 3. Using PromptTemplate

### Create Prompt Template
template = PromptTemplate(
    input_variables=["animal_type", "pet_color"],
    template="What is a good name for a {animal_type} with {pet_color} color?"
)

### Run LLMChain
name_chain = LLMChain(llm=llm, prompt=template)
response = name_chain.run({"animal_type": "dog", "pet_color": "brown"})
print(response)

---

## 4. Using Chains

### Simple Chain with Inputs
from langchain.chains import SimpleSequentialChain

chain1 = LLMChain(llm=llm, prompt=PromptTemplate.from_template("Translate to Spanish: {input}"))
chain2 = LLMChain(llm=llm, prompt=PromptTemplate.from_template("Make it formal: {input}"))

overall_chain = SimpleSequentialChain(chains=[chain1, chain2])
overall_chain.run("Hello, how are you?")

---

## 5. Tools & Agents

### Load Tools
from langchain.agents import load_tools

tools = load_tools(["wikipedia", "llm-math"], llm=llm)

### Create Agent
from langchain.agents import initialize_agent, AgentType

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

### Run Agent
agent.run("Who is Marie Curie’s husband and what was his major discovery?")

---

## 6. Memory

### Add Memory to Chain
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()

conversation = LLMChain(
    llm=llm,
    prompt=PromptTemplate.from_template("You are a helpful assistant. {history} Human: {input}\nAI:"),
    memory=memory
)

conversation.run("What's the weather like today?")
conversation.run("What did I just ask you?")

---

## 7. Vectorstores & Embeddings (Optional)

### Load Embeddings
from langchain.embeddings import OpenAIEmbeddings
embedding = OpenAIEmbeddings()

### FAISS Vector Store
from langchain.vectorstores import FAISS

db = FAISS.from_texts(["hello world", "how are you"], embedding=embedding)
docs = db.similarity_search("hello")

---

## 8. Retrieval-Augmented Generation (RAG)

### Create Retriever
retriever = db.as_retriever()

### RetrievalQA Chain
from langchain.chains import RetrievalQA

qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
qa_chain.run("What is this about?")

---

## 9. Save & Load Chains

### Save Chain
chain.save("my_chain.json")

### Load Chain
from langchain.chains import load_chain
loaded = load_chain("my_chain.json")

---

## 10. Set Default OpenAI Key (optional)

### Environment Setup
import os
os.environ["OPENAI_API_KEY"] = "sk-..."

"""# NumPy"""

# 🧮 NumPy Cheatsheet

## 1. Setup

### Import NumPy
import numpy as np

---

## 2. Creating Arrays

### From List
a = np.array([1, 2, 3])

### Zeros / Ones
z = np.zeros((2, 3))
o = np.ones((2, 3))

### Range / Linspace
r = np.arange(0, 10, 2)
l = np.linspace(0, 1, 5)

### Identity Matrix
I = np.eye(3)

### Random Arrays
rand = np.random.rand(2, 2)
randn = np.random.randn(2, 2)
randint = np.random.randint(0, 10, (2, 3))

---

## 3. Array Inspection

### Shape & Size
a.shape
a.size

### Data Type
a.dtype

### Reshape
a = a.reshape(3, 2)

---

## 4. Indexing & Slicing

### Access Elements
a[0, 1]

### Slice Rows/Cols
a[1:, :2]

### Boolean Masking
a[a > 5]

### Fancy Indexing
a[[0, 2], [1, 0]]

---

## 5. Math Operations

### Elementwise Math
a + b
a * b
a ** 2
np.exp(a)
np.sqrt(a)

### Matrix Multiplication
np.dot(a, b)
a @ b

### Aggregation
a.sum()
a.mean()
a.std()
a.max()
a.min()
a.argmax()
a.cumsum()

---

## 6. Broadcasting

### Scalar Operations
a + 3
a * 2

### Row / Column Broadcasting
a + np.array([[1], [2]])

---

## 7. Linear Algebra

### Transpose
a.T

### Inverse
np.linalg.inv(a)

### Determinant
np.linalg.det(a)

### Eigenvalues
np.linalg.eig(a)

---

## 8. Random Seed & Sampling

### Set Seed
np.random.seed(42)

### Shuffle Array
np.random.shuffle(a)

### Random Choice
np.random.choice(a, size=3, replace=False)

---

## 9. Save & Load

### Save to .npy
np.save('arr.npy', a)

### Load .npy
a = np.load('arr.npy')

### Save to CSV
np.savetxt('arr.csv', a, delimiter=',')

### Load CSV
a = np.loadtxt('arr.csv', delimiter=',')

---

## 10. Useful Utilities

### Stack Arrays
np.vstack([a, b])
np.hstack([a, b])

### Split Arrays
np.split(a, 2)
np.array_split(a, 3)

### Unique Elements
np.unique(a)

### Clip Values
np.clip(a, 0, 1)

### Replace NaNs
np.nan_to_num(a)

"""# Scikit Learn"""

# 🤖 Scikit-learn Cheatsheet

## 1. Setup

### Import Core Modules
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

---

## 2. Dataset Loading

### Built-in Dataset
from sklearn.datasets import load_iris
data = load_iris()
X, y = data.data, data.target

### Custom Dataset
import pandas as pd
df = pd.read_csv('data.csv')
X = df.drop('target', axis=1)
y = df['target']

---

## 3. Train/Test Split

### Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

---

## 4. Preprocessing

### Standard Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

---

## 5. Model Training

### Logistic Regression
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)

### Random Forest
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)

### SVM
from sklearn.svm import SVC
model = SVC()
model.fit(X_train, y_train)

---

## 6. Predictions & Evaluation

### Make Predictions
y_pred = model.predict(X_test)

### Accuracy
accuracy_score(y_test, y_pred)

### Classification Report
print(classification_report(y_test, y_pred))

---

## 7. Cross-Validation

### k-Fold Cross Validation
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5)
print(scores.mean())

---

## 8. Pipelines

### Create Pipeline
from sklearn.pipeline import Pipeline

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('clf', LogisticRegression())
])

pipe.fit(X_train, y_train)
pipe.score(X_test, y_test)

---

## 9. Hyperparameter Tuning

### Grid Search
from sklearn.model_selection import GridSearchCV

params = {'C': [0.1, 1, 10]}
grid = GridSearchCV(LogisticRegression(), params, cv=5)
grid.fit(X_train, y_train)
print(grid.best_params_)
print(grid.best_score_)

---

## 10. Common Models

### Linear Regression
from sklearn.linear_model import LinearRegression
model = LinearRegression()

### Decision Tree
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()

### KNN
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=5)

### Naive Bayes
from sklearn.naive_bayes import GaussianNB
model = GaussianNB()

### Gradient Boosting
from sklearn.ensemble import GradientBoostingClassifier
model = GradientBoostingClassifier()

"""# Seaborn"""

# 🎨 Seaborn Cheatsheet

## 1. Setup

### Import Libraries
import seaborn as sns
import matplotlib.pyplot as plt

### Load Built-in Dataset
df = sns.load_dataset("tips")

---

## 2. Distribution Plots

### Histogram
sns.histplot(df['total_bill'])
plt.show()

### KDE Plot
sns.kdeplot(df['total_bill'], fill=True)
plt.show()

### Histogram + KDE
sns.displot(df['total_bill'], kde=True)
plt.show()

### Box Plot
sns.boxplot(x='day', y='total_bill', data=df)
plt.show()

### Violin Plot
sns.violinplot(x='day', y='total_bill', data=df)
plt.show()

### Strip Plot (Scatter w/ Jitter)
sns.stripplot(x='day', y='total_bill', data=df, jitter=True)
plt.show()

---

## 3. Categorical Plots

### Count Plot
sns.countplot(x='day', data=df)
plt.show()

### Bar Plot (Mean & CI)
sns.barplot(x='day', y='tip', data=df)
plt.show()

### Swarm Plot (Non-overlapping dots)
sns.swarmplot(x='day', y='total_bill', data=df)
plt.show()

### Point Plot
sns.pointplot(x='time', y='tip', hue='sex', data=df)
plt.show()

---

## 4. Relational Plots

### Scatter Plot
sns.scatterplot(x='total_bill', y='tip', data=df)
plt.show()

### Line Plot
sns.lineplot(x='size', y='tip', data=df)
plt.show()

### Relplot (Faceted)
sns.relplot(x='total_bill', y='tip', hue='sex', col='time', data=df)
plt.show()

---

## 5. Matrix Plots

### Heatmap
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()

### Clustermap
sns.clustermap(corr, annot=True, cmap='viridis')
plt.show()

---

## 6. Pairwise Plots

### Pairplot
sns.pairplot(df, hue='sex')
plt.show()

### Jointplot
sns.jointplot(x='total_bill', y='tip', data=df, kind='reg')
plt.show()

---

## 7. Themes & Styles

### Set Style
sns.set_style('whitegrid')

### Set Color Palette
sns.set_palette('pastel')

### Set Figure Size
plt.figure(figsize=(8, 5))

---

## 8. Save Plot

### Save to File
plt.savefig("plot.png", dpi=300, bbox_inches='tight')

"""# Matplotlib"""

# 📈 Matplotlib Cheatsheet

## 1. Setup

### Import Modules
import matplotlib.pyplot as plt
import numpy as np

### Create Sample Data
x = np.linspace(0, 10, 100)
y = np.sin(x)

---

## 2. Basic Plotting

### Line Plot
plt.plot(x, y)
plt.show()

### Scatter Plot
plt.scatter(x, y)
plt.show()

### Bar Plot
categories = ['A', 'B', 'C']
values = [5, 3, 7]
plt.bar(categories, values)
plt.show()

### Horizontal Bar
plt.barh(categories, values)
plt.show()

### Histogram
data = np.random.randn(1000)
plt.hist(data, bins=30)
plt.show()

### Box Plot
plt.boxplot(data)
plt.show()

---

## 3. Customization

### Labels & Title
plt.plot(x, y)
plt.title("Sine Curve")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

### Grid
plt.plot(x, y)
plt.grid(True)
plt.show()

### Legends
plt.plot(x, y, label='Sine')
plt.legend()
plt.show()

---

## 4. Subplots

### 1 Row, 2 Columns
plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title("Left")

plt.subplot(1, 2, 2)
plt.plot(x, -y)
plt.title("Right")

plt.tight_layout()
plt.show()

---

## 5. Figures

### Create New Figure
fig = plt.figure(figsize=(6, 4))
plt.plot(x, y)
plt.show()

### Save Figure
plt.plot(x, y)
plt.savefig("plot.png", dpi=300, bbox_inches='tight')

---

## 6. Styles & Appearance

### Set Style
plt.style.use('ggplot')
plt.plot(x, y)
plt.show()

### Colors & Markers
plt.plot(x, y, color='purple', linestyle='--', marker='o')
plt.show()

---

## 7. Axes Object API

### Create Axes
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("With Axes Object")
ax.set_xlabel("x")
ax.set_ylabel("y")
plt.show()

---

## 8. Advanced Plots

### Fill Between
plt.fill_between(x, y, alpha=0.3)
plt.plot(x, y)
plt.show()

### Log Scale
plt.semilogy(x, np.exp(x))
plt.show()

### Twin Axes
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(x, y, 'g-')
ax2.plot(x, np.cos(x), 'b--')
plt.show()

"""# Tensorflow"""

# ⚡️ TensorFlow Cheatsheet

## 1. Setup

### Import TensorFlow
import tensorflow as tf

### Check Version
tf.__version__

### Set Seed
tf.random.set_seed(42)

---

## 2. Creating Tensors

### Constant
x = tf.constant([[1., 2.], [3., 4.]])

### Variable
v = tf.Variable(tf.random.normal([3, 3]))

### Zeros / Ones
z = tf.zeros([2, 3])
o = tf.ones([2, 3])

### Range
r = tf.range(10)

### Random Normal
rn = tf.random.normal([2, 2])

---

## 3. Tensor Operations

### Element-wise Math
y = x + 3

### Matrix Multiplication
prod = tf.matmul(x, v)

### Reshape
x = tf.reshape(x, [-1])

### Concatenate
cat = tf.concat([x, y], axis=0)

---

## 4. GPU / Device Placement

### List GPUs
tf.config.list_physical_devices('GPU')

### Run on GPU
with tf.device('/GPU:0'):
    y = x * 2

---

## 5. Automatic Differentiation

### GradientTape
with tf.GradientTape() as tape:
    tape.watch(x)
    y = tf.reduce_sum(x ** 2)
grad = tape.gradient(y, x)

---

## 6. Building a Keras Model

### Sequential Model
from tensorflow.keras import layers, models
model = models.Sequential([
    layers.Dense(128, activation='relu', input_shape=(784,)),
    layers.Dense(10, activation='softmax')
])

### Compile
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

---

## 7. Training

### Fit
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

---

## 8. Evaluation & Prediction

### Evaluate
model.evaluate(X_test, y_test)

### Predict
preds = model.predict(X_new)

---

## 9. tf.data Pipeline

### Create Dataset
ds = tf.data.Dataset.from_tensor_slices((X_train, y_train))
ds = ds.shuffle(1000).batch(32).prefetch(tf.data.AUTOTUNE)

---

## 10. Saving & Loading

### Save Full Model
model.save('model.h5')

### Load Model
model = tf.keras.models.load_model('model.h5')

### Save Weights
model.save_weights('weights.ckpt')

### Load Weights
model.load_weights('weights.ckpt')

---

## 11. Callbacks

### Early Stopping
from tensorflow.keras.callbacks import EarlyStopping
es = EarlyStopping(patience=3, restore_best_weights=True)
model.fit(X_train, y_train, epochs=50, callbacks=[es])

---

## 12. Mixed Precision

### Enable Mixed Precision
from tensorflow.keras import mixed_precision
mixed_precision.set_global_policy('mixed_float16')