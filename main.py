from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from routes import auth
from fastapi.middleware.cors import CORSMiddleware
from joblib import load
import numpy as np
import pandas as pd
import logging
from fastapi import FastAPI, HTTPException
from feature_extraction import extract_features


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(auth.router)

# Load the model
model = load('model.joblib')

#logging
logger = logging.getLogger("uvicorn")
logger.setLevel(logging.DEBUG) 
class RegistrationForm(BaseModel):
    username: str
    email: str
    password: str
class URL(BaseModel):
    url: str


class LoginForm(BaseModel):
    username: str
    password: str

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


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/register", response_class=HTMLResponse)
def register(request: Request, form: RegistrationForm):
    # Handle registration form submission here
    # Retrieve form data from request
    # Register user using the UserManager
    return templates.TemplateResponse("registration_success.html", {"request": request})


@app.post("/login", response_class=HTMLResponse)
def login(request: Request, form: LoginForm):
    # Handle login form submission here
    # Retrieve form data from request
    # Check credentials using the UserManager
    return templates.TemplateResponse("login_success.html", {"request": request})


from feature_extraction import extract_features

@app.post("/predict")
async def predict(url: URL):
    extracted_features = await extract_features(url.url)

    # Convert the features to a numpy array
    features_array = np.array(list(extracted_features.values())).astype(float)

    # Create a DataFrame with appropriate column names
    features_df = pd.DataFrame([features_array], columns=extracted_features.keys())

    try:
        # Make a prediction
        prediction = model.predict(features_df)
        # Convert the prediction to a native Python int
        prediction = int(prediction[0])
        # Return the prediction
        return {"prediction": prediction}
    except Exception as e:
        # Log the exception
        logger.exception("An error occurred during prediction")
        # Return an error response
        raise HTTPException(status_code=500, detail=f"An error occurred during prediction: {str(e)}")

@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    logger.exception("An error occurred during request processing")
    raise HTTPException(status_code=500, detail="Internal Server Error")



# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    # Configure logging
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")