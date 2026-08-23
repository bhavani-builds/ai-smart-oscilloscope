import numpy as np
import pandas as pd
import streamlit as st

from sklearn.ensemble import RandomForestClassifier


# ==========================================
# AI SMART OSCILLOSCOPE
# STAGE 09 — INTERACTIVE DASHBOARD
# ==========================================


# ------------------------------------------
# Page configuration
# ------------------------------------------

st.set_page_config(
    page_title="AI Smart Oscilloscope",
    page_icon="📡",
    layout="wide"
)


# ------------------------------------------
# Title
# ------------------------------------------

st.title(
    "📡 AI Smart Oscilloscope"
)

st.write(
    "Interactive signal analysis, FFT, "
    "noise analysis and AI-based signal "
    "quality classification."
)

st.divider()


# ==========================================
# SIDEBAR CONTROLS
# ==========================================

st.sidebar.header(
    "⚙️ Signal Controls"
)


frequency = st.sidebar.slider(
    "Frequency (Hz)",
    min_value=1,
    max_value=50,
    value=5
)


amplitude = st.sidebar.slider(
    "Amplitude",
    min_value=0.1,
    max_value=5.0,
    value=1.0,
    step=0.1
)


noise_level = st.sidebar.slider(
    "Noise Level",
    min_value=0.0,
    max_value=0.60,
    value=0.18,
    step=0.01
)


sampling_frequency = st.sidebar.slider(
    "Sampling Frequency (Hz)",
    min_value=100,
    max_value=5000,
    value=1000,
    step=100
)


duration = 1


# ==========================================
# GENERATE SIGNAL
# ==========================================

number_of_samples = int(
    sampling_frequency * duration
)


time = np.linspace(
    0,
    duration,
    number_of_samples,
    endpoint=False
)


np.random.seed(42)


clean_signal = (
    amplitude
    * np.sin(
        2
        * np.pi
        * frequency
        * time
    )
)


noise = np.random.normal(
    0,
    noise_level,
    number_of_samples
)


signal = (
    clean_signal + noise
)


# ==========================================
# SIGNAL MEASUREMENTS
# ==========================================

maximum = np.max(signal)

minimum = np.min(signal)

peak_to_peak = (
    maximum - minimum
)

rms = np.sqrt(
    np.mean(
        signal ** 2
    )
)

mean_value = np.mean(signal)

standard_deviation = np.std(
    signal
)


# ==========================================
# FFT
# ==========================================

fft_result = np.fft.fft(
    signal
)


frequencies = np.fft.fftfreq(
    number_of_samples,
    1 / sampling_frequency
)


magnitude = (
    np.abs(fft_result)
    / number_of_samples
)


positive_frequencies = (
    frequencies[
        :number_of_samples // 2
    ]
)


positive_magnitude = (
    magnitude[
        :number_of_samples // 2
    ]
)


peak_index = np.argmax(
    positive_magnitude
)


dominant_frequency = (
    positive_frequencies[
        peak_index
    ]
)


# ==========================================
# SNR
# ==========================================

signal_rms = np.sqrt(
    np.mean(
        clean_signal ** 2
    )
)


if noise_level > 0:

    noise_rms = np.sqrt(
        np.mean(
            noise ** 2
        )
    )

    snr_db = (
        20
        * np.log10(
            signal_rms
            / noise_rms
        )
    )

else:

    noise_rms = 0

    snr_db = 100


# ==========================================
# SIGNAL QUALITY
# ==========================================

if snr_db >= 20:

    signal_quality = "GOOD"

elif snr_db >= 10:

    signal_quality = "MODERATE"

else:

    signal_quality = "POOR"


# ==========================================
# DASHBOARD OVERVIEW
# ==========================================

st.subheader(
    "📊 Signal Measurements"
)


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Frequency",
        f"{frequency} Hz"
    )


with col2:

    st.metric(
        "Amplitude",
        f"{amplitude:.2f}"
    )


with col3:

    st.metric(
        "RMS",
        f"{rms:.3f}"
    )


with col4:

    st.metric(
        "Peak-to-Peak",
        f"{peak_to_peak:.3f}"
    )


# ==========================================
# WAVEFORM
# ==========================================

st.divider()

st.subheader(
    "📈 Time-Domain Waveform"
)


waveform_data = pd.DataFrame({

    "Amplitude": signal

})


st.line_chart(
    waveform_data,
    height=400
)


# ==========================================
# FFT
# ==========================================

st.divider()

st.subheader(
    "📡 Frequency Spectrum — FFT"
)


fft_data = pd.DataFrame({

    "Magnitude":
        positive_magnitude

})


fft_data.index = (
    positive_frequencies
)


st.line_chart(
    fft_data,
    height=350
)


st.write(
    f"**Dominant Frequency:** "
    f"{dominant_frequency:.2f} Hz"
)


# ==========================================
# NOISE ANALYSIS
# ==========================================

st.divider()

st.subheader(
    "📢 Noise Analysis"
)


noise_col1, noise_col2, noise_col3 = (
    st.columns(3)
)


with noise_col1:

    st.metric(
        "Noise RMS",
        f"{noise_rms:.4f}"
    )


with noise_col2:

    st.metric(
        "SNR",
        f"{snr_db:.2f} dB"
    )


with noise_col3:

    st.metric(
        "Standard Deviation",
        f"{standard_deviation:.4f}"
    )


# ==========================================
# QUALITY STATUS
# ==========================================

st.divider()

st.subheader(
    "🎯 Signal Quality"
)


if signal_quality == "GOOD":

    st.success(
        "🟢 GOOD SIGNAL QUALITY"
    )

elif signal_quality == "MODERATE":

    st.warning(
        "🟡 MODERATE SIGNAL QUALITY"
    )

else:

    st.error(
        "🔴 POOR SIGNAL QUALITY"
    )


# ==========================================
# QUALITY SCORE
# ==========================================

snr_score = np.clip(
    (snr_db / 30) * 100,
    0,
    100
)


quality_score = round(
    snr_score,
    2
)


st.metric(
    "Signal Quality Score",
    f"{quality_score}/100"
)


# ==========================================
# RECOMMENDATION
# ==========================================

st.subheader(
    "🔧 Engineering Recommendation"
)


if signal_quality == "GOOD":

    recommendation = (
        "Signal quality is good. "
        "No immediate action is required."
    )

elif signal_quality == "MODERATE":

    recommendation = (
        "Noticeable noise is present. "
        "Check signal connections and "
        "measurement conditions."
    )

else:

    recommendation = (
        "High noise level detected. "
        "Inspect the signal source, "
        "connections and measurement setup."
    )


st.info(
    recommendation
)


# ==========================================
# TECHNICAL INFORMATION
# ==========================================

st.divider()

st.subheader(
    "🔬 Technical Information"
)


technical_data = pd.DataFrame({

    "Parameter": [

        "Sampling Frequency",

        "Number of Samples",

        "Mean",

        "Maximum",

        "Minimum",

        "RMS",

        "Peak-to-Peak",

        "Dominant Frequency",

        "SNR"

    ],

    "Value": [

        f"{sampling_frequency} Hz",

        number_of_samples,

        f"{mean_value:.4f}",

        f"{maximum:.4f}",

        f"{minimum:.4f}",

        f"{rms:.4f}",

        f"{peak_to_peak:.4f}",

        f"{dominant_frequency:.2f} Hz",

        f"{snr_db:.2f} dB"

    ]

})


st.dataframe(
    technical_data,
    width="stretch"
)


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "AI Smart Oscilloscope — Educational "
    "ECE/DSP/ML Portfolio Project"
)
