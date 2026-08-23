import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)

import matplotlib.pyplot as plt


# ==========================================
# AI SMART OSCILLOSCOPE
# STAGE 07 — AI SIGNAL CLASSIFICATION
# ==========================================


# ------------------------------------------
# Parameters
# ------------------------------------------

sampling_frequency = 1000
duration = 1

number_of_samples = int(
    sampling_frequency * duration
)


# ==========================================
# GENERATE TRAINING DATA
# ==========================================

dataset = []

np.random.seed(42)


# Create many signal examples

for i in range(300):

    # Random signal frequency

    frequency = np.random.uniform(
        2,
        20
    )


    # Random amplitude

    amplitude = np.random.uniform(
        0.5,
        2.0
    )


    # Random noise level

    noise_level = np.random.uniform(
        0.02,
        0.60
    )


    # Time axis

    time = np.linspace(
        0,
        duration,
        number_of_samples,
        endpoint=False
    )


    # Clean signal

    clean_signal = (
        amplitude
        * np.sin(
            2
            * np.pi
            * frequency
            * time
        )
    )


    # Noise

    noise = np.random.normal(
        0,
        noise_level,
        number_of_samples
    )


    # Noisy signal

    signal = (
        clean_signal + noise
    )


    # ======================================
    # FEATURE 1 — RMS
    # ======================================

    rms = np.sqrt(
        np.mean(
            signal ** 2
        )
    )


    # ======================================
    # FEATURE 2 — STANDARD DEVIATION
    # ======================================

    standard_deviation = np.std(
        signal
    )


    # ======================================
    # FEATURE 3 — PEAK-TO-PEAK
    # ======================================

    peak_to_peak = (
        np.max(signal)
        - np.min(signal)
    )


    # ======================================
    # FEATURE 4 — FFT FREQUENCY
    # ======================================

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


    # ======================================
    # FEATURE 5 — SNR
    # ======================================

    signal_rms = np.sqrt(
        np.mean(
            clean_signal ** 2
        )
    )

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


    # ======================================
    # SIGNAL QUALITY LABEL
    # ======================================

    if snr_db >= 20:

        quality = "GOOD"

    elif snr_db >= 10:

        quality = "MODERATE"

    else:

        quality = "POOR"


    # ======================================
    # STORE FEATURES
    # ======================================

    dataset.append({

        "rms": rms,

        "standard_deviation":
            standard_deviation,

        "peak_to_peak":
            peak_to_peak,

        "dominant_frequency":
            dominant_frequency,

        "snr_db":
            snr_db,

        "quality":
            quality
    })


# ==========================================
# CREATE DATAFRAME
# ==========================================

df = pd.DataFrame(
    dataset
)


print("=" * 70)

print(
    "          AI SMART OSCILLOSCOPE"
)

print(
    "           SIGNAL CLASSIFIER"
)

print("=" * 70)


print(
    "\nDataset Size:"
)

print(
    len(df)
)


print(
    "\nClass Distribution:"
)

print(
    df["quality"].value_counts()
)


# ==========================================
# FEATURES AND TARGET
# ==========================================

features = [
    "rms",
    "standard_deviation",
    "peak_to_peak",
    "dominant_frequency",
    "snr_db"
]


X = df[features]

y = df["quality"]


# ==========================================
# TRAIN / TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = (
    train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )
)


print(
    "\nTraining Samples:",
    len(X_train)
)

print(
    "Testing Samples :",
    len(X_test)
)


# ==========================================
# CREATE RANDOM FOREST
# ==========================================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# ==========================================
# TRAIN MODEL
# ==========================================

model.fit(
    X_train,
    y_train
)


print(
    "\n✅ AI model trained!"
)


# ==========================================
# PREDICTION
# ==========================================

predictions = model.predict(
    X_test
)


# ==========================================
# ACCURACY
# ==========================================

accuracy = accuracy_score(
    y_test,
    predictions
)


print(
    f"\nAccuracy: "
    f"{accuracy * 100:.2f}%"
)


# ==========================================
# CLASSIFICATION REPORT
# ==========================================

print(
    "\nClassification Report"
)

print(
    "-" * 70
)

print(
    classification_report(
        y_test,
        predictions,
        zero_division=0
    )
)


# ==========================================
# CONFUSION MATRIX
# ==========================================

matrix = confusion_matrix(
    y_test,
    predictions,
    labels=[
        "GOOD",
        "MODERATE",
        "POOR"
    ]
)


print(
    "\nConfusion Matrix"
)

print(
    matrix
)


display = ConfusionMatrixDisplay(
    confusion_matrix=matrix,
    display_labels=[
        "GOOD",
        "MODERATE",
        "POOR"
    ]
)


display.plot()


plt.title(
    "AI Signal Quality Classifier",
    fontsize=16,
    fontweight="bold"
)

plt.tight_layout()


plt.savefig(
    "signal_classifier_confusion_matrix.png",
    dpi=300,
    bbox_inches="tight"
)


plt.show()


# ==========================================
# FEATURE IMPORTANCE
# ==========================================

importance = (
    model.feature_importances_
)


feature_importance = pd.DataFrame({

    "feature": features,

    "importance": importance

})


feature_importance = (
    feature_importance
    .sort_values(
        "importance",
        ascending=False
    )
)


print(
    "\nFeature Importance"
)

print(
    "-" * 70
)

print(
    feature_importance.to_string(
        index=False
    )
)


# ==========================================
# SAVE DATASET
# ==========================================

df.to_csv(
    "ai_signal_training_data.csv",
    index=False
)


print(
    "\n✅ Training dataset saved!"
)

print(
    "✅ Confusion matrix saved!"
)

print(
    "\n🎉 STAGE 07 COMPLETED!"
)
