# 🏡 Immo Eliza Price Prediction App

A machine learning-powered web application that predicts real estate prices in Belgium.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-ML-orange?style=for-the-badge)

🔗 **Live Demo:** [immo-eliza-predict.streamlit.app](https://immo-eliza-pricepredict.streamlit.app//)

---

## 📖 Description

This web application provides instant property price estimates for the Belgian real estate market. Users can input property characteristics and receive a predicted price along with a confidence range based on the model's Mean Absolute Error (MAE).

### Key Features

- 🏠 **Instant Predictions** - Get price estimates in seconds
- 📊 **Price Range** - See low and high estimates based on model accuracy
- 📈 **Feature Analysis** - Understand what affects property prices
- 🇧🇪 **Belgium Coverage** - Brussels, Flanders, and Wallonia regions
- 📱 **Responsive Design** - Works on desktop and mobile

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Frontend | Streamlit |
| ML Model | XGBoost |
| Data Processing | Pandas, NumPy, Scikit-learn |
| Visualization | Plotly |
| Deployment | Streamlit Cloud |

---

## 📁 Project Structure

```
Immo-Eliza-Deployment/
├── Model/
│   ├── model.joblib            # Trained XGBoost model
│   ├── scaler.joblib           # StandardScaler for numeric features
│   ├── target_encoder.joblib   # TargetEncoder for categorical features
│   ├── numeric_imputer.joblib  # SimpleImputer for missing values
│   ├── knn_imputer.joblib      # KNNImputer for binary features
│   ├── feature_order.joblib    # Column order for prediction
│   └── metrics.joblib          # Model performance metrics
├── app.py                      # Streamlit application
├── predict.py                  # Prediction logic
├── requirements.txt            # Python dependencies
└── README.md
```

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/immo-eliza-deployment.git
cd immo-eliza-deployment
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

The app will open in your browser as localhost.

---

## 📋 Input Features

| Feature | Type | Description |
|---------|------|-------------|
| Number of Bedrooms | Numeric | 0-20 bedrooms |
| Number of Bathrooms | Numeric | 0-20 bathrooms |
| Number of Toilets | Numeric | 0-20 toilets |
| Property Type | Categorical | apartment, house, villa, studio, land, commercial |
| Region | Categorical | Brussels, Flanders, Wallonia |
| Postal Code | Numeric | Belgian postal codes (1000-9999) |
| Elevator | Binary | Yes/No |
| Garden | Binary | Yes/No |
| Garage | Binary | Yes/No |
| Swimming Pool | Binary | Yes/No |

---



## 🔄 Data Pipeline

```
User Input → Preprocessing → Model Prediction → Price Estimate
     │              │                │               │
     ▼              ▼                ▼               ▼
  Form Data    Target Encoding    XGBoost      €XXX,XXX
               Scaling            Predict      ± MAE
               Imputation
```


---

## 📱 App Sections

### 🏠 Prediction Tab
- Property input form
- Real-time price prediction
- Low/High estimate range
- Visual price range bar

### 📊 Analysis Tab
- Feature importance funnel chart
- Key insights about price factors
- Data-driven recommendations

### 📋 Sidebar
- Property summary panel
- Quick reference of inputs

---

## 🌐 Deployment

The app is deployed on **Streamlit Cloud**:

1. Push code to GitHub
2. Connect repository to [share.streamlit.io](https://share.streamlit.io)
3. Select `app.py` as main file
4. Deploy!

---

## 📝 Requirements

```txt
pandas>=2.0.0
numpy>=1.24.0
scikit-learn>=1.3.0
xgboost>=2.0.0
joblib>=1.3.0
streamlit>=1.28.0
plotly>=5.0.0
```

---

## 🔮 Future Improvements

- [ ] Add interactive map visualization
- [ ] Include more property features (surface area, energy rating)
- [ ] Implement model retraining pipeline
- [ ] Add comparison with similar properties
- [ ] Multi-language support (EN/FR/NL)

---

## 📚 Related Projects

| Project | Description |
|---------|-------------|
| [Immo-Eliza-ML](https://github.com/yourusername/immo-eliza-ml) | Model training and experimentation |


---

## 👤 Author

**Astha Gudgilla**

---

## 📄 License

This project is part of the **BeCode AI Bootcamp**.

---

