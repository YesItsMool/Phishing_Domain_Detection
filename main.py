from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.middleware.cors import CORSMiddleware
from joblib import load
import numpy as np
from pydantic import BaseModel, ValidationError
from typing import List
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Load the model
model = load('model.joblib')

# Initialize the FastAPI app
app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Features(BaseModel):
    asn_ip: float
    time_domain_activation: float
    length_url: float
    qty_dollar_directory: float
    qty_dollar_file: float
    qty_underline_file: float
    qty_equal_file: float
    qty_and_file: float
    qty_questionmark_directory: float
    qty_tilde_file: float
    qty_asterisk_file: float
    qty_equal_directory: float
    qty_plus_file: float
    qty_comma_file: float
    qty_exclamation_directory: float
    qty_slash_file: float
    qty_space_file: float
    qty_and_directory: float
    qty_at_directory: float
    qty_hashtag_directory: float
    qty_asterisk_directory: float
    qty_questionmark_file: float
    qty_hashtag_file: float
    qty_exclamation_file: float
    qty_at_file: float
    qty_comma_directory: float
    qty_percent_file: float
    qty_hyphen_file: float
    qty_tilde_directory: float
    qty_underline_directory: float
    qty_space_directory: float
    qty_percent_directory: float
    qty_plus_directory: float
    qty_hyphen_directory: float
    file_length: float
    qty_dot_file: float
    qty_dot_directory: float
    qty_slash_url: float
    qty_slash_directory: float
    directory_length: float


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict")
def predict(features: Features):
    # Convert the features to a dictionary
    features_dict = features.dict()

    # Check if all required features are present
    required_features = ['asn_ip', 'time_domain_activation', 'length_url', 'qty_dollar_directory', 'qty_dollar_file', 'qty_underline_file', 'qty_equal_file', 'qty_and_file', 'qty_questionmark_directory', 'qty_tilde_file', 'qty_asterisk_file', 'qty_equal_directory', 'qty_plus_file', 'qty_comma_file', 'qty_exclamation_directory', 'qty_slash_file', 'qty_space_file', 'qty_and_directory', 'qty_at_directory', 'qty_hashtag_directory', 'qty_asterisk_directory', 'qty_questionmark_file', 'qty_hashtag_file', 'qty_exclamation_file', 'qty_at_file', 'qty_comma_directory', 'qty_percent_file', 'qty_hyphen_file', 'qty_tilde_directory', 'qty_underline_directory', 'qty_space_directory', 'qty_percent_directory', 'qty_plus_directory', 'qty_hyphen_directory', 'file_length', 'qty_dot_file', 'qty_dot_directory', 'qty_slash_url', 'qty_slash_directory', 'directory_length']
    for feature in required_features:
        if feature not in features_dict:
            raise HTTPException(status_code=400, detail=f"Feature '{feature}' missing from request")

    # Convert the features to a numpy array
    features = np.array(list(features_dict.values()))
    
    # Make a prediction
    try:
        prediction = model.predict([features])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred during prediction: {str(e)}")
    
    # Convert the prediction to a native Python int
    prediction = int(prediction[0])
    
    # Return the prediction
    return templates.TemplateResponse("index.html", {"request": request, "prediction": prediction})