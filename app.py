import streamlit as st
import joblib
from predict import predict_price
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Immo Eliza PricePredict",
    page_icon="🏡",
    layout="wide"
)
    
# ---------------- HEADER ----------------
st.title("🏡 Immo Eliza PricePredict")
st.write("Get an instant price estimate for properties in Belgium")

# Banner image (wide rectangle)
st.image(
    "https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=1200&h=300&fit=crop",
    use_container_width=True
)


# ---------------- REGION & POSTAL LOGIC ----------------
postal_to_province = {
    "Antwerp": range(2000, 3000),
    "East-Flanders": range(9000, 10000),
    "West-Flanders": range(8000, 9000),
    "Flemish-Brabant": list(range(1500, 2000)) + list(range(3000, 3500)),
    "Brussels": range(1000, 1300),
    "Limburg": range(3500, 4000),
    "Luik": range(4000, 5000),
    "Namur": range(5000, 6000),
    "Hainaut": list(range(6000, 6600)) + list(range(7000, 8000)),
    "Luxembourg": range(6600, 7000),
    "Brabant-Wallon": range(1300, 1500)
}

province_to_region = {
    "Antwerp": "Flanders",
    "East-Flanders": "Flanders",
    "West-Flanders": "Flanders",
    "Flemish-Brabant": "Flanders",
    "Limburg": "Flanders",
    "Brussels": "Brussels",
    "Luik": "Wallonia",
    "Namur": "Wallonia",
    "Hainaut": "Wallonia",
    "Luxembourg": "Wallonia",
    "Brabant-Wallon": "Wallonia"
}

# Combine postal codes by region
region_postal_codes = {"Brussels": [], "Flanders": [], "Wallonia": []}
for province, codes in postal_to_province.items():
    region = province_to_region[province]
    region_postal_codes[region] += list(codes)
for region in region_postal_codes:
    region_postal_codes[region].sort()

# # ---------------- TWO-COLUMN FULL-PAGE FORM ----------------
# st.markdown("### 📝 Property Details")

# col1, col2 = st.columns(2)

# with col1:
#     bedrooms = st.number_input("Number of bedrooms", min_value=0, max_value=20, value=3)
#     bathrooms = st.number_input("Number of bathrooms", min_value=0, max_value=20, value=1)
#     toilets = st.number_input("Number of toilets", min_value=0, max_value=20, value=1)
#     property_type = st.selectbox(
#         "Property Type", 
#         ["apartment", "house", "studio", "villa", "land", "commercial-building"]
#     )

# with col2:
#     region = st.selectbox("Region", list(region_postal_codes.keys()))
#     postal_code = st.selectbox("Postal Code", region_postal_codes[region])
#     elevator = st.checkbox("Elevator")
#     garden = st.checkbox("Garden")
#     garage = st.checkbox("Garage")
#     swimming_pool = st.checkbox("Swimming Pool")


# # --- SIDEBAR SUMMARY PANEL ---
# st.sidebar.header("✅ Your Property Summary")
# st.sidebar.write(f"**Bedrooms:** {bedrooms}")
# st.sidebar.write(f"**Bathrooms:** {bathrooms}")
# st.sidebar.write(f"**Toilets:** {toilets}")
# st.sidebar.write(f"**Type:** {property_type}")
# st.sidebar.write(f"**Region:** {region}")
# st.sidebar.write(f"**Postal Code:** {postal_code}")
# st.sidebar.write(f"**Elevator:** {'Yes' if elevator else 'No'}")
# st.sidebar.write(f"**Garden:** {'Yes' if garden else 'No'}")
# st.sidebar.write(f"**Garage:** {'Yes' if garage else 'No'}")
# st.sidebar.write(f"**Swimming Pool:** {'Yes' if swimming_pool else 'No'}")

# st.write("")  # spacing

# # ---------------- FULL-WIDTH PREDICT BUTTON ----------------

# if st.button("🔮 Predict Price", use_container_width=True):
#     input_data = {
#         "Number of bedrooms": bedrooms,
#         "Number of bathrooms": bathrooms,
#         "Number of toilets": toilets,
#         "type": property_type,
#         "Region": region,
#         "Elevator": int(elevator),
#         "Garden": int(garden),
#         "Garage": int(garage),
#         "Swimming pool": int(swimming_pool),
#         "postal_code": postal_code
#     }
    
#     price, metrics = predict_price(input_data)

# # ---------------- PREDICTION RESULTS ----------------

#     low_price = price - metrics["val_mae"]
#     high_price = price + metrics["val_mae"]

#     # st.sidebar.subheader("💰 Price Range")

#     # st.sidebar.write("Low Price:")
#     # st.sidebar.badge(f"€{low_price:,.2f}", color="orange")  

#     # st.sidebar.write("High Price:")
#     # st.sidebar.badge(f"€{high_price:,.2f}", color="blue") 

# # ---------------- RESULTS ----------------
#     st.markdown("---")
#     st.subheader("🏷️ Prediction Results")
    
#     # Three metric cards
#     col1, col2, col3 = st.columns(3)
    
#     with col1:
#         st.metric(label="📉 Low Estimate", value=f"€{low_price:,.0f}")
    
#     with col2:
#         st.metric(label="💰 Predicted Price", value=f"€{price:,.0f}")
    
#     with col3:
#         st.metric(label="📈 High Estimate", value=f"€{high_price:,.0f}")
    
#     # Visual range bar (full width)
#     st.markdown("""
#     <div style="width: 100%; height: 30px; background: linear-gradient(to right, #FFA726, #1E88E5, #66BB6A); border-radius: 15px; margin: 10px 0;"></div>
#     """, unsafe_allow_html=True)

# # ---------------- FOOTER ----------------
# st.markdown("---")
# st.markdown(
#     """
#     <div style='text-align: center; color: #888; padding: 20px; font-size: 14px;'>
#         <p><strong>Immo Eliza PricePredict</strong></p>
#         <p>📊 Model: XGBoost | 📍 Coverage: Belgium | 🏠 Data: Immovlan</p>
#         <p style='font-size: 12px; margin-top: 10px;'>
#             ⚠️ Disclaimer: Predictions are estimates based on historical data and should not be used as the sole basis for financial decisions.
#         </p>
#     </div>
#     """,
#     unsafe_allow_html=True
# )
# st.caption("© 2025 Immo Eliza")


# ---------------- TABS ----------------
tab1, tab2 = st.tabs(["🏠 Prediction", "📊 Analysis"])

# ============================================
# TAB 1: PREDICTION
# ============================================
with tab1:
    st.markdown("### 📝 Property Details")
    
    col1, col2 = st.columns(2)
    
    with col1:
        bedrooms = st.number_input("Number of bedrooms", min_value=0, max_value=20, value=3)
        bathrooms = st.number_input("Number of bathrooms", min_value=0, max_value=20, value=1)
        toilets = st.number_input("Number of toilets", min_value=0, max_value=20, value=1)
        property_type = st.selectbox(
            "Property Type", 
            ["apartment", "house", "studio", "villa", "land", "commercial-building"]
        )
    
    with col2:
        region = st.selectbox("Region", list(region_postal_codes.keys()))
        postal_code = st.selectbox("Postal Code", region_postal_codes[region])
        elevator = st.checkbox("Elevator")
        garden = st.checkbox("Garden")
        garage = st.checkbox("Garage")
        swimming_pool = st.checkbox("Swimming Pool")
    
    st.write("")
    
    # ---------------- PREDICT BUTTON ----------------
    if st.button("🔮 Predict Price", use_container_width=True):
        input_data = {
            "Number of bedrooms": bedrooms,
            "Number of bathrooms": bathrooms,
            "Number of toilets": toilets,
            "type": property_type,
            "Region": region,
            "Elevator": int(elevator),
            "Garden": int(garden),
            "Garage": int(garage),
            "Swimming pool": int(swimming_pool),
            "postal_code": postal_code
        }
        
        # Spinner while predicting
        with st.spinner("🔍 Analyzing property..."):
            price, metrics = predict_price(input_data)
        
        # Success message
        st.success("✅ Prediction complete!")
        
        # Calculate price range
        low_price = price - metrics["val_mae"]
        high_price = price + metrics["val_mae"]
        
        # ---------------- RESULTS ----------------
        st.markdown("---")
        st.subheader("🏷️ Prediction Results")
        
        # Three metric cards
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(label="📉 Low Estimate", value=f"€{low_price:,.0f}")
        
        with col2:
            st.metric(label="💰 Predicted Price", value=f"€{price:,.0f}")
        
        with col3:
            st.metric(label="📈 High Estimate", value=f"€{high_price:,.0f}")
        
        # Visual range bar
        st.markdown("""
        <div style="width: 100%; height: 30px; background: linear-gradient(to right, #FFA726, #1E88E5, #66BB6A); border-radius: 15px; margin: 10px 0;"></div>
        """, unsafe_allow_html=True)


# ============================================
# TAB 2: ANALYSIS
# ============================================
with tab2:
    st.markdown("### 🎯 What Affects Property Price?")
    st.write("This chart shows which features have the most impact on price prediction.")
    
    # Real feature importance from your model (sorted by importance)
    features = ['Number of bathrooms', 'Number of toilets', 'Elevator', 'Garden', 
                'Type', 'Swimming pool', 'Postal code', 'Region', 'Garage', 'Number of bedrooms']
    importance = [22.8, 16.9, 11.5, 9.4, 9.1, 7.4, 7.3, 6.8, 4.7, 4.1]
    
    # Funnel chart (fixed)
    fig = px.funnel(
        x=importance,
        y=features,
        title="Feature Importance Ranking"
    )
    fig.update_layout(
        height=500,
        showlegend=False
    )
    fig.update_traces(
        texttemplate='%{x:.1f}%',
        textposition='inside',
        marker_color='#1E88E5'  # Blue color
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Key insights
    st.markdown("### 💡 Key Insights")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **🚿 Number of Bathrooms** has the biggest impact (22.8%).
        More bathrooms significantly increases property value.
        """)
        
        st.info("""
        **🚽 Number of Toilets** is second most important (16.9%).
        Properties with more toilets command higher prices.
        """)
    
    with col2:
        st.info("""
        **🛗 Elevator** adds significant value (11.5%).
        Essential for apartments in multi-story buildings.
        """)
        
        st.info("""
        **🌳 Garden & Pool** together contribute ~17%.
        Outdoor amenities add premium value.
        """)
# ---------------- SIDEBAR SUMMARY ----------------
st.sidebar.header("✅ Your Property Summary")
st.sidebar.write(f"**Bedrooms:** {bedrooms}")
st.sidebar.write(f"**Bathrooms:** {bathrooms}")
st.sidebar.write(f"**Toilets:** {toilets}")
st.sidebar.write(f"**Type:** {property_type}")
st.sidebar.write(f"**Region:** {region}")
st.sidebar.write(f"**Postal Code:** {postal_code}")
st.sidebar.write(f"**Elevator:** {'Yes' if elevator else 'No'}")
st.sidebar.write(f"**Garden:** {'Yes' if garden else 'No'}")
st.sidebar.write(f"**Garage:** {'Yes' if garage else 'No'}")
st.sidebar.write(f"**Swimming Pool:** {'Yes' if swimming_pool else 'No'}")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #888; padding: 20px; font-size: 14px;'>
        <p><strong>Immo Eliza PricePredict</strong></p>
        <p>📊 Model: XGBoost | 📍 Coverage: Belgium | 🏠 Data: Immovlan</p>
        <p style='font-size: 12px; margin-top: 10px;'>
            ⚠️ Disclaimer: Predictions are estimates based on historical data and should not be used as the sole basis for financial decisions.
        </p>
        <p style='font-size: 12px; margin-top: 15px; color: #aaa;'>© 2025 Immo Eliza</p>
    </div>
    """,
    unsafe_allow_html=True
)

