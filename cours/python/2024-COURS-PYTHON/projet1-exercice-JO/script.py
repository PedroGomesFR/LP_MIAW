import pandas as pd
import matplotlib.pyplot as plt

# Charger le fichier Excel
df = pd.read_excel('athlete_events3.xlsx')

# Créer un DataFrame avec le nombre de sportifs uniques par année
df_comptage = df.groupby('Year')['Name'].nunique().reset_index()
df_comptage.columns = ['Année', 'Nombre de sportifs']

# Créer le graphique
plt.figure(figsize=(15, 6))
plt.bar(df_comptage['Année'], df_comptage['Nombre de sportifs'])
plt.title('Nombre de sportifs par année')
plt.xlabel('Année')
plt.ylabel('Nombre de sportifs')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()