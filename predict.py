# ============================================
# SECTION 1: IMPORTS
# ============================================
import pandas as pd
import joblib
import os

# ============================================
# SECTION 2: LOAD SAVED OBJECTS
# ============================================

# Get the current file's directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Folder where your joblib files live (make sure folder is named exactly 'models')
MODEL_PATH = os.path.join(BASE_DIR, "Model")

# Load joblib files correctly
model = joblib.load(os.path.join(MODEL_PATH, "model.joblib"))
scaler = joblib.load(os.path.join(MODEL_PATH, "scaler.joblib"))
target_encoder = joblib.load(os.path.join(MODEL_PATH, "target_encoder.joblib"))
numeric_imputer = joblib.load(os.path.join(MODEL_PATH, "numeric_imputer.joblib"))
knn_imputer = joblib.load(os.path.join(MODEL_PATH, "knn_imputer.joblib"))
feature_order = joblib.load(os.path.join(MODEL_PATH, "feature_order.joblib"))
metrics = joblib.load(os.path.join(MODEL_PATH, "metrics.joblib"))


# ============================================
# SECTION 3: DEFINE COLUMN NAMES
# ============================================
NUMERIC_COLS = ['Number of bedrooms', 'Number of bathrooms', 'Number of toilets']
CATEGORICAL_COLS = ['type', 'Region']
BINARY_COLS_KNN = ['Elevator', 'Garden']
BINARY_COLS_ZERO = ['Garage', 'Swimming pool']


# ============================================
# SECTION 4: MAIN PREDICTION FUNCTION
# ============================================
def predict_price(input_data: dict):
    """
    Takes a dictionary of property features
    Returns: predicted price, metrics dictionary
    """
    # Convert to DataFrame
    df = pd.DataFrame([input_data])
    
    # Apply preprocessing (same order as training)
    df[CATEGORICAL_COLS] = target_encoder.transform(df[CATEGORICAL_COLS])
    df[NUMERIC_COLS] = numeric_imputer.transform(df[NUMERIC_COLS])
    df[NUMERIC_COLS] = scaler.transform(df[NUMERIC_COLS])
    df[BINARY_COLS_KNN] = knn_imputer.transform(df[BINARY_COLS_KNN])
    df[BINARY_COLS_ZERO] = df[BINARY_COLS_ZERO].fillna(0)
    
    # Reorder columns to match training
    df = df[feature_order]
    
    # Predict
    price = model.predict(df)[0]
    
    # Return both the prediction and metrics
    return price, metrics


# ============================================
# SECTION 5: LOCAL TESTING
# ============================================
if __name__ == "__main__":
    test_property = {
        'Number of bedrooms': 3,
        'Number of bathrooms': 2,
        'Number of toilets': 1,
        'type': 'apartment',
        'Region': 'Brussels',
        'Elevator': 1,
        'Garden': 0,
        'Garage': 1,
        'Swimming pool': 0,
        'postal_code': 1000
    }

    price, metrics = predict_price(test_property)

    # # Display result
    # print("=" * 50)
    # print("PREDICTION RESULT")
    # print("=" * 50)
    # print(f"\n💰 Predicted Price: €{price:,.2f}")
    # print(f"\n📊 Model Performance:")
    # print(f"   R²:   {metrics['val_r2']:.4f}")
    # print(f"   MAE:  ±€{metrics['val_mae']:,.0f}")
    # print(f"   RMSE: ±€{metrics['val_rmse']:,.0f}")
    # print(f"\n📍 Price Range (using MAE):")
    # print(f"   Low:  €{price - metrics['val_mae']:,.2f}")
    # print(f"   High: €{price + metrics['val_mae']:,.2f}")
    # print("=" * 50)

