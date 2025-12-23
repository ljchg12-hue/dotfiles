---
name: csv-analysis
description: Automated CSV data analysis with statistical insights, pattern detection, visualization recommendations, and anomaly detection
---

# CSV Analysis Skill

Comprehensive CSV data analysis with automatic insight generation, statistical analysis, pattern detection, and visualization recommendations.

## When to Use This Skill

Activate this skill when the user:
- Requests CSV file analysis
- Needs data insights from tabular data
- Wants statistical analysis
- Asks about data patterns or trends
- Mentions "analyze CSV", "data analysis", "spreadsheet analysis"
- Needs data cleaning or validation
- Wants visualization recommendations
- Requires anomaly or outlier detection

## Core Capabilities

### 1. Statistical Analysis
- Descriptive statistics (mean, median, mode, std dev)
- Distribution analysis (normal, skewed, bimodal)
- Correlation analysis
- Percentiles and quartiles
- Variance and standard deviation
- Missing data analysis
- Data type inference

### 2. Pattern Detection
- Trend identification (upward, downward, seasonal)
- Periodic patterns (daily, weekly, monthly, yearly)
- Clustering and grouping
- Outlier detection
- Correlation patterns
- Time series patterns
- Categorical frequency analysis

### 3. Data Quality Assessment
- Missing value detection
- Duplicate row identification
- Data type consistency check
- Range and boundary validation
- Format validation (dates, emails, phone numbers)
- Encoding issues detection
- Schema validation

### 4. Anomaly Detection
- Statistical outliers (z-score, IQR method)
- Time series anomalies
- Categorical anomalies
- Multivariate anomalies
- Contextual outliers
- Collective anomalies

### 5. Visualization Recommendations
- Chart type suggestions (bar, line, scatter, pie, heatmap)
- Best practices for data presentation
- Color scheme recommendations
- Axis scaling suggestions
- Grouping and aggregation advice

### 6. Insight Generation
- Automatic summary generation
- Key findings extraction
- Trend interpretation
- Actionable recommendations
- Comparative analysis
- What-if scenarios

## Analysis Workflow

### Phase 1: Data Loading and Inspection
```
1. Load CSV file
2. Detect encoding (UTF-8, Latin-1, etc.)
3. Infer data types for each column
4. Check for headers
5. Count rows and columns
6. Display sample data (first/last N rows)
7. Identify null/missing values
```

### Phase 2: Data Profiling
```
1. Generate column-by-column statistics
2. Detect data types (numeric, categorical, datetime, text)
3. Calculate cardinality (unique values)
4. Identify primary key candidates
5. Check for duplicates
6. Analyze value distributions
7. Detect potential relationships between columns
```

### Phase 3: Statistical Analysis
```
1. Descriptive statistics for numeric columns
2. Frequency analysis for categorical columns
3. Correlation matrix
4. Distribution fitting
5. Outlier detection
6. Missing data patterns
7. Time series decomposition (if applicable)
```

### Phase 4: Pattern Recognition
```
1. Trend analysis
2. Seasonality detection
3. Clustering analysis
4. Association rules
5. Anomaly detection
6. Segment identification
```

### Phase 5: Insight Generation
```
1. Summarize key findings
2. Identify significant patterns
3. Highlight anomalies
4. Compare segments
5. Generate recommendations
6. Create visualizations
```

## Tools and Commands

### Basic CSV Inspection
```bash
# Preview first 10 rows
head -n 10 file.csv

# Preview last 10 rows
tail -n 10 file.csv

# Count rows
wc -l file.csv

# Count columns
head -n 1 file.csv | tr ',' '\n' | wc -l

# Display specific columns (column 1 and 3)
cut -d',' -f1,3 file.csv

# Sort by column
sort -t',' -k2 file.csv
```

### Data Cleaning
```bash
# Remove duplicate rows
sort file.csv | uniq > clean.csv

# Remove empty lines
grep -v '^$' file.csv > clean.csv

# Convert to Unix line endings
dos2unix file.csv

# Remove BOM (Byte Order Mark)
sed '1s/^\xEF\xBB\xBF//' file.csv > clean.csv
```

### Statistical Analysis (using awk)
```bash
# Sum of column 2
awk -F',' '{sum+=$2} END {print sum}' file.csv

# Average of column 2
awk -F',' '{sum+=$2; count++} END {print sum/count}' file.csv

# Min and max of column 2
awk -F',' 'NR==1{min=max=$2} {if($2<min) min=$2; if($2>max) max=$2} END {print "Min:", min, "Max:", max}' file.csv

# Count occurrences of values in column 1
awk -F',' '{count[$1]++} END {for(val in count) print val, count[val]}' file.csv
```

### Python-based Analysis
```python
import pandas as pd
import numpy as np

# Load CSV
df = pd.read_csv('file.csv')

# Basic info
df.info()
df.describe()

# Check for missing values
df.isnull().sum()

# Detect duplicates
df.duplicated().sum()

# Correlation matrix
df.corr()

# Value counts
df['column'].value_counts()

# Groupby analysis
df.groupby('category').agg({'value': ['mean', 'sum', 'count']})

# Outlier detection (IQR method)
Q1 = df['column'].quantile(0.25)
Q3 = df['column'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['column'] < Q1 - 1.5*IQR) | (df['column'] > Q3 + 1.5*IQR)]
```

## Analysis Templates

### Sales Data Analysis
```
Columns: Date, Product, Category, Quantity, Revenue, Region

Analysis:
1. Revenue trends over time
2. Top products by revenue
3. Regional performance comparison
4. Seasonal patterns
5. Product category breakdown
6. Average order value
7. Growth rate calculation
```

### Customer Data Analysis
```
Columns: CustomerID, Age, Gender, Location, SignupDate, LastPurchase, TotalSpent

Analysis:
1. Customer demographics (age, gender distribution)
2. Geographic distribution
3. Customer lifetime value
4. Churn analysis (last purchase date)
5. Cohort analysis by signup date
6. Spending patterns by segment
7. Customer retention rate
```

### Web Analytics Data
```
Columns: Date, PageViews, Sessions, Users, BounceRate, AvgSessionDuration

Analysis:
1. Traffic trends over time
2. User engagement metrics
3. Bounce rate analysis
4. Peak traffic periods
5. User retention patterns
6. Session duration distribution
7. Conversion funnel analysis
```

### Financial Data Analysis
```
Columns: Date, Account, Type, Amount, Category, Description

Analysis:
1. Income vs expenses
2. Category breakdown (spending patterns)
3. Monthly trends
4. Budget vs actual
5. Unusual transactions (anomalies)
6. Cash flow analysis
7. Forecast future expenses
```

## Pattern Detection Examples

### Time Series Trends
```
Trend Types:
- Upward: Values consistently increasing
- Downward: Values consistently decreasing
- Seasonal: Regular periodic patterns
- Cyclical: Irregular periodic patterns
- Random: No discernible pattern

Detection Methods:
- Moving averages
- Linear regression
- Seasonal decomposition
- Autocorrelation analysis
```

### Categorical Patterns
```
Pattern Types:
- Dominant category (80/20 rule)
- Balanced distribution
- Rare events
- Category correlations

Detection Methods:
- Frequency analysis
- Chi-square test
- Association rules
- Contingency tables
```

### Numerical Patterns
```
Pattern Types:
- Normal distribution
- Skewed distribution
- Bimodal distribution
- Uniform distribution

Detection Methods:
- Histogram analysis
- Q-Q plots
- Skewness and kurtosis
- Kolmogorov-Smirnov test
```

## Anomaly Detection Methods

### Statistical Outliers
```
Z-Score Method:
- Calculate mean and std dev
- Z-score = (value - mean) / std dev
- Flag if |Z-score| > 3

IQR Method:
- Calculate Q1 (25th percentile) and Q3 (75th percentile)
- IQR = Q3 - Q1
- Lower bound = Q1 - 1.5 * IQR
- Upper bound = Q3 + 1.5 * IQR
- Flag if value < lower bound or value > upper bound
```

### Time Series Anomalies
```
Methods:
- Moving average deviation
- ARIMA residuals
- Seasonal decomposition anomalies
- Change point detection
- Rate of change anomalies
```

### Multivariate Anomalies
```
Methods:
- Isolation Forest
- Local Outlier Factor (LOF)
- Mahalanobis distance
- One-Class SVM
- DBSCAN clustering
```

## Visualization Recommendations

### Chart Selection Guide

| Data Type | Recommended Chart | Use Case |
|-----------|------------------|----------|
| Single numeric variable | Histogram, Box plot | Distribution analysis |
| Two numeric variables | Scatter plot, Line chart | Correlation, trends |
| Categorical variable | Bar chart, Pie chart | Frequency comparison |
| Time series | Line chart, Area chart | Trend over time |
| Multiple categories | Grouped bar chart, Stacked bar chart | Category comparison |
| Correlation matrix | Heatmap | Multiple variable relationships |
| Part-to-whole | Pie chart, Treemap | Composition analysis |
| Distribution comparison | Violin plot, Box plot | Group comparison |
| Geographic data | Choropleth map, Bubble map | Spatial patterns |
| Hierarchical data | Treemap, Sunburst | Hierarchical structure |

### Best Practices
- ✅ Choose chart based on data type and question
- ✅ Use consistent color schemes
- ✅ Include clear labels and legends
- ✅ Avoid 3D charts (distort perception)
- ✅ Start y-axis at zero for bar charts
- ✅ Use log scale for wide value ranges
- ✅ Highlight key insights
- ✅ Keep visualizations simple and focused

## Example Analysis Report

### Dataset: sales_data.csv (10,000 rows)

**1. Data Overview**
```
Columns: Date, Product, Category, Quantity, Price, Revenue, Region
Rows: 10,000
Date Range: 2024-01-01 to 2024-12-31
Missing Values: 0
Duplicates: 0
```

**2. Descriptive Statistics**
```
Revenue:
  Mean: $1,245.67
  Median: $987.50
  Std Dev: $456.78
  Min: $10.00
  Max: $4,999.99

Quantity:
  Mean: 12.5 units
  Median: 10 units
  Mode: 5 units
```

**3. Key Findings**
```
- Total Revenue: $12,456,700
- Top Product: "Widget Pro" ($2.5M, 20% of revenue)
- Top Region: "North America" (45% of sales)
- Growth Rate: +15% YoY
- Seasonal Peak: Q4 (November-December, 35% of annual revenue)
- Best Day: December 15 ($125,000)
```

**4. Patterns Detected**
```
- Strong upward trend (+15% growth)
- Clear seasonal pattern (Q4 spike)
- Weekly pattern (higher sales on weekends)
- Category correlation: Electronics products correlate with accessories
```

**5. Anomalies**
```
- 15 days with revenue >3 std dev above mean (promotional events)
- 3 days with zero sales (system downtime)
- 1 product with unusually high return rate (45% vs 5% average)
```

**6. Recommendations**
```
1. Increase inventory for Q4 (35% spike expected)
2. Investigate high return rate for "Product XYZ"
3. Replicate success of "Widget Pro" in other categories
4. Expand marketing in underperforming regions
5. Analyze weekend sales drivers for weekday application
```

**7. Suggested Visualizations**
```
1. Line chart: Revenue over time (show trend and seasonality)
2. Bar chart: Top 10 products by revenue
3. Pie chart: Revenue by region
4. Heatmap: Sales by day of week and hour
5. Scatter plot: Price vs quantity (demand curve)
```

## Best Practices

### Do's
- ✅ Always check for missing and duplicate data first
- ✅ Validate data types before analysis
- ✅ Use appropriate statistical methods for data type
- ✅ Consider domain knowledge when interpreting results
- ✅ Cross-validate findings with multiple methods
- ✅ Document assumptions and limitations
- ✅ Provide context for insights
- ✅ Use visualizations to support findings

### Don'ts
- ❌ Don't ignore missing data patterns
- ❌ Don't assume correlation implies causation
- ❌ Don't use inappropriate chart types
- ❌ Don't analyze without understanding the domain
- ❌ Don't overlook data quality issues
- ❌ Don't present findings without confidence intervals
- ❌ Don't ignore outliers without investigation
- ❌ Don't use overly complex analysis when simple works

## Common Pitfalls

1. **Simpson's Paradox**: Trend disappears when data is grouped
2. **Survivorship Bias**: Only analyzing surviving/visible data
3. **Overfitting**: Finding patterns that don't generalize
4. **P-hacking**: Testing until finding significant result
5. **Data Leakage**: Using future data to predict past
6. **Aggregation Bias**: Losing important details in summaries
7. **Cherry-picking**: Selecting only supporting evidence

## Integration with Other Skills

- **data-visualization**: Create charts from analysis results
- **statistical-modeling**: Build predictive models
- **database-analysis**: Query and analyze database tables
- **report-generation**: Format analysis into reports
- **data-cleaning**: Clean data before analysis

## Output Format

Always provide:
1. **Executive Summary**: High-level findings (3-5 bullets)
2. **Data Overview**: Rows, columns, date range, data quality
3. **Descriptive Statistics**: Key metrics by column
4. **Patterns Identified**: Trends, seasonality, correlations
5. **Anomalies Detected**: Outliers and unusual patterns
6. **Key Insights**: Meaningful interpretations
7. **Recommendations**: Actionable next steps
8. **Visualization Suggestions**: Recommended charts
9. **Technical Details**: Methods used, confidence levels

## Limitations

- Cannot analyze non-CSV formats without conversion
- Large files (>100MB) may require chunking
- Complex relationships may need domain expertise
- Statistical significance depends on sample size
- Causation cannot be inferred from correlation alone
- Some patterns require specialized time series tools
- Missing data may affect accuracy

## Resources

- pandas: https://pandas.pydata.org/
- NumPy: https://numpy.org/
- matplotlib/seaborn: Data visualization libraries
- statsmodels: Statistical analysis in Python
- csvkit: Command-line CSV tools
- GNU awk: https://www.gnu.org/software/gawk/manual/
