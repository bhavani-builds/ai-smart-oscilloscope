import numpy as np
import matplotlib.pyplot as plt


# ==========================================
# AI SMART OSCILLOSCOPE
# STAGE 04 — FFT FREQUENCY ANALYSIS
# ==========================================


# ------------------------------------------
# Signal parameters
# ------------------------------------------

sampling_frequency = 1000
duration = 1
frequency = 5
amplitude = 1


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
# Generate signal
# ------------------------------------------

signal = (
    amplitude
    * np.sin(
        2 * np.pi * frequency * time
    )
)


# ==========================================
# FFT
# ==========================================

fft_result = np.fft.fft(
    signal
)


# Calculate frequency bins

frequencies = np.fft.fftfreq(
    number_of_samples,
    1 / sampling_frequency
)


# Calculate magnitude

magnitude = (
    np.abs(fft_result)
    / number_of_samples
)


# Keep only positive frequencies

positive_frequencies = (
    frequencies[:number_of_samples // 2]
)

positive_magnitude = (
    magnitude[:number_of_samples // 2]
)


# ==========================================
# FIND DOMINANT FREQUENCY
# ==========================================

peak_index = np.argmax(
    positive_magnitude
)

dominant_frequency = (
    positive_frequencies[
        peak_index
    ]
)


dominant_amplitude = (
    positive_magnitude[
        peak_index
    ]
    * 2
)


# ==========================================
# DISPLAY RESULTS
# ==========================================

print("=" * 65)

print(
    "          AI SMART OSCILLOSCOPE"
)

print(
    "             FFT ANALYSIS"
)

print("=" * 65)


print(
    f"\nSampling Frequency : "
    f"{sampling_frequency} Hz"
)

print(
    f"Signal Frequency   : "
    f"{frequency} Hz"
)

print(
    f"Number of Samples  : "
    f"{number_of_samples}"
)


print("\nFFT Results")
print("-" * 65)

print(
    f"Dominant Frequency : "
    f"{dominant_frequency:.2f} Hz"
)

print(
    f"Dominant Amplitude : "
    f"{dominant_amplitude:.2f}"
)


# ==========================================
# FREQUENCY ERROR
# ==========================================

frequency_error = abs(
    frequency - dominant_frequency
)


print(
    f"Frequency Error    : "
    f"{frequency_error:.2f} Hz"
)


# ==========================================
# CHECK RESULT
# ==========================================

if frequency_error < 0.5:

    print(
        "\n✅ FFT correctly detected "
        "the signal frequency."
    )

else:

    print(
        "\n⚠️ FFT frequency detection "
        "needs review."
    )


# ==========================================
# PLOT FREQUENCY SPECTRUM
# ==========================================

plt.figure(
    figsize=(12, 6)
)


plt.plot(
    positive_frequencies,
    positive_magnitude,
    linewidth=2
)


# Mark dominant frequency

plt.axvline(
    dominant_frequency,
    linestyle="--",
    linewidth=1
)


plt.title(
    "FFT Frequency Spectrum",
    fontsize=18,
    fontweight="bold"
)


plt.xlabel(
    "Frequency (Hz)"
)

plt.ylabel(
    "Magnitude"
)


plt.xlim(
    0,
    50
)


plt.grid(
    True,
    linestyle="--",
    alpha=0.5
)


plt.tight_layout()


# Save FFT graph

plt.savefig(
    "fft_frequency_spectrum.png",
    dpi=300,
    bbox_inches="tight"
)


plt.show()


# ==========================================
# COMPLETION
# ==========================================

print(
    "\n✅ FFT analysis completed!"
)

print(
    "✅ Frequency spectrum saved!"
)

print(
    "\n🎉 STAGE 04 COMPLETED!"
)
