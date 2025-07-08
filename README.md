Interactive Manufacturing Process Dashboard
An interactive, single-page web application designed to analyze and visualize key performance indicators from a real-world manufacturing dataset. This project translates complex operational data into an intuitive dashboard, making it easy to identify opportunities for process optimization and quality improvement.

Live Demo Link

Table of Contents
Project Overview

Key Features

Tech Stack

Data Source

Analytical Insights

How to Run Locally

Project Overview
The goal of this project was to analyze a manufacturing dataset to uncover the relationships between various process parameters and the resulting product quality. Instead of a static report, the findings are presented in a dynamic, single-page application that allows users to explore the data visually. The dashboard highlights critical insights and provides clear, data-driven recommendations for improving operational efficiency.

Key Features
At-a-Glance KPIs: The dashboard immediately presents the most critical findings, such as the negative correlation between speed/temperature and quality.

Interactive Charts: All visualizations are built with Chart.js and are fully responsive, with tooltips that provide detailed information on hover.

Visual Correlation Analysis: A horizontal bar chart quantifies the strength of key correlations, making it easy to see which factors are most influential.

Optimal Operating Zone: Interactive scatter plots visualize the relationship between machine parameters and quality, clearly highlighting the "optimal zone" for production.

Actionable Recommendations: The application concludes with a clear, prioritized list of recommendations based directly on the analytical findings.

Tech Stack
Frontend: HTML5, Tailwind CSS

Data Visualization: Chart.js, chartjs-plugin-annotation

Core Logic: Vanilla JavaScript

Data Source
This analysis was performed on the "Smart Manufacturing Process Data" dataset, publicly available on Kaggle. The dataset contains 10,000 time-stamped observations from an industrial machine, capturing key operational parameters like temperature, machine speed, vibration levels, and production quality scores.

Analytical Insights
The analysis uncovered three core insights that drive the recommendations:

Negative Correlation: Machine Speed (RPM) and Temperature (°C) were identified as having the strongest negative correlation with the final Production Quality Score.

Optimal Window: The highest quality scores are consistently achieved when machine speed is kept below 1600 RPM and temperature is below 90°C.

Actionable Factors: By focusing on controlling these two parameters, the facility can achieve significant gains in quality and efficiency.
