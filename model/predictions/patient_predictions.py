import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


not_my_data = set(globals())

# Declare some global variables
foo5 = "hii"
foo6 = 7

not_my_data


# TODO paramerize 'random_state' v1
# TODO once paramerized move 'random_state' into .yaml
# TODO
# TODO update model prediction based on input values gatherd from user
# Load and preprocess data (age, income, distance, missed_appointments)
data = pd.read_csv("../../data/patient_HEDIC_appointment_demo.csv")
X = data.drop("patient_missed_appointments", axis=1)
y = data["patient_missed_appointments"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# Train a RandomForestClassifier
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Predict on test data
y_pred = clf.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy scoring: {accuracy}")

# Print the actual and predicted values
print("Actual values:", list(y_test))
print("Predicted values:", list(y_pred))

# Print a summary of the results
print(
    f"\nOut of {len(y_test)} test cases, the model correctly predicted {int(accuracy * len(y_test))} cases, with an accuracy of {accuracy * 100}%."
)

# Print predictions for each patient
print("\nPrediction results for each patient in the test set:")
for i, (actual, predicted) in enumerate(zip(y_test, y_pred)):
    appointment_status = "miss" if predicted == 1 else "not miss"
    print(
        f"Patient {i + 1}: Predicted to {appointment_status} the appointment. Actual status: {'missed' if actual == 1 else 'not missed'}."
    )
