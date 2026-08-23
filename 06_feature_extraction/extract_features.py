import numpy as np
import pandas as pd


# ==========================================
# AI SMART OSCILLOSCOPE
# STAGE 06 — FEATURE EXTRACTION
# ==========================================


# ------------------------------------------
# Signal parameters
# ------------------------------------------

sampling_frequency = 1000
duration = 1
frequency = 5
amplitude = 1

noise_levels = [
    0.05,
    0.10,
    0.20,
    0.30,
    0.40,
    0.50
]


# ------------------------------------------
# Create feature list
# ------------------------------------------

feature_data = []


# ==========================================
# PROCESS DIFFERENT SIGNAL CONDITIONS
# ==========================================

for noise_level in noise_levels:

    number_of_samples = int(
        sampling_frequency * duration
    )

    time = np.linspace(
        0,
        duration,
        number_of_samples,
        endpoint=False
    )


    # Generate clean signal

    clean_signal = (
        amplitude
        * np.sin(
            2 * np.pi * frequency * time
        )
    )


    # Generate noise

    np.random.seed(42)

    noise = np.random.normal(
        0,
        noise_level,
        number_of_samples
    )


    # Create noisy signal

    signal = (
        clean_signal + noise
    )


    # ======================================
    # TIME-DOMAIN FEATURES
    # ======================================

    maximum = np.max(signal)

    minimum = np.min(signal)

    peak_to_peak = (
        maximum - minimum
    )

    mean_value = np.mean(signal)

    rms_value = np.sqrt(
        np.mean(signal ** 2)
    )

    standard_deviation = np.std(
        signal
    )


    # ======================================
    # ZERO CROSSINGS
    # ======================================

    zero_crossings = np.where(
        np.diff(
            np.sign(signal)
        ) != 0
    )[0]


    zero_crossing_count = len(
        zero_crossings
    )


    # ======================================
    # FREQUENCY FEATURE
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
    # NOISE / SNR FEATURES
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
            signal_rms / noise_rms
        )
    )


    noise_percentage = (
        noise_rms
        / signal_rms
    ) * 100


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

    feature_data.append({

        "frequency": frequency,

        "amplitude": amplitude,

        "noise_level": noise_level,

        "maximum": maximum,

        "minimum": minimum,

        "peak_to_peak": peak_to_peak,

        "mean": mean_value,

        "rms": rms_value,

        "standard_deviation":
            standard_deviation,

        "zero_crossings":
            zero_crossing_count,

        "dominant_frequency":
            dominant_frequency,

        "snr_db":
            snr_db,

        "noise_percentage":
            noise_percentage,

        "signal_quality":
            quality
    })


# ==========================================
# CREATE DATAFRAME
# ==========================================

df = pd.DataFrame(
    feature_data
)


# ==========================================
# DISPLAY DATA
# ==========================================

print("=" * 70)

print(
    "          AI SMART OSCILLOSCOPE"
)

print(
    "             FEATURE EXTRACTION"
)

print("=" * 70)


print(
    "\nExtracted Signal Features"
)

print(
    "-" * 70
)


print(
    df.to_string(
        index=False
    )
)


# ==========================================
# FEATURE SUMMARY
# ==========================================

print(
    "\nFeature Statistics"
)

print(
    "-" * 70
)


print(
    df.describe(
        numeric_only=True
    ).round(3)
)


# ==========================================
# QUALITY SUMMARY
# ==========================================

print(
    "\nSignal Quality Distribution"
)

print(
    "-" * 70
)

print(
    df["signal_quality"]
    .value_counts()
)


# ==========================================
# SAVE DATASET
# ==========================================

df.to_csv(
    "signal_features.csv",
    index=False
)


print(
    "\n✅ Signal features extracted!"
)

print(
    "✅ Feature dataset created!"
)

print(
    "\nFile: signal_features.csv"
)

print(
    "\n🎉 STAGE 06 COMPLETED!"
)
