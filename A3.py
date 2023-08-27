import pandas
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

dataframe = pandas.read_excel(r"Lab Session1 Data.xlsx", sheet_name="Purchase data")
dframe=dataframe.iloc[0:10,0:5]

dframe['Label'] = dframe['Payment (Rs)'].apply(lambda x: 'RICH' if x > 200 else 'POOR')
print(dframe)
x = dframe.drop(['Customer', 'Payment (Rs)', 'Label'], axis=1)
y = dframe['Label']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

model = RandomForestClassifier(random_state=42)
model.fit(x_train_scaled, y_train)

y_pred = model.predict(x_test_scaled)

print(classification_report(y_test, y_pred))