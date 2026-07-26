import joblib


MODEL_PATH = "src/models/cbc_model.pkl"
ENCODER_PATH = "src/models/label_encoder.pkl"
GENDER_ENCODER_PATH = "src/models/gender_encoder.pkl"


model = joblib.load(MODEL_PATH)

label_encoder = joblib.load(ENCODER_PATH)

gender_encoder = joblib.load(GENDER_ENCODER_PATH)