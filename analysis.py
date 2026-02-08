# ===============================
# A/B TEST ANALYSIS - WEBSITE REDESIGN
# ===============================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency, ttest_ind

# -------------------------------
# 1. Load Dataset
# -------------------------------
df = pd.read_csv("ab_test_data.csv")

# Separate groups
control = df[df["group"] == "control"]
treatment = df[df["group"] == "treatment"]

# -------------------------------
# 2. KPI CALCULATIONS
# -------------------------------

# Conversion Rate
control_cr = control["converted"].mean()
treatment_cr = treatment["converted"].mean()

# Revenue per User
control_rev = control["revenue"].mean()
treatment_rev = treatment["revenue"].mean()

# Avg Time on Site
control_time = control["time_on_site"].mean()
treatment_time = treatment["time_on_site"].mean()

print("KPI SUMMARY")
print("---------------------")
print(f"Control Conversion Rate: {control_cr:.4f}")
print(f"Treatment Conversion Rate: {treatment_cr:.4f}")
print(f"Control Revenue/User: ₹{control_rev:.2f}")
print(f"Treatment Revenue/User: ₹{treatment_rev:.2f}")
print(f"Control Time on Site: {control_time:.2f} sec")
print(f"Treatment Time on Site: {treatment_time:.2f} sec")

# -------------------------------
# 3. VISUALIZATION
# -------------------------------

# Conversion Rate Bar Chart
plt.figure()
plt.bar(["Control", "Treatment"], [control_cr, treatment_cr])
plt.title("Conversion Rate Comparison")
plt.ylabel("Conversion Rate")
plt.show()

# Revenue Comparison
plt.figure()
plt.bar(["Control", "Treatment"], [control_rev, treatment_rev])
plt.title("Average Revenue per User")
plt.ylabel("Revenue")
plt.show()

# -------------------------------
# 4. HYPOTHESIS TESTING
# -------------------------------

# ---- A. Chi-Square Test (Conversion Rate) ----
conversion_table = [
    [control["converted"].sum(), len(control) - control["converted"].sum()],
    [treatment["converted"].sum(), len(treatment) - treatment["converted"].sum()]
]

chi2, p_value, dof, expected = chi2_contingency(conversion_table)

print("\nCHI-SQUARE TEST (Conversion Rate)")
print("--------------------------------")
print(f"P-value: {p_value:.4f}")

if p_value < 0.05:
    print("Result: Statistically Significant (Reject Null Hypothesis)")
else:
    print("Result: Not Statistically Significant")

# ---- B. T-Test (Revenue) ----
t_stat_rev, p_rev = ttest_ind(
    control["revenue"],
    treatment["revenue"],
    equal_var=False
)

print("\nT-TEST (Revenue)")
print("----------------")
print(f"P-value: {p_rev:.4f}")

# ---- C. T-Test (Time on Site) ----
t_stat_time, p_time = ttest_ind(
    control["time_on_site"],
    treatment["time_on_site"],
    equal_var=False
)

print("\nT-TEST (Time on Site)")
print("---------------------")
print(f"P-value: {p_time:.4f}")

# -------------------------------
# 5. FINAL BUSINESS CONCLUSION
# -------------------------------
print("\nFINAL CONCLUSION")
print("----------------")
if p_value < 0.05:
    print("The new website layout significantly improved conversion rate.")
else:
    print("No significant improvement detected.")
