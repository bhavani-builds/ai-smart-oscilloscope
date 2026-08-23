import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestClassifier


# ==========================================
# AI SMART OSCILLOSCOPE
# STAGE 08 — SIGNAL QUALITY SCORE
# ==========================================


# ------------------------------------------
# Parameters
# ------------------------------------------

sampling_frequency = 1000
duration = 1
frequency = 5
amplitude = 1


# ------------------------------------------
# Generate training data
# ------------------------------------------

dataset = []

np.random.seed(42)


for i in range(300):

    test_frequency = np.random.uniform(
        2,
        20
    )

    test_amplitude = np.random.uniform(
        0.5,
        2.0
    )

    noise_level = np.random.uniform(
        0.02,
        0.60
    )

    samples = int(
        sampling_frequency * duration
    )

    time = np.linspace(
        0,
        duration,
        samples,
        endpoint=False
    )

    clean_signal = (
        test_amplitude
        * np.sin(
            2
            * np.pi
            * test_frequency
            * time
        )
    )

    noise = np.random.normal(
        0,
        noise_level,
        samples
    )

    signal = (
        clean_signal + noise
    )


    # --------------------------------------
    # Features
    # --------------------------------------

    rms = np.sqrt(
        np.mean(signal ** 2)
    )

    standard_deviation = np.std(
        signal
    )

    peak_to_peak = (
        np.max(signal)
        - np.min(signal)
    )


    # FFT

    fft_result = np.fft.fft(
        signal
    )

    frequencies = np.fft.fftfreq(
        samples,
        1 / sampling_frequency
    )

    magnitude = (
        np.abs(fft_result)
        / samples
    )

    positive_frequencies = (
        frequencies[:samples // 2]
    )

    positive_magnitude = (
        magnitude[:samples // 2]
    )

    peak_index = np.argmax(
        positive_magnitude
    )

    dominant_frequency = (
        positive_frequencies[peak_index]
    )


    # SNR

    signal_rms = np.sqrt(
        np.mean(clean_signal ** 2)
    )

    noise_rms = np.sqrt(
        np.mean(noise ** 2)
    )

    snr_db = (
        20
        * np.log10(
            signal_rms / noise_rms
        )
    )


    # Quality label

    if snr_db >= 20:

        quality = "GOOD"

    elif snr_db >= 10:

        quality = "MODERATE"

    else:

        quality = "POOR"


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


# ------------------------------------------
# Create DataFrame
# ------------------------------------------

training_data = pd.DataFrame(
    dataset
)


# ------------------------------------------
# Train AI model
# ------------------------------------------

features = [
    "rms",
    "standard_deviation",
    "peak_to_peak",
    "dominant_frequency",
    "snr_db"
]


X = training_data[features]

y = training_data["quality"]


model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(
    X,
    y
)


# ==========================================
# CREATE NEW TEST SIGNAL
# ==========================================

np.random.seed(100)


time = np.linspace(
    0,
    duration,
    int(
        sampling_frequency * duration
    ),
    endpoint=False
)


clean_signal = (
    amplitude
    * np.sin(
        2
        * np.pi
        * frequency
        * time
    )
)


# Change this value to test signal quality

test_noise_level = 0.18


noise = np.random.normal(
    0,
    test_noise_level,
    len(time)
)


test_signal = (
    clean_signal + noise
)


# ==========================================
# EXTRACT TEST FEATURES
# ==========================================

rms = np.sqrt(
    np.mean(
        test_signal ** 2
    )
)

standard_deviation = np.std(
    test_signal
)

peak_to_peak = (
    np.max(test_signal)
    - np.min(test_signal)
)


# FFT

fft_result = np.fft.fft(
    test_signal
)

frequencies = np.fft.fftfreq(
    len(test_signal),
    1 / sampling_frequency
)

magnitude = (
    np.abs(fft_result)
    / len(test_signal)
)

positive_frequencies = (
    frequencies[:len(test_signal) // 2]
)

positive_magnitude = (
    magnitude[:len(test_signal) // 2]
)

peak_index = np.argmax(
    positive_magnitude
)

dominant_frequency = (
    positive_frequencies[peak_index]
)


# ==========================================
# SNR
# ==========================================

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
        signal_rms / noise_rms
    )
)


# ==========================================
# AI PREDICTION
# ==========================================

test_features = pd.DataFrame(
    [[
        rms,
        standard_deviation,
        peak_to_peak,
        dominant_frequency,
        snr_db
    ]],
    columns=features
)


prediction = model.predict(
    test_features
)[0]


probabilities = (
    model.predict_proba(
        test_features
    )[0]
)


# ==========================================
# QUALITY SCORE
# ==========================================

# SNR-based score.
# 30 dB or higher = 100
# 0 dB or lower = 0

snr_score = np.clip(
    (snr_db / 30) * 100,
    0,
    100
)


# AI confidence

prediction_index = list(
    model.classes_
).index(prediction)


ai_confidence = (
    probabilities[
        prediction_index
    ] * 100
)


# Combine SNR and AI confidence

quality_score = (
    0.7 * snr_score
    + 0.3 * ai_confidence
)


quality_score = round(
    quality_score,
    2
)


# ==========================================
# QUALITY LEVEL
# ==========================================

if quality_score >= 70:

    quality_level = "GOOD"

elif quality_score >= 40:

    quality_level = "MODERATE"

else:

    quality_level = "POOR"


# ==========================================
# DISPLAY RESULTS
# ==========================================

print("=" * 70)

print(
    "          AI SMART OSCILLOSCOPE"
)

print(
    "            SIGNAL QUALITY"
)

print("=" * 70)


print(
    "\nSignal Measurements"
)

print(
    "-" * 70
)

print(
    f"RMS                  : "
    f"{rms:.4f}"
)

print(
    f"Peak-to-Peak         : "
    f"{peak_to_peak:.4f}"
)

print(
    f"Dominant Frequency   : "
    f"{dominant_frequency:.2f} Hz"
)

print(
    f"SNR                  : "
    f"{snr_db:.2f} dB"
)


print(
    "\nAI Analysis"
)

print(
    "-" * 70
)

print(
    f"AI Classification    : "
    f"{prediction}"
)

print(
    f"AI Confidence        : "
    f"{ai_confidence:.2f}%"
)


print(
    "\nFinal Signal Quality"
)

print(
    "-" * 70
)

print(
    f"SNR Score            : "
    f"{snr_score:.2f}/100"
)

print(
    f"Final Quality Score  : "
    f"{quality_score}/100"
)

print(
    f"Quality Level        : "
    f"{quality_level}"
)


# ==========================================
# RECOMMENDATION
# ==========================================

if quality_level == "GOOD":

    recommendation = (
        "Signal quality is good. "
        "No immediate action required."
    )

elif quality_level == "MODERATE":

    recommendation = (
        "Signal contains noticeable noise. "
        "Check the signal source and connections."
    )

else:

    recommendation = (
        "Signal quality is poor. "
        "Investigate noise sources and "
        "measurement conditions."
    )


print(
    "\nRecommendation"
)

print(
    "-" * 70
)

print(
    recommendation
)


# ==========================================
# SAVE RESULT
# ==========================================

result = pd.DataFrame({

    "rms": [rms],

    "peak_to_peak": [
        peak_to_peak
    ],

    "dominant_frequency": [
        dominant_frequency
    ],

    "snr_db": [snr_db],

    "ai_prediction": [
        prediction
    ],

    "ai_confidence": [
        ai_confidence
    ],

    "quality_score": [
        quality_score
    ],

    "quality_level": [
        quality_level
    ],

    "recommendation": [
        recommendation
    ]
})


result.to_csv(
    "signal_quality_result.csv",
    index=False
)


print(
    "\n✅ Signal quality score calculated!"
)

print(
    "✅ Result saved to "
    "signal_quality_result.csv"
)

print(
    "\n🎉 STAGE 08 COMPLETED!"
)
