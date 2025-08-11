import csv
import os
from config import ONBOARDING_TASKS

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

def get_onboardees_from_csv(filename):
    filepath = os.path.join(DATA_DIR, filename)
    data = []
    with open(filepath, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            role = row["role"].strip().lower()
            onboardee = row["onboardee"].strip()
            
            if row["role"] in ONBOARDING_TASKS:
                data.append({
                    "onboardee": onboardee,
                    "role": role
                })
            else:
                print(f"❗️❗️Warning: role '{role}' not found in onboarding tasks for onboardee '{onboardee}'!")

    return data