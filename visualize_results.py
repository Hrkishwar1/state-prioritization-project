import pandas as pd
import matplotlib.pyplot as plt

# Load your environmental scores CSV
df = pd.read_csv("env_plastic_scores.csv")

# Sort states by environmental score
df_sorted = df.sort_values(by="EnvScore", ascending=False)

# Create the horizontal bar chart
plt.figure(figsize=(12, 8))
bars = plt.barh(df_sorted["State"], df_sorted["EnvScore"], color="seagreen")
plt.xlabel("Environmental Score (0–10)")
plt.title("Environmental Policy Strength by U.S. State")
plt.gca().invert_yaxis()  # Highest on top
plt.tight_layout()

# Add text annotations for plastic bag bans
for bar, ban in zip(bars, df_sorted["PlasticLawCount"]):
    label = "🛍️ Ban" if ban == 1 else ""
    plt.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2, label, va='center')

plt.show()
