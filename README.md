f1-capstone-project
# Formula 1 Tire Degradation Modeling & Race Strategy Optimization
Final Report by Jeff Goode
## Executive Summary
The goal of the project was to answer the question: **“As an F1 Team Principal, should we pit now or stay out?”.**   

As was evidenced in the 2025 Qatar Grand Prix, pitting at the wrong time can be the difference between winning and losing a race.   

Given the narrow margin between **First** and **Second** place for the 2025 season (only 2 points separated the top 2 drivers), winning or losing a single race can be the difference 
in winning or losing the season.   

The challenge for F1 teams is to formulate a pit strategy (use of tire compounds and stint lengths) that adheres to 
F1 rules and is adaptive to race day conditions (yellow flag conditions).

This project provides (outputs) optimal pre-race and race-day pit strategies, allowing the race engineer to answer the "pit now or stay out?" question on a lap by lap basis.

## Model Outcomes

Supervised regression models were built that predict F1 circuit specific race car lap times based 
on a fuel-load model (linear regression) and tire degradation model (2nd degree polynomial) which form the basis of a race simulator.   
A pit strategy optimizer uses the race simulator to evaluate and recommends the top three pre-race and race-day pit strategies. 

## Data Acquisition

The models used publicly available Formula 1 timing and telemetry data from [Formula1.com](https://formula1.com)
and [FastF1 API](https://theoehrly.github.io/Fast-F1/)
.  These sources provided access to historical races by year, venue and driver.   
The FastF1 API is well documented as is the de facto source for historical F1 timing data. 

The FastF1 API data source had all the necessary timing data to enable development of the lap time models.  
Thirty-one columns of information are available per lap.  The project models used the columns indicated in green below in Table 1-1. 

![Model Performance](images/fastf1_data_example.png)

**Table 1.1 - Per Lap Timing Data**

## Data Preprocessing/Preperation

As indicated by Table 1.1, all available timing data needed for model development was available via the FastF1 API – 
there were no missing values and inconsistencies, and there was no need to build proxies for missing data.

The training data consisted of three Qatar races (2021, 2023, 2024) for the top 10 finishers with Max Verstappen’s lap information held out.   The test set was Max Verstappen’s lap information for Qatar 2025.  

Filtering out outlier data due to slow laps (pitting, yellow conditions, etc.) is essential - for Qatar the filter was set at 95 seconds.   

![Model Performance](images/filtered_lap_times.png)

**Figure 1-1 Test Data Post Slow Lap Filtering**
## Rationale

Correctly answering the question **"Should we pit now, or stay out?"** is often 
the difference between winning and losing in Formula 1.  

After a race incident involving two cars on lap 7 of the 2025 Qatar Grand Prix, Red Bull properly chose to pit 
and ultimately won the race, while McLaren chose to stay out and lost position and the race.

A quantitative model that predicts lap‑time evolution and simulates race outcomes provides:

* A reproducible, data‑driven alternative to intuition‑based strategy
* A way to evaluate “what‑if” scenarios
* A foundation for more advanced modeling in Module 24 (global vs single-driver modeling)

This project demonstrates how machine learning can support strategic decision‑making 
in a high‑performance environment.

## Research Question
**How can we model tire degradation and stint performance to predict total race time and identify 
the optimal pre-race and in-race pit‑stop strategy for the 2025 Qatar Grand Prix?**

## Data Sources
The dataset consists of lap‑by‑lap timing and stint information for Max Verstappen during the 2025 Qatar Grand Prix.
Variables include:
* Lap time
* Tire compound
* Stint number
* Lap‑in‑stint
* Fuel‑corrected lap time (engineered feature)
* Track evolution indicators (engineered feature)

The dataset was cleaned to remove outliers (pit laps, safety‑car laps, anomalous slow laps) and 
structured for modeling.

## Methodology
The analysis follows a structured workflow:

**Exploratory Data Analysis (EDA)**
* Distribution analysis of lap times and stint lengths
* Compound‑level performance comparison
* Visualization of degradation curves
* Outlier detection and removal
* Correlation analysis
* Feature engineering:
  * Fuel‑corrected lap time
  * Compound encoding
  * Stint progression features

**Baseline Machine Learning Model**

Several algorithms were tested:
* Linear Regression
* K‑Nearest Neighbors
* Support Vector Machine
* Decision Tree 

The **Decision Tree Regressor** was selected as the **baseline model** due to:
* Lowest RMSE among the tested algorithms
* Strong performance on nonlinear degradation patterns
* Interpretability

**Note:**  
This baseline model is separate from the **hand‑tuned BASE model** used in the strategy engine.  
The strategy engine ultimately uses the **SVM (RBF) model** for simulation because it produces smoother, 
more realistic degradation curves.

**Strategy Simulation Engine**
Using the SVM (RBF) model, the project simulates:
* Full race time under different pit‑stop strategies
* Compound sequences (e.g., S‑M‑H, M‑H‑H, S‑S‑M‑H)
* Stint length variations
* Degradation‑driven lap‑time evolution

This enables direct comparison of 2‑stop vs. 3‑stop strategies.

## Results
**Key EDA Finding (Qatar specific but extensible to other races)**
* Medium tires offer balanced performance, with moderate degradation
* Hard tires degrade slowest, providing the most stable long‑run pace
* Fuel‑corrected lap times reveal a clear nonlinear degradation curve across both compounds

**Model Performance**

Note the Decision Tree Regressor is the baseline model.


![Model Performance](images/model_performance.png)

**Strategy Engine Findings**
* Simulated outcomes were tuned to match historical data
* The SVM degradation model reproduces the 2025 Qatar stint behavior
* Strategy simulations confirm that pitting on lap 7 yields a faster race time than staying out

## Next Steps
* Expand the project to evaluate global modeling across multiple drivers
* Provide a more thorough analysis of model performance with tuning and cross-validation
* Add Evaluation and Deployment Sections
* Clean up project folder and remove extraneous files

## Outline of project

[Capstone Notebook](notebooks/f1.ipynb)


