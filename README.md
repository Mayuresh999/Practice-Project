# Chicken Disease Project
A Webapp to classify "Healthy" vs "Coccidiosis" infected chicken fecal images.

## Project flow: 
1. Data Ingestion (data downloaded and unzipped)
2. Prepare Base Model (defining model and required parameters and hyperparameters)
3. Define Callbacks (defining callbacks used during training)
4. Train Model (train the model on dataset)
5. Evaluate Model (evaluate the model on defined evaluation metrics)
6. Prediction (predict image on trained model)

## Tech stack used:
1. GitHub
2. DVC
3. Docker
4. Tensorboard

## Github Repository
### Clone Repository
```git clone https://github.com/Mayuresh999/Practice-Project.git```
### Install Requirements
```pip install -r requirements.txt```
### Run Project
```python app.py```
### OR...
## Pull Docker Image
```docker pull mayuresh999/chicken-disease-project:latest```
## Run Image
```docker run -it -p 8080:8080 chicken:latest```

It will start the project in localhost:8080