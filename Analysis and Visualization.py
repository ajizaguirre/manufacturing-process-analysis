# --- Analysis & Visualization ---

# Set plot style
sns.set(style="whitegrid", palette="viridis")

# 1. Correlation Analysis
plt.figure(figsize=(10, 8))
correlation_matrix = df[['Temperature_C', 'Machine_Speed_RPM', 'Production_Quality_Score', 'Vibration_Level_mms', 'Energy_Consumption_kWh']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='viridis', fmt=".2f")
plt.title('Correlation Matrix of Manufacturing Process Variables', fontsize=16, fontweight='bold')
plt.show()

# 2. Quality Score Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Production_Quality_Score'], kde=True, bins=30)
plt.title('Distribution of Production Quality Scores', fontsize=16, fontweight='bold')
plt.xlabel('Production Quality Score')
plt.ylabel('Frequency')
plt.show()

# 3. Impact of Machine Speed on Quality
plt.figure(figsize=(12, 7))
sns.scatterplot(x='Machine_Speed_RPM', y='Production_Quality_Score', data=df, alpha=0.6, hue='Optimal_Conditions_Flag')
plt.title('Machine Speed vs. Production Quality', fontsize=16, fontweight='bold')
plt.xlabel('Machine Speed (RPM)')
plt.ylabel('Production Quality Score')
plt.legend(title='Optimal Conditions')
plt.show()

# 4. Impact of Temperature on Quality
plt.figure(figsize=(12, 7))
sns.scatterplot(x='Temperature_C', y='Production_Quality_Score', data=df, alpha=0.6, hue='Optimal_Conditions_Flag')
plt.title('Temperature vs. Production Quality', fontsize=16, fontweight='bold')
plt.xlabel('Temperature (°C)')
plt.ylabel('Production Quality Score')
plt.legend(title='Optimal Conditions')
plt.show()