import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import median_abs_deviation, linregress

# Your DMIPS data
iterations_per_sec = np.array([
    999560,
    1007195,
    1013042,
    1016369,
    1001256,
    973242,
    962696,
    994588,
    983867,
    984465
])

dmips = iterations_per_sec / 1757
runs = np.arange(1, len(dmips) + 1)

# Statistics
mean = np.mean(dmips)
median = np.median(dmips)
std_dev = np.std(dmips, ddof=1)
mad = median_abs_deviation(dmips, scale='normal')  # robust std dev estimate
cv = std_dev / mean
percentiles = np.percentile(dmips, [5, 25, 50, 75, 95])

print(f"Mean: {mean:.3f}")
print(f"Median: {median:.3f}")
print(f"Standard Deviation: {std_dev:.3f}")
print(f"Median Absolute Deviation (MAD): {mad:.3f}")
print(f"Coefficient of Variation (CV): {cv:.4f}")
print(f"Percentiles (5th, 25th, 50th, 75th, 95th): {percentiles}")

# Outlier detection using 1.5*IQR
q1, q3 = np.percentile(dmips, [25, 75])
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers = dmips[(dmips < lower_bound) | (dmips > upper_bound)]
print(f"Outliers: {outliers}")

# Plotting setup
plt.figure(figsize=(14, 10))

# 1) Bar chart with error bars (mean ± SD)
plt.subplot(3, 3, 1)
plt.bar(runs, dmips, color='lightblue', alpha=0.7, label='DMIPS per run')
plt.errorbar(runs, dmips, yerr=std_dev, fmt='none', ecolor='red', capsize=5, label='±1 SD')
plt.axhline(mean, color='orange', linestyle='--', label='Mean')
plt.title('Bar Chart with Error Bars')
plt.xlabel('Run Number')
plt.ylabel('DMIPS')
plt.legend()

# 2) Box plot
plt.subplot(3, 3, 2)
sns.boxplot(dmips, color='lightgreen')
plt.title('Box Plot of DMIPS')
plt.xlabel('DMIPS')

# 3) Histogram
plt.subplot(3, 3, 3)
plt.hist(dmips, bins=5, color='skyblue', edgecolor='black')
plt.title('Histogram of DMIPS')
plt.xlabel('DMIPS')
plt.ylabel('Frequency')

# 4) Violin plot
#plt.subplot(3, 3, 4)
#sns.violinplot(dmips, inner='quartile', color='lightcoral')
#plt.title('Violin Plot of DMIPS')
#plt.xlabel('DMIPS')

# 5) Run sequence plot
plt.subplot(3, 3, 5)
plt.plot(runs, dmips, marker='o', linestyle='-', color='purple')
plt.title('Run Sequence Plot')
plt.xlabel('Run Number')
plt.ylabel('DMIPS')
plt.grid(True)

# 6) Scatter plot with regression line
plt.subplot(3, 3, 6)
plt.scatter(runs, dmips, color='teal')
slope, intercept, r_value, p_value, std_err = linregress(runs, dmips)
plt.plot(runs, intercept + slope * runs, color='orange', label=f'Fit line (R²={r_value**2:.2f})')
plt.title('Scatter Plot with Trend Line')
plt.xlabel('Run Number')
plt.ylabel('DMIPS')
plt.legend()

# 7) Cumulative Distribution Function (CDF)
plt.subplot(3, 3, 4)
sorted_dmips = np.sort(dmips)
cdf = np.arange(1, len(dmips)+1) / len(dmips)
plt.plot(sorted_dmips, cdf, marker='o', linestyle='-', color='darkgreen')
plt.title('Cumulative Distribution Function (CDF)')
plt.xlabel('DMIPS')
plt.ylabel('Cumulative Probability')
plt.grid(True)

plt.tight_layout()
# Save the figure as a PNG file
plt.savefig('dmips_plot.png', dpi=300)  # You can change the filename and dpi as you like
plt.show()
