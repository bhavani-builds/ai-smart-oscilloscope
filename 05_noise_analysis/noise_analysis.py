import numpy as np
import matplotlib.pyplot as plt


# ==========================================
# AI SMART OSCILLOSCOPE
# STAGE 05 — NOISE ANALYSIS
# ==========================================


# ------------------------------------------
# Signal parameters
# ------------------------------------------

sampling_frequency = 1000
duration = 1
frequency = 5
amplitude = 1

noise_level = 0.25


# ------------------------------------------
# Create time axis
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
        2 * np.pi * frequency * time
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
# Create noisy signal
# ------------------------------------------

noisy_signal = (
    clean_signal + noise
)


# ==========================================
# RMS CALCULATIONS
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


total_rms = np.sqrt(
    np.mean(
        noisy_signal ** 2
    )
)


# ==========================================
# SIGNAL-TO-NOISE RATIO
# ==========================================

snr_db = (
    20
    * np.log10(
        signal_rms / noise_rms
    )
)


# ==========================================
# NOISE PERCENTAGE
# ==========================================

noise_percentage = (
    noise_rms
    / signal_rms
) * 100


# ==========================================
# DISPLAY RESULTS
# ==========================================

print("=" * 65)

print(
    "          AI SMART OSCILLOSCOPE"
)

print(
    "              NOISE ANALYSIS"
)

print("=" * 65)


print("\nSignal Information")
print("-" * 65)

print(
    f"Signal Frequency : "
    f"{frequency} Hz"
)

print(
    f"Signal Amplitude : "
    f"{amplitude}"
)

print(
    f"Noise Level      : "
    f"{noise_level}"
)


print("\nNoise Measurements")
print("-" * 65)

print(
    f"Signal RMS       : "
    f"{signal_rms:.4f}"
)

print(
    f"Noise RMS        : "
    f"{noise_rms:.4f}"
)

print(
    f"Total Signal RMS : "
    f"{total_rms:.4f}"
)

print(
    f"SNR              : "
    f"{snr_db:.2f} dB"
)

print(
    f"Noise Percentage : "
    f"{noise_percentage:.2f}%"
)


# ==========================================
# SIGNAL QUALITY
# ==========================================

if snr_db >= 20:

    quality = "GOOD"

elif snr_db >= 10:

    quality = "MODERATE"

else:

    quality = "POOR"


print(
    f"\nSignal Quality   : "
    f"{quality}"
)


# ==========================================
# PLOT CLEAN SIGNAL
# ==========================================

plt.figure(
    figsize=(12, 5)
)

plt.plot(
    time,
    clean_signal,
    linewidth=2
)

plt.title(
    "Clean Sine Wave",
    fontsize=18,
    fontweight="bold"
)

plt.xlabel(
    "Time (seconds)"
)

plt.ylabel(
    "Amplitude"
)

plt.grid(
    True,
    linestyle="--",
    alpha=0.5
)

plt.tight_layout()

plt.savefig(
    "clean_signal.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==========================================
# PLOT NOISY SIGNAL
# ==========================================

plt.figure(
    figsize=(12, 5)
)

plt.plot(
    time,
    noisy_signal,
    linewidth=1
)

plt.title(
    "Noisy Sine Wave",
    fontsize=18,
    fontweight="bold"
)

plt.xlabel(
    "Time (seconds)"
)

plt.ylabel(
    "Amplitude"
)

plt.grid(
    True,
    linestyle="--",
    alpha=0.5
)

plt.tight_layout()

plt.savefig(
    "noisy_signal.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==========================================
# COMPLETION
# ==========================================

print(
    "\n✅ Noise analysis completed!"
)

print(
    "✅ SNR calculated!"
)

print(
    "✅ Signal quality estimated!"
)

print(
    "\n🎉 STAGE 05 COMPLETED!"
)
