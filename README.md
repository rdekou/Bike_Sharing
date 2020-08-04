# Bike_Sharing


This repository contains IPython Notebook with sample code, implementing Machine Learning algorithm for the Bike Demand Forecasting
given the Bike Sharing Data set at https://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset



 
### Task
Given the Bike Sharing Data set at https://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset,
make an explorative data anlysis and build a prediction model for the hourly used count.

### Data (brief description)
The data set (hour.csv) contains a wide range of features such as the season, year, weathersit, humidity, etc. all associated with the count of total rental bikes including both casual and registered users.

### Modelling approach 
- Identify columns that are potentially useful features based on data visualisation and exploration
- Create new feature colums if necessary to improve alignement between the features and the target (feature engineering)
- Select the appropriate Machine Learning algorithm for the Bike Demand Forecasting  (Regression Algorithms)
- Split the data and use a portion of it to train the selected algorithm based on the selected features columns
- Examine the trained model to identify the features that appear to have the most effect on the predictive outcome
- Score the model using the data held back to compare the predicted values with known actual values
- Repeat the process, pruning features that don't appear  to be predictively important, engineering new features and selecting alternative algorithms to create alternative models
- Evaluate all the models created by comparing with one another and examine the error statistics based on predicted and known values


Installation (for manual usage)
============

1. Clone this repository.

    git clone https://github.com/rdekou/Bike_Sharing.git


2. Setup a conda virtual environment and activate it. If you do not have conda, use an anaconda installation.

# First check if an enviroment bike-share-py37 already exists
 
    conda info --envs                              

# Remove if it exists
 
    conda remove --name bike-share-py37 --all      

# Create enviroment if it's not yet created. Otherwise, skip this step.
# This step is creating the enviroment with the necessary requirements listed in the environment-py37.yaml file
 
    conda env create -f environment-py37.yaml      

# Activate enviroment
 
    source activate bike-share-py37

# installing extra packages in the environment

    pip install -r requirements.txt             

# Note: the name bike-share-py37  is defined in the first line of the environment-py37.yml file