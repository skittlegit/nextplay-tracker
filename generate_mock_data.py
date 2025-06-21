import pandas as pd
import random
from datetime import datetime, timedelta
import os

# Player names to simulate
players = ["Aryan", "Zizou", "Sujit"]

# Generate random date range
start_date = datetime.strptime("2025-01-01", "%Y-%m-%d")
end_date = datetime.strptime("2025-06-01", "%Y-%m-%d")

data = []

for _ in range(100):  # Generate 100 entries
    date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    player = random.choice(players)
    sprint = round(random.uniform(5.0, 8.0), 2)
    juggles = random.randint(50, 250)
    dribble = random.randint(4, 10)
    goals = random.randint(0, 3)
    assists = random.randint(0, 2)
    notes = ""

    data.append([date.strftime("%Y-%m-%d"), player, sprint, juggles, dribble, goals, assists, notes])

# Create folder if not exists
if not os.path.exists("data"):
    os.makedirs("data")

# Save to CSV
df = pd.DataFrame(data, columns=["Date", "Player", "Sprint", "Juggles", "Dribble", "Goals", "Assists", "Notes"])
df.to_csv("data/player_stats.csv", index=False)

print("✅ Mock data generated and saved to data/player_stats.csv")
