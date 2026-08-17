import streamlit as st
import sys
import os

# =========================================================
# IMPORT MODEL
# =========================================================

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "src")
    )
)

from predict import predict_message


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Scam Intelligence",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# GLOBAL CSS
# =========================================================

st.html("""
<style>

.stApp {
    background:
        radial-gradient(
            circle at top left,
            rgba(127, 29, 29, 0.25),
            transparent 35%
        ),
        radial-gradient(
            circle at bottom right,
            rgba(220, 38, 38, 0.10),
            transparent 35%
        ),
        #080808;
}

/* Hide Streamlit chrome */
#MainMenu {
    visibility: hidden;
}

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* Main width */
.block-container {
    max-width: 1050px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Hero */
.hero {
    padding: 35px;
    border-radius: 22px;

    background:
        linear-gradient(
            135deg,
            rgba(255,255,255,0.06),
            rgba(255,255,255,0.015)
        );

    border: 1px solid rgba(255,255,255,0.10);

    box-shadow:
        0 20px 60px rgba(0,0,0,0.40);

    margin-bottom: 30px;
}

.hero-title {
    font-size: 42px;
    font-weight: 900;
    color: white;
    letter-spacing: -1px;
}

.hero-title span {
    color: #ef4444;
}

.hero-subtitle {
    margin-top: 8px;
    color: #a1a1aa;
    font-size: 17px;
}

/* Section title */
.section-title {
    color: white;
    font-size: 22px;
    font-weight: 800;
    margin: 25px 0 15px 0;
}

/* Result */
.result-card {
    margin-top: 30px;
    padding: 40px;
    border-radius: 22px;
    text-align: center;

    background:
        linear-gradient(
            145deg,
            rgba(239,68,68,0.12),
            rgba(255,255,255,0.025)
        );

    border: 1px solid rgba(239,68,68,0.30);

    box-shadow:
        0 0 50px rgba(239,68,68,0.08);
}

.result-label {
    color: #a1a1aa;
    font-size: 13px;
    text-transform: uppercase;
    letter-spacing: 2px;
}

.result-status {
    font-size: 40px;
    font-weight: 900;
    margin-top: 12px;
}

.result-confidence {
    font-size: 56px;
    font-weight: 900;
    margin-top: 10px;
}

.result-subtitle {
    color: #a1a1aa;
    font-size: 14px;
    margin-top: 5px;
}

.model-badge {
    display: inline-block;
    margin-top: 18px;
    padding: 8px 16px;

    border-radius: 999px;

    background: rgba(239,68,68,0.10);
    border: 1px solid rgba(239,68,68,0.25);

    color: #f87171;

    font-size: 13px;
    font-weight: 700;
}

/* Metric cards */
.metric-card {
    padding: 22px;
    border-radius: 16px;

    background: rgba(255,255,255,0.035);

    border: 1px solid rgba(255,255,255,0.08);

    min-height: 100px;
}

.metric-label {
    color: #a1a1aa;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.metric-value {
    color: white;
    font-size: 25px;
    font-weight: 800;
    margin-top: 8px;
}

/* Footer */
.footer {
    text-align: center;
    color: #71717a;

    font-size: 13px;

    margin-top: 45px;
    padding-top: 25px;

    border-top:
        1px solid rgba(255,255,255,0.06);
}

</style>
""")


# =========================================================
# HERO
# =========================================================

st.html("""
<div class="hero">

    <div class="hero-title">
        🛡️ SCAM <span>INTELLIGENCE</span>
    </div>

    <div class="hero-subtitle">
        Machine Learning powered message threat detection
    </div>

</div>
""")


# =========================================================
# MESSAGE INPUT
# =========================================================

st.html("""
<div class="section-title">
    🔎 Analyze a Message
</div>
""")

message = st.text_area(
    "Message",
    placeholder=(
        "Paste a suspicious message here...\n\n"
        "Example:\n"
        "Congratulations! You have won ₹50,000. "
        "Click this link to claim your prize."
    ),
    height=180,
    label_visibility="collapsed"
)


st.write("")


# =========================================================
# ANALYZE BUTTON
# =========================================================

if st.button(
    "🔍 ANALYZE MESSAGE",
    use_container_width=True
):

    if not message.strip():

        st.warning(
            "Please enter a message before analyzing."
        )

    else:

        # ---------------------------------------------
        # MODEL PREDICTION
        # ---------------------------------------------

        label, confidence = predict_message(message)

        confidence = max(
            0,
            min(100, confidence)
        )


        # ---------------------------------------------
        # RESULT CONFIG
        # ---------------------------------------------

        if label == "SCAM":

            status = "🚨 SCAM DETECTED"
            status_color = "#ef4444"

            description = (
                "This message contains patterns associated "
                "with scam or phishing content."
            )

        else:

            status = "✅ SAFE MESSAGE"
            status_color = "#22c55e"

            description = (
                "No strong scam patterns were detected "
                "in this message."
            )


        # =================================================
        # RESULT CARD
        # =================================================

        st.html(f"""
        <div class="result-card">

            <div class="result-label">
                Threat Analysis Result
            </div>

            <div
                class="result-status"
                style="color:{status_color};"
            >
                {status}
            </div>

            <div
                class="result-confidence"
                style="color:{status_color};"
            >
                {confidence:.2f}%
            </div>

            <div class="result-subtitle">
                Model Confidence
            </div>

            <div class="model-badge">
                TF-IDF • Logistic Regression
            </div>

            <div style="
                margin-top:20px;
                color:#a1a1aa;
                font-size:14px;
            ">
                {description}
            </div>

        </div>
        """)


        # =================================================
        # METRICS
        # =================================================

        st.html("""
        <div class="section-title">
            📊 Analysis Summary
        </div>
        """)

        col1, col2, col3 = st.columns(3)


        with col1:

            st.html(f"""
            <div class="metric-card">

                <div class="metric-label">
                    Prediction
                </div>

                <div
                    class="metric-value"
                    style="color:{status_color};"
                >
                    {label}
                </div>

            </div>
            """)


        with col2:

            st.html(f"""
            <div class="metric-card">

                <div class="metric-label">
                    Confidence
                </div>

                <div class="metric-value">
                    {confidence:.2f}%
                </div>

            </div>
            """)


        with col3:

            st.html("""
            <div class="metric-card">

                <div class="metric-label">
                    Model
                </div>

                <div class="metric-value">
                    Logistic Regression
                </div>

            </div>
            """)


        # =================================================
        # SAFETY MESSAGE
        # =================================================

        st.write("")

        if label == "SCAM":

            st.error(
                "⚠️ Avoid clicking unknown links, sharing "
                "OTPs, passwords, banking details, or "
                "sending money to unknown sources."
            )

        else:

            st.success(
                "No obvious scam patterns were detected. "
                "Always verify important messages through "
                "official channels."
            )


# =========================================================
# FOOTER
# =========================================================

st.html("""
<div class="footer">

    <strong>SCAM INTELLIGENCE DETECTOR</strong>

    <br><br>

    Built with Python • Scikit-Learn • TF-IDF • Streamlit

    <br><br>

    Machine Learning NLP Classification Project

</div>
""")