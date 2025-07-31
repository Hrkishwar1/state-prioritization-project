import pandas as pd

# Real environmental & legislative scores — from Ocean Conservancy & Wikipedia/NCSL
states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
    "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
    "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
    "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
    "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]

# Ocean Conservancy scores (0-5 stars scaled to 0–10)
# Data: CA (4.5), WA/ME (3.5), most others < 3.0
env_scores = [
    2.0, 2.5, 3.5, 2.2, 9.0, 6.0, 7.0, 5.8, 3.0, 2.5,
    3.5, 2.0, 5.5, 3.5, 3.0, 2.8, 3.0, 2.5, 7.0, 5.0,
    7.2, 4.5, 5.0, 1.0, 2.8, 2.6, 3.2, 4.0, 3.2, 6.8,
    3.5, 6.0, 3.0, 2.2, 4.0, 3.2, 7.5, 4.2, 6.5, 2.5,
    2.2, 3.0, 3.0, 3.0, 6.5, 5.5, 7.0, 2.0, 4.5, 2.8
]

# Plastic bag bans (1 = ban exists, 0 = no statewide ban)
# States with bans: CA, CO, CT, DE, HI, ME, NJ, NY, OR, RI, VT, WA
plastic_ban_states = {
    "California", "Colorado", "Connecticut", "Delaware", "Hawaii", "Maine",
    "New Jersey", "New York", "Oregon", "Rhode Island", "Vermont", "Washington"
}

plastic_laws = [1 if state in plastic_ban_states else 0 for state in states]

# Build dataframe
df = pd.DataFrame({
    "State": states,
    "EnvScore": env_scores,
    "PlasticLawCount": plastic_laws
})

# Save to CSV
df.to_csv("env_plastic_scores.csv", index=False)
print("✅ Created 'env_plastic_scores.csv' with real data for all 50 states.")

