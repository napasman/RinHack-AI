import pandas as pd
import requests
import time
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from imblearn.over_sampling import BorderlineSMOTE
from imblearn.pipeline import Pipeline

df = pd.read_csv("network_traffic.csv")

print("Columns in the dataset:", df.columns)

categorical_features = ["protocol", "source_ip", "destination_ip"]
for column in categorical_features:
    if column in df.columns:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
    else:
        print(f"Warning: Column {column} not found in the dataset.")

if "threat" in df.columns:
    y = df["threat"].apply(lambda x: 1 if x != "Normal" else 0)
    X = df.drop(["time_stamp", "threat"], axis=1)
else:
    raise ValueError("Column 'threat' not found in the dataset.")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

smote = BorderlineSMOTE()
rf_classifier = RandomForestClassifier(n_estimators=20, random_state=42)
pipeline_rf = Pipeline([("smote", smote), ("classifier", rf_classifier)])
pipeline_rf.fit(X_train, y_train)

ada_boost = AdaBoostClassifier(n_estimators=50, random_state=42)
ada_boost.fit(X_train, y_train)

xgb_classifier = XGBClassifier(use_label_encoder=False, eval_metric="logloss")
xgb_classifier.fit(X_train, y_train)

models = {
    "Random Forest": pipeline_rf,
    "AdaBoost": ada_boost,
    "XGBoost": xgb_classifier,
}
for name, model in models.items():
    y_pred = model.predict(X_test)
    print(f"Results for {name}:")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("\n")

    for i, (index, row) in enumerate(X_test.iterrows()):
        # Prepare the dictionary for each prediction
        traffic_data = {
            "timestamp": str(df.loc[index, "time_stamp"]),
            "source_ip": str(df.loc[index, "source_ip"]),
            "destination_ip": str(df.loc[index, "destination_ip"]),
            "protocol": str(df.loc[index, "protocol"]),
            "port": str(row["port"]),
            "packet_size": str(row["packet_size"]),
            "prediction": "true" if y_pred[i] == 1 else "false",
        }

        # Encapsulate the dictionary in a list to match the expected list of TrafficDTO
        data = {"traffic": [traffic_data]}

        # Sending the request to the specified endpoint
        response = requests.post(url="http://localhost:3000/ai/traffic/add", json=data)
        print(f"Sent data for index {index}: {response.status_code}")
        time.sleep(1)  # Sleep for 1 second to mimic real-time data sending
