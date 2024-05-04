# Junior Seminar (CMPSC 580) Project Proposal

## Semester: Spring 2024

This document is to contain your project proposal. __As you complete each of the below sections in this document, please be sure to remove all preamble text so that it does not appear in your work.__

## GitHub Handle: gyamfi01

## Name: Jason Gyamfi

## Major: CS

## Project Title: WE DONE WITH THE NINETY'S

Introduction
The proposed study leverages data science methodologies to delve into the question of scoring difficulty across distinct eras in basketball. By employing statistical analysis and machine learning techniques on historical basketball data, this research aims to determine if scoring points was demonstrably harder during specific periods. The ultimate goal is to achieve a deeper understanding of how the dynamics of basketball gameplay have evolved over time, and how these changes have impacted both player effectiveness and strategic approaches on the court.

A critical component of this project involves the collection of comprehensive historical basketball statistics. This data will encompass player performance metrics, team statistics, and game outcomes, all meticulously gathered from various eras. To ensure accuracy and consistency for subsequent analysis, the data will undergo a rigorous cleansing and preprocessing phase. The core analysis will involve a two-pronged approach. First, machine learning algorithms will be utilized to identify patterns and trends in scoring difficulty across different eras. Second, this will be complemented by the computation of scoring data for various eras, including points per game (PPG), shooting percentages, and offensive efficiency. To effectively showcase these scoring trends and facilitate comparisons between eras, compelling visualizations such as graphs and charts will be created.

The study delves into fundamental questions regarding basketball. Did scoring difficulty undergo significant changes between the sport's early period (1950s-1990s) and the modern era (2000s-present)?  Additionally, the research will examine variables that potentially influence scoring difficulty, including rule modifications, player skill levels, and defensive tactics.  The underlying theory driving this research posits that while advancements in player training and strategic breakthroughs have undoubtedly impacted scoring patterns throughout history, the increased scoring difficulty observed in earlier eras can be primarily attributed to variations in gameplay styles and defensive tactics employed.

By investigating these factors, this research aspires to not only enrich the appreciation of basketball fans but also contribute valuable insights into the sport's historical background and the evolution of its gameplay mechanics. Witnessing the challenges and adaptations players have faced throughout history will enable basketball fans to develop a deeper understanding of the sport's remarkable evolution and the efforts that have shaped its current form. This introductory section lays the groundwork for a thorough examination of data analysis, findings, and their broader implications, which will be explored in subsequent sections.

## Literature Review

This lit review examines how NBA scoring has changed over time using thorough scholarly research and insightful articles from the sports analytics and basketball communities. It studies many aspects of basketball evolution, such as regulation changes, player performance, and statistical analysis, in order to interpret these patterns' broader significance for the sport.

Peer-Reviewed Articles

* Rocha da Silva, João Vítor; Rodrigues, Paulo Canas (2021). "The Three Eras of the NBA Regular Seasons: Historical Trend and Success Factors," Journal of Sports Analytics. This research applies advanced statistical methods, such as K-means clustering and LASSO regression, to delineate distinct eras of NBA basketball, offering insights into the key factors driving success across different periods.
DOI: 10.3233/JSA-200525

* "Trends in NBA and Euroleague Basketball (2000-2017)." This study conducts a comparative analysis using box-score statistics to explore differences and trends in the game dynamics and team success metrics over nearly two decades, published in PLOS ONE.
* "Exploring Game Performance in the NBA Using Player Tracking Data." This article investigates how all-star and non-all-star players perform differently, utilizing advanced player tracking data to analyze performance metrics and identify discriminative variables between player groups in PLOS ONE.
  
* "Game Statistics That Discriminate Winning and Losing in the NBA." Focuses on identifying game-related statistical parameters that distinguish winning and losing outcomes in NBA games, offering insights into critical performance indicators during competitive periods in PLOS ONE.
  
* "Strategically Driven Rule Changes in NBA: Causes and Consequences." Examines the effects of NBA rule changes on game statistics, particularly how these changes have influenced the speed and efficiency of the game, thus affecting scoring dynamics and gameplay strategies in The Sport Journal.
  
* "What are the changes in basketball shooting pattern and accuracy in the NBA in the past decade?" Discusses how changes in game rules and playing styles have affected the pace and shooting patterns in NBA games, highlighting the increase in three-point shooting and its impact on scoring trends in Frontiers.

Non-Peer-Reviewed Articles

* Fromal, Adam. "Ranking Each Decade of NBA Basketball, from the 1960s to Today." Provides a narrative analysis of NBA basketball over the decades, offering insights into how the game and its players have evolved over time. Available on sports analysis websites like Bleacher Report.
  
* Wang, Daniel. "How Can We Accurately Compare NBA Players Across Different Eras?" Tackles the challenge of comparing player performance across different periods, discussing various statistical techniques and considerations that should be taken into account. Found on basketball analytics blogs or sports data science platforms.
  
* "How the Average NBA Player has Evolved Throughout 75 Years of League History." Explores the physical and performance changes in NBA players over the league's history, supported by data on player size, role, and contributions. Available on comprehensive sports news sites like ESPN.

* Reynolds, Tim. "The NBA’s Scoring Boom is Still Going Strong, and Some Wonder if That’s a Good Thing." This article discusses the contemporary scoring trends in the NBA, particularly the increase in overall game scoring, and debates whether these changes are beneficial for the sport. This piece provides a critical perspective on modern scoring dynamics, questioning the sustainability and impact of high-scoring games on the sport’s integrity and viewer engagement.

* This literature review's use of both scholarly and popular sources provides a complete study of how NBA scoring dynamics have changed throughout time. It offers a comprehensive knowledge of how basketball has evolved, guided by rigorous data-driven research and complemented by larger cultural and historical perspectives. This literature study not only covers the academic discourse surrounding NBA scoring patterns, but also engages in broader debates and conversations within the basketball community, emphasizing the sport's continual growth and its impact on players, teams, and fans alike.

## Prototype

This study's main goal is to examine historical basketball data to identify variations in scoring challenges throughout various basketball eras, with a focus on comprehending potential effects on player efficacy and strategy. By delving into the nuances of scoring difficulties across different time periods, we aim to unravel the intricate relationship between gameplay dynamics, rule changes, and player performance. Through rigorous analysis and interpretation of the data, we seek to gain deeper insights into how scoring challenges have evolved over time and how these changes have shaped the strategies and effectiveness of players on the court.

The exploration of historical basketball data offers a unique opportunity to uncover patterns and trends that may not be immediately apparent. By leveraging advanced statistical and machine learning techniques, we can extract meaningful information from vast datasets spanning decades of basketball history. This comprehensive analysis will allow us to compare scoring difficulties across eras, identify key factors influencing scoring trends, and elucidate the impact of external variables such as rule modifications and defensive tactics.

Furthermore, this study goes beyond mere data analysis by exploring the implications of scoring challenges on player performance and strategic decision-making. Understanding how scoring difficulties have evolved can provide valuable insights for coaches, players, and analysts in optimizing game strategies, player development programs, and tactical approaches. By bridging the gap between historical data and contemporary basketball dynamics, we aim to contribute to the ongoing dialogue surrounding basketball analytics and enhance our understanding of the sport's evolution.

In conclusion, this study is a determined attempt to understand the fundamental dynamics of basketball scoring difficulties from the early decades to the present. Our goal is to provide stakeholders with actionable insights, shed light on the factors influencing scoring challenges, and push basketball analytics as an essential part of sports research and strategy development by utilizing state-of-the-art analytical tools and methodologies.

Data Collection:

* Sources: Data was sourced from several historical databases and archives that compile basketball statistics, including player performance measures, team statistics, and game outcomes from various eras.
* Selection Criteria: Data selection focused on comprehensive coverage across multiple decades, ensuring representation from early (1950s–1990s) and modern (2000s–present) periods of basketball.
* Retrieval Method: The data was accessed using APIs where available, such as the nba_api for recent decades, and digital archives for older statistical records. Manual data entry was employed for archival data not available in digital format.

Data Processing

* Cleaning: Initial data cleaning involved removing inconsistencies and errors, such as duplicate entries and mislabeled statistics, using Python’s pandas library.
* Normalization: To compare across eras effectively, scoring metrics like points per game were normalized against era averages to account for different paces of play and scoring environments.

## Preliminary Results and Outcomes

Experimental Study and Results:

* Comprehensive datasets spanning several decades of NBA play were analyzed to extract trends in scoring, player efficiency, and team strategies.

Statistical Analysis Outcomes:

* Era Comparison: The analysis revealed statistically significant differences in scoring averages and efficiencies between the early and modern eras of basketball. Players from the modern era were found to have higher points per game (PPG) but also faced more dynamic and complex defenses.

* Impact of Rule Changes: Changes in basketball rules, particularly those relating to the shot clock and three-point line, were found to correlate significantly with increases in scoring rates, supporting the hypothesis that rule changes have facilitated higher scoring.


## Conclusions and Future Work

The study established a detailed understanding of how basketball dynamics have evolved over time, with important implications for player performance and game strategies. By methodically studying historical basketball statistics, the study offers a deep dive into the scoring obstacles faced across several eras, revealing the interplay between regulation changes, player evolution, and strategic shifts. The detailed research revealed not only quantitative changes in scoring, but also improvements in quality in gameplay, providing a deeper understanding of the sport's evolution. The findings of this study are especially significant since they contribute significantly to the continuing discussion about basketball's expansion, both as a competitive sport and as an area of academic interest within sports analytics. This improved understanding helps scholars, strategists, and fans appreciate the nuances of basketball and develops a deeper engagement with its historical and analytical components.

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

Ensuring Model Transparency:

* Provide detailed explanations of how the models make their predictions, known as model interpretability, which can help in validating the outputs and ensuring they are free from biases.

* Regular audits of the models to check for any discriminatory patterns or outcomes.

Impact Assessment:

* Evaluate the application's possible effects on different stakeholders, such as players, teams, fans, and bettors, prior to its public release.

* Provide rules for the application's ethical usage, making sure it supports the sports community and complies with fair use requirements.

* By continuing to improve the project with these developments, it will not only provide deeper insights into basketball but also push the boundaries of sports analytics, making it more interactive, informative, and accessible to a wider audience.

## References

Rocha da Silva, J. V., & Rodrigues, P. C. (2021). The Three Eras of the NBA Regular Seasons: Historical Trend and Success Factors. Journal of Sports Analytics, 7(4), 263-275. https://doi.org/10.3233/JSA-200525
Radivoj Mandić. (2019). Trends in NBA and Euroleague Basketball (2000-2017). PLOS ONE.
Jaime Sampaio. (2019). Exploring Game Performance in the NBA Using Player Tracking Data. PLOS ONE.
Dimitrije Cabarkapa. (2022). Game Statistics That Discriminate Winning and Losing in the NBA. PLOS ONE.
Mahmoud M. Nourayi. Strategically Driven Rule Changes in NBA: Causes and Consequences. The Sport Journal.
Feng Wang. (2022). What are the changes in basketball shooting pattern and accuracy in the NBA in the past decade? Frontiers.
OpenAI. (2024, May 3). OpenAI Chat. Retrieved from https://chat.openai.com