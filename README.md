# Nutrition Customer Analysis Project

## Background and Overview

This project aims to provide in-depth insights and actionable recommendations leveraging comprehensive customer data from **Mattson Nutrition**. The analysis encompasses behavioral, demographic, psychological, and health-related attributes across two distinct periods:

- **Delta1**: 3 months prior  
- **Delta2**: 6 months prior  

The dataset initially contained **83,216 customer records** and required extensive data normalization, cleaning, and imputation.

### Primary Goals

- Identify key factors influencing customer purchasing behaviors  
- Analyze correlations between customer characteristics (age, gender, personality traits, health behaviors) and sales  
- Develop robust predictive models and customer segmentation strategies for targeted marketing and improved sales performance  

---

## Data Structure Overview

The original dataset comprised 25 columns, several containing **nested JSON structures**. Data normalization significantly expanded the dataset, extracting detailed features for analysis.

### Key Feature Categories

- **Demographic Information**: Age, gender  
- **Health Metrics**: Body Mass Index (BMI), blood pressure, sleep patterns, heart rate, stress levels  
- **Behavioral Data**: Website visits, social media interactions, mobile app logins, steps  
- **Psychological Data**: Big 5 personality traits  
- **Family Medical History**: Depression, diabetes, heart disease, cancer, Alzheimer's, Parkinson's, Crohn's, and others  

---

## Executive Summary

Critical findings from the analysis include:

- A **decline in sales post-late 2022** strongly associated with customer behavior and psychological profiles  
- **Conscientiousness and extroversion** were positively correlated with sales  
- **Older demographics** consistently showed higher purchasing activity  
- Health indicators such as **BMI, stress, and sleep quality** significantly influenced customer engagement  

Insights were developed using:

- Rigorous preprocessing  
- Clustering analysis  
- Principal Component Analysis (PCA)  
- Predictive regression modeling  

---

## Insights Deep Dive

### Behavioral Trends

- **Social Media Engagement**: Strong correlation with sales; supports investment in digital marketing  
- **Mobile App Utilization**: Higher app engagement aligns with increased sales  

### Demographic Insights

- **Age**: Older customers had higher average sales; opportunity for age-focused marketing  
- **Gender**: Preserved gender proportions using imputation allowed deeper segmentation  

### Health & Psychological Insights

- **Personality Traits**: High conscientiousness and extroversion predicted higher purchasing  
- **BMI**: Overweight and obese groups showed distinct buying behaviors  
- **Stress & Sleep**: Higher stress and lower sleep quality linked to reduced sales  

---

## Recommendations

### Strategic Marketing

- **Target Personality Traits**: Focus campaigns on high-conscientious and extroverted users  
- **Age-Specific Messaging**: Customize communications for older customers  

### Digital Channel Optimization

- **Invest in App & Social Media**: Enhance budget for digital touchpoints with proven sales impact  

### Health & Wellness Initiatives

- **BMI-Specific Campaigns**: Launch programs tailored to customers in overweight/obese categories  
- **Stress Reduction Programs**: Promote sleep and stress-reducing services to boost engagement  

---

## Caveats and Assumptions

- Minor bias possible due to imputation methods, though distributions were preserved  
- Some behaviors may reflect **post-pandemic anomalies**  
- Assumes relative stability in psychological and behavioral variables over time  

---

## Technical Notes

### Data Normalization & Imputation

- Flattened nested structures  
- Applied random sampling, median, and multi-feature imputations  
- Categorical variables were dummy coded  

### Dimensionality Reduction & Clustering

- PCA was used to simplify data while preserving variance  
- Enabled effective customer segmentation  

### Regression Modeling

- Models used: **KNN**, **Decision Tree**, **Random Forest**, **Voting Regressor**  
- GridSearchCV was used for hyperparameter tuning  
- Final models prioritized interpretability and accuracy  

---

## Project Structure

- `meta-data.txt`: Preprocessing logs and modeling decisions  
- `predictions.xlsx`: Results of regression models and scenario simulations  
- `.pkl` files: Serialized models, scalers, and PCA objects  

---
