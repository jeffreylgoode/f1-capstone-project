f1-capstone-project
# Formula 1 Tire Degradation Modeling & Race Strategy Optimization
Final Report by Jeff Goode
## Executive Summary
The goal of the project was to answer the question: **“As an F1 Team Principal, should we pit now or stay out?”.**   

As was evidenced in the 2025 Qatar Formula 1 Grand Prix, pitting at the wrong time can be the difference between winning and losing a race.

McLaren's Oscar Piastri started the race in 1st place, while Red Bull's Max Verstappen started the race in 2nd.  On lap 7, a yellow flag condition occurred.  Max as well as most of the field pitted and changed tires.  Oscar stayed out and pitted on lap 24 under normal green conditions.  Max won the race earning 25 points for the win, Oscar came in second place earning 18 points.  **The decision to stay out on lap 7 cost McLaren the race.** 

The 2025 season was won by McLaren's Lando Norris with 423 points vs Max Verstappen's 421 points further reinforcing the criticality of each race and each point. 

To answer the "pit now or stay out" question requires selecting a pit strategy that will minimize lap times which in turn requires predicting lap time based on **fuel burn** and **tire degradation**.  In this project predictive models were built for both as part of a race simulator.  Additionally, a strategy optimization engine was developed to iterate all possibilities of tire compounds and tire usage.


This project provides (outputs) optimal pre-race and race-day pit strategies, allowing the race engineer to answer the "pit now or stay out?" question on a lap-by-lap basis.

![Qatar 2025 Winning Strategy](images/qatar_2025_winning_strategy.png)

**Figure 1 - Max Verstappen's Qatar 2025 Winning Strategy**

### Findings
A linear model was used to capture fuel‑burn effects, and a second‑degree polynomial (poly-2) model was selected as the most reliable approach for modeling tire degradation. Among the four candidate models evaluated, the second‑degree polynomial delivered the strongest overall performance on the 2025 Qatar test data and was therefore chosen for the strategy engine.





### Results and Conclusion

Using the top 10 drivers from prior Qatar races as the training set, and the poly-2 model for predicting tire degradation, the strategy optimizer correctly identified Max's pre-race strategy (Medium tires) and correctly identified the "pit now" decision on lap 7 (a 42-second savings using Medium tires for 25 laps, and Hard tires for 25 laps).  If McLaren had been using this toolset (race simulator and strategy optimizer engine), they would have pitted on lap 7 and likely won the 2025 Qatar Grand Prix changing the trajectory of the 2025 season.

![Qatar 2025 Winning Strategy](images/strategy_engine_results_reva.png)

**Table 1 - Tire Degradation Model and Strategy Optimizer Engine Results**

### Future Reseach and Development

**Probability of a Safety Car or Virtual Safety Car Event.**  Sometimes pit decisions should be delayed based on the probability of a SC or VSC event.  Coupling the probability of the event with tire (stint) age would yield a more realistic strategy engine.

**Treatment of Wet Weather Conditions**.  The model and strategy engine need to be modified to take into account weather and use of SOFT, WET and INTERMEDIATE tires as evidenced by the Canadian F1 2026 results shown in section 10.0 of the Jupyter notebook. 

**Scaleability**. Predicting new race outcomes requires a lot of copy and paste work.
Accordingly, the code should be refactored, wrappers developed, to enable functional calls versus running the code in line.  

### Next Steps and Recommendations
The Jupyter notebook demonstrates how the deployed code (section 6 of the Jupyter notebook) can be modified for the current Formula 1 season.  The example shown in section 10 of the notebook should be used to refactor the code to make it more production ready and easier to use for quick analysis (lap time filtering and model fit analysis).

## Rationale

Correctly answering the question **"Should we pit now, or stay out?"** is often the difference between winning and losing in Formula 1.

After a race incident involving two cars on lap 7 of the 2025 Qatar Grand Prix, Red Bull properly chose to pit and ultimately won the race, while McLaren chose to stay out and lost position and the race.

A quantitative model that predicts lap‑time evolution and simulates race outcomes provides:

* A reproducible, data‑driven alternative to intuition‑based strategy
* A way to evaluate “what‑if” scenarios
* A foundation for more advanced modeling (probability of a race incident, weather impact on tire choice, race traffic, undercut strategies)

This project demonstrates how machine learning can support strategic decision‑making in a high‑performance environment.
## Research Question
How can we model tire degradation and stint performance to predict total race time and identify the optimal pre-race and in-race pit‑stop strategy for the 2025 Qatar Grand Prix?


## Data Acquisition

The models used publicly available Formula 1 timing and telemetry data from [Formula1.com](https://formula1.com)
and [FastF1 API](https://theoehrly.github.io/Fast-F1/). These sources provided access to historical races by year, venue and driver. The FastF1 API is well documented as is the de facto source for historical F1 timing data. 

The FastF1 API data source had all the necessary timing data to enable development of the lap time models.  
Thirty-one columns of information are available per lap.  The project models used the columns indicated in green below in Table 2. 

![Model Performance](images/fastf1_data_example.png)

**Table 2 - Per Lap Timing Data**

## Project Tool Set Hierarchy and Workflow

The following diagram indicates how data comes into the project, and the relationship between the models, the race simulator and the strategy optimization engine.  The race week workflow describes the steps a race engineer would follow to prepare for an upcoming race. 

![Model Performance](images/workflow.png)

**Figure 2 - Project Tool Set Hierarchy and Workflow**

## Data Preprocessing/Preparation

As indicated by Table 2, all available timing data needed for model development was available via the FastF1 API – 
there were no missing values and inconsistencies, and there was no need to build proxies for missing data.

The training data consisted of three Qatar races (2021, 2023, 2024) for the top 10 finishers with Max Verstappen’s lap information held out.   The test set was Max Verstappen’s lap information for Qatar 2025.  

Filtering out outlier data due to slow laps (pitting, yellow conditions, etc.) is essential - for Qatar the filter was set at 95 seconds.   

![Model Performance](images/filtered_lap_times.png)

**Figure 3 Test Data Post Slow-Lap Filtering**
## Modeling

The project utilized two supervised regression models, a linear regression model for predicting fuel-load lap time reduction and
a 2nd degree polynomial for predicting tire degradation. 
## Methodology
The analysis followed a structured workflow:

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
* Polynomial Regression
* K‑Nearest Neighbors
* Support Vector Machine
* Decision Tree 

Initially (in a Module 20 Berkeley submission), the **Decision Tree** was selected as the **baseline model** due to:
* Lowest RMSE among the tested algorithms
* Strong performance on nonlinear degradation patterns
* Interpretability

For the second stage of this capstone project (Module 24 Berkeley submission) a formal training set and test set were identified.  Using that training set, and performing subsequent analysis indicated that a 2nd degree polynomial was the best model and the baseline model was changed. 


## Modeling Evaluation 
### Fuel Load Modeling
The Linear Regression model is well documented in the F1 community as the best model for modeling fuel burn or fuel-load with laps getting 
faster per lap as the car gets lighter due to a reduced fuel mass.  See Table 3 below for the results of the fuel-load modeling.   The average of the slopes was used to model fuel burn for Qatar 2025, -0.080096 sec/lap.

![Model Performance](images/fuel_modeling_performance.png)

**Table 3  - Fuel Load Model Performance**
### Tire Degradation Modeling

Before evaluating model performance on the 2025 Qatar race, a year‑to‑year pace correction was applied to account for differences in track evolution, car performance, and event‑specific conditions. This correction, expressed as an offset of −2.246 seconds, aligns the model’s baseline with the actual pace observed in 2025. After applying the offset, all models were evaluated on the held‑out Qatar 2025 race.

Slow laps (pit lane and SC/VSC periods) are removed from the plotted dataset to ensure that model comparisons reflect only true race‑pace behavior. Because these laps are excluded entirely—rather than shown as separate points—the prediction lines contain intentional gaps at laps 7–11 and 31–33. These discontinuities are expected and simply indicate where non‑representative laps were filtered out before plotting.

With the offset applied and slow laps removed, four models were evaluated for modeling tire degradation, as shown in Figure 3. Polynomial‑2, Decision Tree, KNN, and SVM (RBF) were used to predict lap times for the test data, Max Verstappen’s 2025 Qatar results (blue line).

The KNN and Decision Tree models produced jagged results that are not indicative of real tire‑degradation behavior. The SVM model produced smoother curves, but because RMSE (0.7088) and MAE (0.5709) were lower and R² (0.6257) was higher, the Poly‑2 model was chosen.

![Model Performance](images/four_models.png)

**Figure 4 Tire Degradation Models and Model Performance**

## Strategy Optimization Engine

The Strategy Optimization Engine is the core decision‑making module of the project. It transforms the stint‑level tire and fuel models into full‑race strategic predictions, enabling both pre‑race planning and real‑time Safety Car decision logic. For this project, the engine is calibrated specifically for the 2025 Qatar Grand Prix, though the architecture is designed so it can be generalized to other circuits in future work.  

**What the Engine Computes**
* Pre‑race strategy predictions — evaluates all valid tire‑compound sequences and stint lengths to identify the fastest baseline race plans
* Safety Car stay‑out logic — determines whether a driver should pit or remain on track when a Safety Car appears
* Pit‑now vs stay‑out deltas — quantifies the time difference between immediate pitting and continuing the current stint
* Full‑race simulation timing — computes total race time for each candidate strategy using the selected tire‑degradation model

The Strategy Optimization Engine brings together all prior modeling work—fuel load effects, tire degradation, stint‑time prediction, and pit‑loss modeling—into a unified race‑strategy framework. It demonstrates how data‑driven modeling can replicate real‑world F1 decision‑making and provides a foundation for future generalization across circuits and seasons.
## Outline of Project

[Link to Capstone Jupyter Notebook](notebooks/f1.ipynb)

* For analysis of the 2025 Qatar F1 Grand Prix, see Section 6.0
* For the Final Summary, see Section 7.0
* For analysis of the 2026 Canadian F1 Grand Prix, see Section 10.0




## Contact and Further Information

Jeff Goode

Email: jeffreylgoode@gmail.com

[LinkedIn](https://www.linkedin.com/in/jeffreylgoode/)
