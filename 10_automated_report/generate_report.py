import numpy as np
from datetime import datetime


# ==========================================
# AI SMART OSCILLOSCOPE
# STAGE 10 — AUTOMATED ENGINEERING REPORT
# ==========================================


# ------------------------------------------
# Signal parameters
# ------------------------------------------

sampling_frequency = 1000
duration = 1
frequency = 5
amplitude = 1
noise_level = 0.18


# ------------------------------------------
# Generate time axis
# ------------------------------------------

number_of_samples = int(
    sampling_frequency * duration
)

time = np.linspace(
    0,
    duration,
    number_of_samples,
    endpoint=False
)


# ------------------------------------------
# Generate clean signal
# ------------------------------------------

clean_signal = (
    amplitude
    * np.sin(
        2
        * np.pi
        * frequency
        * time
    )
)


# ------------------------------------------
# Generate noise
# ------------------------------------------

np.random.seed(42)

noise = np.random.normal(
    0,
    noise_level,
    number_of_samples
)


# ------------------------------------------
# Generate final signal
# ------------------------------------------

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

mean_value = np.mean(signal)

rms_value = np.sqrt(
    np.mean(signal ** 2)
)

standard_deviation = np.std(
    signal
)


# ==========================================
# FFT ANALYSIS
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
# NOISE ANALYSIS
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
        signal_rms
        / noise_rms
    )
)


noise_percentage = (
    noise_rms
    / signal_rms
) * 100


# ==========================================
# SIGNAL QUALITY
# ==========================================

if snr_db >= 20:

    quality = "GOOD"

    recommendation = (
        "Signal quality is good. "
        "No immediate action is required."
    )

elif snr_db >= 10:

    quality = "MODERATE"

    recommendation = (
        "Noticeable noise is present. "
        "Check signal connections and "
        "measurement conditions."
    )

else:

    quality = "POOR"

    recommendation = (
        "High noise level detected. "
        "Inspect the signal source, "
        "connections and measurement setup."
    )


# ==========================================
# GENERATE REPORT
# ==========================================

output_file = (
    "signal_analysis_report.txt"
)


with open(
    output_file,
    "w",
    encoding="utf-8"
) as report:

    report.write(
        "=" * 70 + "\n"
    )

    report.write(
        "             AI SMART OSCILLOSCOPE\n"
    )

    report.write(
        "              ENGINEERING REPORT\n"
    )

    report.write(
        "=" * 70 + "\n\n"
    )


    # --------------------------------------
    # Report information
    # --------------------------------------

    report.write(
        "REPORT INFORMATION\n"
    )

    report.write(
        "-" * 70 + "\n"
    )

    report.write(
        "Generated: "
        + datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        + "\n"
    )

    report.write(
        "System: AI Smart Oscilloscope\n\n"
    )


    # --------------------------------------
    # Signal parameters
    # --------------------------------------

    report.write(
        "SIGNAL PARAMETERS\n"
    )

    report.write(
        "-" * 70 + "\n"
    )

    report.write(
        f"Sampling Frequency : "
        f"{sampling_frequency} Hz\n"
    )

    report.write(
        f"Signal Frequency   : "
        f"{frequency} Hz\n"
    )

    report.write(
        f"Amplitude          : "
        f"{amplitude}\n"
    )

    report.write(
        f"Duration           : "
        f"{duration} second\n"
    )

    report.write(
        f"Noise Level        : "
        f"{noise_level}\n"
    )

    report.write(
        f"Number of Samples  : "
        f"{number_of_samples}\n\n"
    )


    # --------------------------------------
    # Measurements
    # --------------------------------------

    report.write(
        "SIGNAL MEASUREMENTS\n"
    )

    report.write(
        "-" * 70 + "\n"
    )

    report.write(
        f"Maximum            : "
        f"{maximum:.4f}\n"
    )

    report.write(
        f"Minimum            : "
        f"{minimum:.4f}\n"
    )

    report.write(
        f"Peak-to-Peak       : "
        f"{peak_to_peak:.4f}\n"
    )

    report.write(
        f"Mean               : "
        f"{mean_value:.4f}\n"
    )

    report.write(
        f"RMS                : "
        f"{rms_value:.4f}\n"
    )

    report.write(
        f"Standard Deviation : "
        f"{standard_deviation:.4f}\n\n"
    )


    # --------------------------------------
    # FFT
    # --------------------------------------

    report.write(
        "FFT ANALYSIS\n"
    )

    report.write(
        "-" * 70 + "\n"
    )

    report.write(
        f"Expected Frequency : "
        f"{frequency:.2f} Hz\n"
    )

    report.write(
        f"Detected Frequency : "
        f"{dominant_frequency:.2f} Hz\n"
    )

    report.write(
        f"Frequency Error    : "
        f"{abs(frequency - dominant_frequency):.2f} Hz\n\n"
    )


    # --------------------------------------
    # Noise analysis
    # --------------------------------------

    report.write(
        "NOISE ANALYSIS\n"
    )

    report.write(
        "-" * 70 + "\n"
    )

    report.write(
        f"Signal RMS         : "
        f"{signal_rms:.4f}\n"
    )

    report.write(
        f"Noise RMS          : "
        f"{noise_rms:.4f}\n"
    )

    report.write(
        f"SNR                : "
        f"{snr_db:.2f} dB\n"
    )

    report.write(
        f"Noise Percentage   : "
        f"{noise_percentage:.2f}%\n\n"
    )


    # --------------------------------------
    # Quality
    # --------------------------------------

    report.write(
        "SIGNAL QUALITY\n"
    )

    report.write(
        "-" * 70 + "\n"
    )

    report.write(
        f"Quality Level      : "
        f"{quality}\n\n"
    )


    # --------------------------------------
    # Recommendation
    # --------------------------------------

    report.write(
        "ENGINEERING RECOMMENDATION\n"
    )

    report.write(
        "-" * 70 + "\n"
    )

    report.write(
        recommendation + "\n\n"
    )


    # --------------------------------------
    # Disclaimer
    # --------------------------------------

    report.write(
        "NOTE\n"
    )

    report.write(
        "-" * 70 + "\n"
    )

    report.write(
        "This project is an educational signal-analysis "
        "prototype. Measurements depend on the generated "
        "or supplied signal and should be validated with "
        "real instrumentation before engineering decisions."
    )


# ==========================================
# CONSOLE OUTPUT
# ==========================================

print("=" * 70)

print(
    "      AI SMART OSCILLOSCOPE REPORT"
)

print("=" * 70)

print(
    f"\nDetected Frequency : "
    f"{dominant_frequency:.2f} Hz"
)

print(
    f"SNR                : "
    f"{snr_db:.2f} dB"
)

print(
    f"Signal Quality     : "
    f"{quality}"
)

print(
    "\nRecommendation:"
)

print(
    recommendation
)

print(
    "\n✅ Engineering report generated!"
)

print(
    f"✅ Saved as: {output_file}"
)

print(
    "\n🎉 STAGE 10 COMPLETED!"
)
