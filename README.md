
# 👶 Pediatric Dosing: Then & Now Dashboard

## 🌟 Project Overview

This project is an **interactive, educational dashboard** built with **Streamlit** and **Python** designed to illustrate the critical evolution of **pediatric drug dosing** practices.

It visually compares two methods: the historical, age-based **Young's Rule** (circa 1838) and the **Modern Weight-Based Standard**. The dashboard clearly shows how reliance on a child's weight, rather than just age, leads to significantly more accurate and safer dosage calculations.

**⚠️ Disclaimer:** This tool is for **educational purposes only**. The drug data and calculations provided are illustrative and **must not be used for actual clinical decision-making**. Always consult professional medical guidelines (like the BNFc or Harriet Lane Handbook) for real-world dosing.

## ✨ Key Features

The dashboard is organized into three main pages:

1.  **Home:** An introductory page providing an overview of the project's purpose.
2.  **Then & Now Calculator:**
    * Allows users to select a **Drug** from a pre-defined list (e.g., Amoxicillin, Ibuprofen).
    * Inputs for **Child's Age (years)** and **Weight (kg)**.
    * Calculates and displays doses based on both the **Young's Rule (Historical)** and the **Weight-Based Method (Modern)**.
    * Provides a **visual comparison (bar chart)** and a simple **analysis** highlighting the potential difference (under/over-dosing).
3.  **About the Project:** Explains the mathematical formulas used for both the historical (Young's Rule) and modern (Weight-Based) dosing methods.

## 🚀 Getting Started

Follow these instructions to set up and run the dashboard locally.

### Prerequisites

* **Python 3.8+**
* **A `c.mp4` video file** (A looping background video of a baby is used for the aesthetic theme. The included file should be placed in the project root.)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone (https://github.com/himachand-dev/Dose-Adjustment-Tool)
    cd Dose-adjustment-Tool # or your folder name
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    The core dependencies are Streamlit, Pandas, Plotly, and `streamlit-option-menu`.
    ```bash
    pip install streamlit pandas plotly-express streamlit-option-menu
    ```
    *(Alternatively, create a `requirements.txt` file and run `pip install -r requirements.txt`)*

### Running the Dashboard

1.  **Execute the Streamlit application:**
    ```bash
    streamlit run a.py
    ```

2.  The application will automatically launch in your default web browser at `http://localhost:8501`.

## ⚙️ Project Structure

````

.
├── a.py                      \# Main Streamlit application file
├── c.mp4                     \# Background video file (set via base64 embedding)
└── drug\_data.py              \# Python file containing the `get_drug_data()` function

```

## 🛠️ Technologies Used

* **Python:** Core programming language.
* **Streamlit:** For building and deploying the interactive web dashboard.
* **Pandas:** Data handling and preparation.
* **Plotly Express:** Generating the interactive dose comparison bar chart.
* **Custom CSS/HTML:** Used in `a.py` for setting the centered video background and styling.

## 📝 Dosing Formulas

The project uses the following formulas for comparison:

#### **Young's Rule (Historical)**
$$\text{Child's Dose} = \frac{\text{Age of Child}}{\text{Age of Child} + 12} \times \text{Adult Dose}$$

#### **Modern Weight-Based Dosing (Standard)**
$$\text{Child's Dose} = \text{Weight (kg)} \times \text{Dose (mg/kg)}$$

The modern dose is also capped by the adult maximum dose for safety illustration.

## 👨‍💻 Author

* **Project Name:** Pediatric Dosing Dashboard: Then & Now
* **Author:** VUYALALA HIMACHAND
* **Class/Date:** V Pharm. D / 19-09-2025

---
```
