# Junior Seminar (CMPSC 580) Project Proposal

## Semester: Spring 2024

This document is to contain your project proposal. __As you complete each of the below sections in this document, please be sure to remove all preamble text so that it does not appear in your work.__

## GitHub Handle: gyamfi01

## Name: Jason Gyamfi

## Major: CS

## Project Title: WE DONE WITH THE NINETY'S

## Introduction

The proposed study uses data science approaches to compare and examine scoring difficulties in basketball over different eras. This study aims to shed light on whether it was harder for players to score points during some eras than during others by examining historical basketball data and using statistical and machine learning approaches. The goal of this research is to better understand how basketball gameplay dynamics have changed over time and how these changes may affect player effectiveness and strategy.

The collection of extensive historical basketball statistics, including player performance measures, team statistics, and game outcomes, from various eras is one of the project's main components. To ensure precision and consistency for further analysis, these data will be cleansed and preprocessed. Combining machine learning algorithms to find patterns and trends in scoring difficulties over time with the computation of scoring data for various eras, including points per game, shooting percentages, and offensive efficiency, will compose the analysis. In order to show scoring trends and make historical comparisons easier, visualizations like graphs and charts will be made.

Fundamental concerns about basketball will be explored by the study, such as whether scoring difficulty significantly changed between the game's early (the 1950s–1990s) and modern (the 2000s–present) periods. Additionally, variables including rule modifications, player skill levels, and defensive tactics that affect scoring difficulties will be examined. The theories driving this research suggest that while player training improvements and strategic breakthroughs have impacted scoring patterns across time, earlier periods' increased scoring difficulty was caused by variations in gameplay styles and defensive tactics.

The goal of this research is to increase appreciation among basketball fans while also advancing our understanding of the historical background and gameplay mechanics of the sport. Basketball fans can develop a deep understanding of the sport's evolution and the efforts that have created its current form by witnessing the difficulties and adaptations players have undergone over the years. The groundwork for a thorough examination of the data analysis, findings, and implications in later sections is laid in this Introduction section.

## Literature Review

TODO (10 source minimum, with 5 of those being published peer-reviewed articles): Conduct literature review by describing relevant work related to the project and hence providing an overview of the state of the art in the area of the project. This section serves to contextualize the study within the existing body of literature, presenting a thorough review of relevant prior research and scholarly contributions. In clear and meaningful language, this section aims to demonstrate the problems, gaps, controversies, or unanswered questions that are associated with the current understanding of the topic. In addition, this section serves to highlight the current study's unique contribution to the field. By summarizing and critiquing existing works, this section provides a foundation for readers to appreciate the novelty and significance of the study in relation to the broader academic discourse. The "Literature Review" section further (in detail) contributes to the `why is the project important?` question.

## Prototype

TODO: Discuss the methods of the project to be able to answer the `how` question (`how was this project completed?`). For this section, you must describe  the methodology behind your implemented prototype. The methods section in an academic research outlines the specific procedures, techniques, and methodologies employed to conduct the study, offering a transparent and replicable framework for the research. It details the resourcs behind the work, in terms of, for example, the design of the algorithm and the experiment(s), data collection methods, applied software libraries, required tools, the types of statistical analyses and models which are applied to ensure the rigor and validity of the study. This section provides clarity for other researchers to understand and potentially replicate the study, contributing to the overall reliability and credibility of the research findings.

This study's main goal is to examine historical basketball data to identify variations in scoring challenges throughout various basketball eras, with a focus on comprehending potential effects on player efficacy and strategy.

Data Collection:

* Sources: Data was sourced from several historical databases and archives that compile basketball statistics, including player performance measures, team statistics, and game outcomes from various eras.
* Selection Criteria: Data selection focused on comprehensive coverage across multiple decades, ensuring representation from early (1950s–1990s) and modern (2000s–present) periods of basketball.
* Retrieval Method: The data was accessed using APIs where available, such as the nba_api for recent decades, and digital archives for older statistical records. Manual data entry was employed for archival data not available in digital format.

Data Processing

* Cleaning: Initial data cleaning involved removing inconsistencies and errors, such as duplicate entries and mislabeled statistics, using Python’s pandas library.
* Normalization: To compare across eras effectively, scoring metrics like points per game were normalized against era averages to account for different paces of play and scoring environments.

## Preliminary Results and Outcomes

TODO: Discuss the outcomes of your project in this section. Depending on the project type, the presented results and outcomes will vary. In some projects, you will be asked to present a theoretical analysis, and in others your experimental study and its results. In this section, you are also to demonstrate an enhanced version of your artifact by showing its capabilities and applications, in light of the evaluation metrics for assessing the artifact

The study developed a sophisticated grasp of how basketball dynamics have changed and impacted player performance and game strategy by effectively utilizing historical basketball data to examine scoring challenges throughout various eras. The results have a substantial impact on the growth of basketball as a game and on scholarly viewpoints on sports analytics.

Experimental Study and Results:

Statistical Analysis Outcomes:

Era Comparison: The analysis revealed statistically significant differences in scoring averages and efficiencies between the early and modern eras of basketball. Players from the modern era were found to have higher points per game (PPG) but also faced more dynamic and complex defenses.

Impact of Rule Changes: Changes in basketball rules, particularly those relating to the shot clock and three-point line, were found to correlate significantly with increases in scoring rates, supporting the hypothesis that rule changes have facilitated higher scoring.

## Conclusions and Future Work

TODO: Summarize your work and outline future steps needed to complete to take the project to the next stage (for example, if you were to continue with this project in 600/610). You must also address ethical implications of your project, especially as pertains to the public release or use of your software or methods.

What I Plan on Doing: 

* Predictive Modeling: Apply machine learning methods to forecast players' future performance by analyzing past patterns. This can include the use of categorization models to group players into various performance categories according to their numbers, or regression models to predict scoring based on a player's career trajectory.

* Feature Engineering: Create complex features that take into account not only fundamental statistics like points per game or assists, but also more nuanced measures like player efficiency or win shares, which are modified for era-specific characteristics.

* Use time series analysis to track patterns over time and predict future changes in the sport.

* Investigate advanced statistical models for effectively dealing with data anomalies and volatility, ensuring that historical comparisons are as fair and precise as feasible.

Implementing Machine Learning: 

* Development: Build a comprehensive machine learning pipeline that includes data preprocessing, feature extraction, model training, evaluation, and deployment.

* Model Training: Use historical data to train models, adjusting parameters to optimize for accuracy and generalizability.
Model Evaluation: Rigorously test models using appropriate cross-validation techniques to ensure they perform well on unseen data.

Deep Learning for Advanced Pattern Recognition:

* Explore deep learning models to capture complex nonlinear relationships in the data that simpler models might miss. This could include using neural networks to predict player performance based on a wide range of input features.

* Use convolutional neural networks (CNNs) for image-based analysis, such as player movements or game situations, if video or image data becomes available.

Natural Language Processing (NLP):

* Implement NLP to analyze commentary and reports for qualitative insights into player performance and public perception over different eras. This can provide a richer, more nuanced understanding of how players are viewed by fans and analysts across time.

Expanding Data Sources

Integrating More Diverse Data:

* Incorporate additional data sources such as social media sentiment analysis to understand public perception of players and teams across different eras.

* Explore other statistical databases for more granular data, such as minute-by-minute player tracking information.

Real-Time Data Analysis:

* Develop capabilities to analyze data in real-time during games, providing live insights and updates. This could enhance fan experiences and provide immediate feedback for coaching staff.

* Enhancements to the Streamlit Dashboard

Interactive Features:

* Implement more interactive elements, such as sliders to adjust parameters of the machine learning models, allowing users to see how changes affect predictions.
* Provide users with the ability to upload their data sets for custom analysis.

Visualization Upgrades:

Incorporate more advanced visualizations, such as heat maps or dynamic graphs, to show changes over time more vividly.
Use Plotly or D3.js for more sophisticated, interactive charting capabilities.
Addressing Ethical Considerations

Ensuring Model Transparency:

* Provide detailed explanations of how the models make their predictions, known as model interpretability, which can help in validating the outputs and ensuring they are free from biases.

* Regular audits of the models to check for any discriminatory patterns or outcomes.

Impact Assessment:

* Evaluate the application's possible effects on different stakeholders, such as players, teams, fans, and bettors, prior to its public release.
  
* Provide rules for the application's ethical usage, making sure it supports the sports community and complies with fair use requirements.

* By continuing to improve the project with these developments, it will not only provide deeper insights into basketball but also push the boundaries of sports analytics, making it more interactive, informative, and accessible to a wider audience.

## References

TODO: Add references in the [ACM style](https://www.acm.org/publications/authors/reference-formatting). All references must be cited in the proposal.
