# Data-Driven Insights for South Africa’s Car Insurance Market

## Executive Summary

As part of AlphaCare Insurance Solutions' (ACIS) commitment to innovation in car insurance planning and marketing, an analysis of historical insurance claim data was conducted. The objective was to identify low-risk customer segments for targeted premium reductions, thereby enhancing customer acquisition and retention.
Key insights revealed significant variations in the Premium to Claims Ratio across demographic, geographic, and product-specific dimensions:

## Business Objective

The primary objective of this project is to enhance risk and predictive analytics for car insurance at ACIS. By analyzing historical insurance claim data, we aim to refine marketing strategies and identify low-risk clients who may benefit from reduced premiums.

## Objectives

1. **Understand Insurance Terminologies**:
   - Build a foundational understanding of insurance terms.

2. **Conduct A/B Hypothesis Testing**:
   - Test hypotheses to assess risk differences and margin impacts across demographics and geographic locations.

3. **Develop Predictive Models**:
   - Fit linear regression models and create machine learning models to predict total claims and optimal premium values based on various features.

4. **Report Findings**:
   - Document methodologies, findings, and recommendations to help ACIS tailor insurance products more effectively.

## Data

The dataset covers historical insurance claim data from February 2014 to August 2015.

## Tasks

### Task 1: Git and GitHub Setup

- **Create a GitHub Repository**:
  - Initialize a new repository and create a comprehensive README.
  
- **Version Control**:
  - Implement Git for version control and set up CI/CD pipelines using GitHub Actions.

- **Exploratory Data Analysis (EDA) & Statistics**:
  - Perform EDA to understand the data, identify trends, and detect outliers.
  - Regularly commit changes and document the analysis process.

### Task 2: Data Version Control (DVC)

- **Install and Configure DVC**:
  - Install DVC and configure it for managing and versioning data.

- **Data Tracking**:
  - Use DVC to track and manage dataset versions.

**DVC Setup Instructions**:

1. Initialize DVC:

  ```bash
  dvc init
  ```
  
2. Configure Remote Storage:

```bash
dvc remote add -d localremote "path/to/your/local-storage/"  #"C:/Users/getac/Documents/10 Academy/week 3/KAIMW3DVC"
```

3. Add Data to DVC:

```bash
dvc add data/MachineLearningRating_v3.txt
```

4. Commit DVC Changes:

```bash
git add .dvc/config .dvc/cache data/.gitignore
git commit -m "Add DVC configuration and data"
```

### Task 3: A/B Hypothesis Testing

- **Test Hypotheses**:
  - There are no risk differences across provinces
  - There are no risk differences between zip codes
  - There are no significant margin (profit) difference between zip codes 
  - There are not significant risk difference between Women and Men

- **Data Segmentation and Analysis**:
  - Design and implement A/B tests, segment data, and analyze results.

### Task 4: Statistical Modeling

- **Data Preparation**:
  - Handle missing data, perform feature engineering, and encode categorical variables.

- **Model Building**:
  - Implement Linear Regression, Decision Trees, Random Forests, and Gradient Boosting Machines (XGBoost).

- **Model Evaluation and Interpretability**:
  - Evaluate models using metrics such as accuracy and precision

- **Feature Importance Analysis**:
  - Analyze which features are most influential in predicting retention.

- Use SHAP (SHapley Additive exPlanations) or LIME (Local Interpretable Model-agnostic Explanations) to interpret the model's predictions and understand how individual features influence the outcomes.

- Report comparison between each model performance.


For any questions or further information, please contact [Wasihun Tesfaye](mailto:wasihunpersonal@gmail.com).
