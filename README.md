# Bestseller Book Prediction Model

## Project Overview
This repository contains the implementation of a logistic regression model to predict the bestseller status of books. The model is trained on a dataset of 868 books with data collected via web scraping from Public Random House Publishing House and Amazon.

## Features
- Ratings
- Prices
- Book length
- Genre
- Amazon bestseller rank
- Author information

The output variable is the Amazon bestseller rank, with the other features serving as input variables.

## Data Collection
Data was collected through web scraping, initially including features like targeted audience and genre derived from book synopses. However, due to accuracy concerns, these features were refined to improve the model's predictive performance.

## Model Development
A logistic regression machine learning model was chosen for its effectiveness in classification problems. The dataset was split into an 80-20 train-test ratio. The final model achieved an accuracy of 81%.

## Modifications
- Removal of the 'targeted audience' and 'genre' features post-initial trials for better accuracy.
- Exclusion of 'total number of reviews' led to a rise in model accuracy.

## Repository Contents

├── data
│ ├── scraped_data.csv # Dataset containing the features of books.
├── notebooks
│ ├── data_preprocessing.ipynb # Jupyter notebook for data cleaning and preprocessing.
│ ├── model_training.ipynb # Jupyter notebook for training the logistic regression model.
├── src
│ ├── scraping
│ │ ├── scrape.py # Script used for web scraping.
│ ├── analysis
│ │ ├── data_analysis.py # Script for initial data analysis.
│ ├── model
│ │ ├── logistic_model.py # Script containing the logistic regression model.
├── README.md
└── requirements.txt # Required libraries and dependencies to run the project.

## Setup
To set up the project environment:
1. Clone the repository.
2. Install the required dependencies:
```bash
pip install -r requirements.txt



