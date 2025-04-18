# Nutrition Customer Analysis Project

## Background and Overview

This project delivers actionable insights using rich customer data from **Mattson Nutrition**. The dataset captures behavioral, demographic, psychological, and health data across two reference periods:

- **Delta1**: 3 months prior  
- **Delta2**: 6 months prior

The original data included **83,216 customer records**, with extensive preprocessing required—such as JSON flattening, imputation, encoding, and standardization.

### Primary Goals

- Identify behavioral and psychological predictors of purchasing behavior  
- Analyze correlations between customer attributes (age, gender, health indicators) and sales  
- Develop predictive models for segmentation and revenue optimization  
- Conduct “what-if” analyses to simulate marketing or behavioral interventions  

---

## Data Structure Overview

The original dataset contained **25 columns**, many with **nested JSON structures**, which were normalized to create a rich, wide-format dataset.

### Key Feature Categories

- **Demographics**: Age, gender  
- **Health Metrics**: BMI, blood pressure, sleep (REM/Deep/Light), heart rate, stress  
- **Behavioral Data**: App logins, social media interactions, website visits, steps  
- **Psychological Data**: Big 5 traits — Conscientiousness, Openness, Extroversion, Agreeableness, Neuroticism  
- **Family History**: Depression, diabetes, heart disease, cancer, Alzheimer’s, Parkinson’s, etc.  

---

## Executive Summary

Key insights:

- **Sales dropped after late 2022**, strongly linked to health behaviors and psychological traits  
- Customers high in **conscientiousness and extroversion** were consistently higher spenders  
- **Older individuals** showed stronger purchase behaviors  
- High **stress** and poor **sleep quality** were linked to lower sales  

These patterns were extracted through:

- Preprocessing pipelines for nested JSON  
- PCA for dimensionality reduction  
- Clustering (e.g., KMeans)  
- Regression and classification modeling  

---

## Insights Deep Dive

### Behavioral Trends

- Customers more engaged on **social media** and **mobile apps** had higher sales  
- Digital behaviors are strong predictors of purchasing patterns  

### Demographic Signals

- **Age** was directly proportional to purchasing behavior  
- Imputed **gender** preserved population balance, enabling unbiased segmentation  

### Health & Psychology

- **Personality traits** like conscientiousness and extroversion highly influenced purchase intent  
- **BMI categories** revealed distinct buying trends—overweight/obese customers had different engagement patterns  
- Elevated **stress** and limited **REM/Deep sleep** correlated with low engagement and sales  

---

## Strategic Recommendations

### Targeted Marketing

- **Personality-Driven Campaigns**: Prioritize marketing for highly conscientious or extroverted users  
- **Age-Specific Targeting**: Leverage age group segmentation for personalized outreach  

### Digital Channel Optimization

- Enhance UX and investment in **app features** and **social media engagement**  

### Health & Wellness Initiatives

- Run campaigns around **wellness**, **BMI**, and **sleep quality improvement**  
- Launch stress management product bundles for high-stress segments  

---

## Caveats and Assumptions

- Data imputation (random, median, group-based) may introduce minor bias  
- Post-pandemic consumer behavior shifts may reduce model generalizability  
- Personality and behavior assumed relatively stable across observation periods  

---

## Technical Implementation

### Data Processing

- Normalized nested structures (e.g., delta1/delta2 JSON fields)  
- Applied **random**, **median**, and **multi-feature** imputation strategies  
- One-hot encoded all relevant categorical values  

### Dimensionality Reduction

- Used **Principal Component Analysis (PCA)** to reduce feature space  
- Retained top components explaining the majority of variance  

### Machine Learning Models Used

1. **K-Nearest Neighbors (KNN)**  
   - Used as a baseline for nonlinear regression  
   - Captures local similarity in behavioral and health metrics  

2. **Decision Tree Regressor**  
   - Base model for interpretability  
   - Pruned version built using `max_depth` and `min_samples_split`  

3. **GridSearchCV-Optimized Decision Tree**  
   - Performed hyperparameter tuning to maximize test R²  
   - Best model saved and used in production predictions  

4. **Random Forest Regressor**  
   - High-performing ensemble method  
   - Useful for reducing overfitting of individual trees  

5. **Stochastic Gradient Descent (SGD) Regressor**  
   - Applied with `invscaling` learning rate  
   - Tuned for fast linear approximation  

6. **Support Vector Regressor (SVR)**  
   - Used with RBF kernel  
   - Strong at capturing nonlinear patterns in small-to-mid feature spaces  

7. **Voting Regressor (Ensemble Model)**  
   - Combined KNN, Decision Tree, and Random Forest  
   - Also evaluated a second ensemble: Optimized Tree + Random Forest  

### Evaluation Metrics

- **Train/Test R² Scores**  
- **RMSE (Root Mean Squared Error)**  
- **Variance Gap** between training and testing performance  
- **Silhouette Score** used for KMeans clustering performance  

---

## Project Structure

- `meta-data.txt`: Logs of each transformation step, timestamped  
- `predictions.xlsx`: Original + what-if simulated prediction outputs  
- `.pkl` files:  
  - `scaler.pkl`: Scaler object for numeric preprocessing  
  - `pca.pkl`: PCA object used to reduce dimensionality  
  - `*.pkl`: Trained models (KNN, Decision Tree, Optimized Tree, RF, SVR, SGD, Voting Regressors)  
- `sample_implementation.txt`: Used to load test data for what-if analysis  

---

## Final Output and Usage

The final dataset is cleaned, encoded, and PCA-transformed—ready for direct application in:

- Targeted marketing and outreach  
- Campaign planning by demographic or health behavior segment  
- Simulation of "what-if" interventions on key behavioral attributes  

For replication, load the scalers, PCA, and models using `pickle` or `joblib`, and follow the preprocessing pipeline as applied on the training data.

---
