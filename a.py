import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from drug_data import get_drug_data  # Your drug data file

import streamlit as st
import base64

def set_bg_video_centered(video_file, video_opacity=0.5, width="100vw", height="85vh", border_radius="24px"):
    with open(video_file, "rb") as video:
        video_bytes = video.read()
    video_base64 = base64.b64encode(video_bytes).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            position: relative;
            min-height: 100vh;
        }}
        #bgvid {{
            position: fixed;
            top: 50%;
            left: 50%;
            width: {width};
            height: {height};
            transform: translate(-50%, -50%);
            object-fit: cover;
            z-index: -1;
            opacity: {video_opacity};
            border-radius: {border_radius};
            box-shadow: 0 8px 32px 0 rgba(50, 50, 93, 0.15);
        }}
        .block-container {{
            position: relative;
            z-index: 1;
            background: transparent !important;
        }}
        </style>
        <video autoplay loop muted id="bgvid">
            <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
        </video>
        """,
        unsafe_allow_html=True
    )

# Usage: adjust width, height, and opacity as needed
set_bg_video_centered("c.mp4", video_opacity=0.8, width="100vw", height="100vh")

# --- Page Configuration ---
st.set_page_config(
    page_title="Pediatric Dosing Dashboard",
    page_icon="👶",
    layout="wide"
)

# --- Top Navigation Bar ---
selected_page = option_menu(
    menu_title=None,
    options=["Home", "Then & Now Calculator", "About the Project"],
    icons=["house-heart", "calculator-fill", "info-circle"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "20px"},
        "nav-link": {
            "font-size": "16px",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#eee",
        },
        "nav-link-selected": {"background-color": "#02ab21"},
    },
)

# --- Load Data (once) ---
drug_df = get_drug_data()

def render_home_page():
    st.title("Pediatric Dosing: Then & Now ⏳")
    st.markdown("---")
    st.markdown(
        """
        ### Welcome to the Pediatric Dosing Dashboard!

        This interactive tool is designed for **educational purposes** to explore the evolution of pediatric pharmacology.
        It visually demonstrates the difference between historical age-based formulas and modern weight-based dosing standards.

        **Select a page from the top navigation bar to get started:**

        - **Then & Now Calculator:** Interactively calculate and compare drug doses.
        - **About the Project:** Learn more about the formulas used.
        """
    )


def render_calculator_page():
    # --- Calculation Functions ---
    def youngs_rule(age, adult_dose):
        if age <= 0 or age > 12: return 0
        return (age / (age + 12)) * adult_dose

    def weight_based_dose(weight, mg_per_kg, max_dose):
        calculated_dose = weight * mg_per_kg
        return min(calculated_dose, max_dose)

    # --- UI Layout ---
    st.title("Then & Now: A Dosing Comparison")
    st.markdown("Compare the historical **Young's Rule** with the **Modern Weight-Based Standard**.")
    st.markdown("---")

    # --- Inputs ---
    col1, col2 = st.columns(2)
    with col1:
        selected_drug = st.selectbox("Select a Drug:", options=drug_df['Drug'], index=0)

    drug_note = drug_df[drug_df['Drug'] == selected_drug]['Notes'].values[0]
    with col2:
        st.write(" ")
        st.info(f"**Dosing Note:** {drug_note}", icon="💡")

    age = st.number_input("Enter Child's Age (years):", min_value=1, max_value=12, value=4, step=1)
    weight = st.number_input("Enter Child's Weight (kg):", min_value=5.0, max_value=60.0, value=18.0, step=0.5, format="%.1f")
    st.markdown("---")

    # --- Get Drug Info ---
    adult_dose_mg = drug_df.loc[drug_df['Drug'] == selected_drug, 'Adult Dose (mg)'].values[0]
    mg_per_kg = drug_df.loc[drug_df['Drug'] == selected_drug, 'Dose (mg/kg)'].values[0]

    # --- Calculations ---
    youngs_dose = youngs_rule(age, adult_dose_mg)
    modern_dose = weight_based_dose(weight, mg_per_kg, adult_dose_mg)

    # --- Display Results ---
    st.header("Dosage Calculation Results")
    col_then, col_now = st.columns(2)
    with col_then:
        st.subheader("Then: Young's Rule")
        st.warning("⚠️ Historical formula - Not for clinical use.")
        if youngs_dose > 0:
            st.metric(label="Calculated Dose (mg)", value=f"{youngs_dose:.2f}")
            st.write(f"Based on age **{age} years** and adult dose **{adult_dose_mg} mg**.")
        else:
            st.error("Young's Rule is not applicable for this age.")

    with col_now:
        st.subheader("Now: Weight-Based")
        st.success("✅ Current clinical standard.")
        if mg_per_kg > 0:
            st.metric(label="Calculated Dose (mg)", value=f"{modern_dose:.2f}")
            st.write(f"Based on weight **{weight} kg** at **{mg_per_kg} mg/kg** (capped at {adult_dose_mg} mg).")
        else:
            st.info(f"{selected_drug} is not typically dosed systemically.")

    st.markdown("---")
    # --- Visualization (only once!) ---
    st.header("Visual Comparison")
    if youngs_dose > 0 and modern_dose > 0:
        chart_data = pd.DataFrame({'Method': ["Young's Rule (Then)", "Weight-Based (Now)"], 'Dose (mg)': [youngs_dose, modern_dose]})
        fig = px.bar(chart_data, x='Method', y='Dose (mg)', color='Method',
                     color_discrete_map={"Young's Rule (Then)": "#FF6B6B", "Weight-Based (Now)": "#6BCB77"},
                     title=f"Dose Comparison for a {age}-year-old weighing {weight} kg", text_auto=True)
        fig.update_layout(showlegend=False, yaxis_title="Dose (mg)", xaxis_title="")
        st.plotly_chart(fig, use_container_width=True)

        difference = modern_dose - youngs_dose
        st.subheader("Analysis")
        if abs(difference) < 1:
            st.write("The doses are nearly identical for this specific age and weight.")
        elif difference > 0:
            st.write(f"Young's Rule **under-doses** by **{abs(difference):.2f} mg**. This could lead to ineffective treatment.")
        else:
            st.write(f"Young's Rule **over-doses** by **{abs(difference):.2f} mg**. This could increase the risk of side effects.")
    else:
        st.info("A visual comparison cannot be generated for this drug or age.")

def render_about_page():
    st.title("About This Project 📜")
    st.markdown("---")
    st.header("The Goal: Education Through Comparison")
    st.write(
        """
        The purpose of this dashboard is to provide an interactive, educational experience on the evolution of
        pediatric drug dosing. By placing a historical formula next to the modern standard, we can clearly
        see why pharmacology has advanced and why personalized medicine, even as simple as dosing by weight, is so crucial.
        """
    )
    st.header("The Formulas Used")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Young's Rule (Circa 1838)")
        st.latex(r'''\text{Child's Dose} = \frac{\text{Age of Child}}{\text{Age of Child} + 12} \times \text{Adult Dose}''')
        st.markdown("- **Pros:** Simple and easy to calculate without modern tools.\n- **Cons:** Highly inaccurate.")
    with col2:
        st.subheader("Modern Weight-Based Dosing")
        st.latex(r'''\text{Child's Dose} = \text{Weight (kg)} \times \text{Dose (mg/kg)}''')
        st.markdown("- **Pros:** Far more accurate as it's tailored to the individual child's body mass.\n- **Cons:** Requires an accurate weight.")
    st.markdown("---")

# --- Main App Logic ---
if selected_page == "Home":
    render_home_page()
elif selected_page == "Then & Now Calculator":
    render_calculator_page()
elif selected_page == "About the Project":
    render_about_page()
