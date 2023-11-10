import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from yellowbrick.regressor import ResidualsPlot

# Leitura dos dados
base_avaliacao_docencia = pd.read_csv('C:\\Users\\Adalberto\\Desktop\\Projetos\\regressao_linear\\avaliacao_docencia.csv', sep=";")


# Filtrar por nome de docente específico
base_avaliacao_docencia = base_avaliacao_docencia[base_avaliacao_docencia['nome_docente'] == 'FLAVIUS DA LUZ E GORGONIO']

# Remover valores ausentes
base_avaliacao_docencia = base_avaliacao_docencia.drop(columns='nome_docente')
print(base_avaliacao_docencia)
# Plotar um heatmap da matriz de correlação
sns.heatmap(base_avaliacao_docencia.corr())
# Exibir o gráfico
plt.show()


X_base_docencia = base_avaliacao_docencia ['qtd_discentes' ].values

Y_base_docencia = base_avaliacao_docencia ['postura_profissional_media'].values

X_base_docencia = base_avaliacao_docencia ['qtd_discentes' ].values

Y_base_docencia = base_avaliacao_docencia ['atuacao_profissional_media'].values

X_base_docencia = base_avaliacao_docencia ['qtd_discentes' ].values

Y_base_docencia = base_avaliacao_docencia ['autoavaliacao_aluno_media'].values