import numpy as np
import matplotlib.pyplot as plt


# ==========================================
# AI SMART OSCILLOSCOPE
# STAGE 03 — SIGNAL MEASUREMENTS
# ==========================================


# Signal parameters
sampling_frequency = 1000
duration = 1
frequency = 5
amplitude = 1


# Create time axis
time = np.linspace(
    0,
    duration,
    int(sampling_frequency * duration),
    endpoint=False
)


# Generate sine wave
signal = (
    amplitude
    * np.sin(
        2 * np.pi * frequency * time
    )
)


# ==========================================
# SIGNAL MEASUREMENTS
# ==========================================

maximum = np.max(signal)

minimum = np.min(signal)

peak_to_peak = maximum - minimum

measured_amplitude = peak_to_peak / 2

mean_value = np.mean(signal)

rms_value = np.sqrt(
    np.mean(signal ** 2)
)

standard_deviation = np.std(signal)


# ==========================================
# ZERO CROSSING
# ==========================================

zero_crossings = np.where(
    np.diff(
        np.sign(signal)
    ) != 0
)[0]

zero_crossing_count = len(
    zero_crossings
)


# Estimate frequency
measured_frequency = (
    zero_crossing_count
    / (2 * duration)
)


# ==========================================
# DISPLAY RESULTS
# ==========================================

print("=" * 65)

print(
    "          AI SMART OSCILLOSCOPE"
)

print(
    "             SIGNAL ANALYSIS"
)

print("=" * 65)


print("\nSignal Parameters")
print("-" * 65)

print(
    f"Sampling Frequency : "
    f"{sampling_frequency} Hz"
)

print(
    f"Expected Frequency : "
    f"{frequency} Hz"
)

print(
    f"Expected Amplitude : "
    f"{amplitude}"
)


print("\nMeasured Parameters")
print("-" * 65)

print(
    f"Maximum Value      : "
    f"{maximum:.4f}"
)

print(
    f"Minimum Value      : "
    f"{minimum:.4f}"
)

print(
    f"Peak-to-Peak       : "
    f"{peak_to_peak:.4f}"
)

print(
    f"Measured Amplitude : "
    f"{measured_amplitude:.4f}"
)

print(
    f"Mean Value         : "
    f"{mean_value:.4f}"
)

print(
    f"RMS Value          : "
    f"{rms_value:.4f}"
)

print(
    f"Standard Deviation : "
    f"{standard_deviation:.4f}"
)

print(
    f"Zero Crossings     : "
    f"{zero_crossing_count}"
)

print(
    f"Measured Frequency : "
    f"{measured_frequency:.2f} Hz"
)


# ==========================================
# FREQUENCY ERROR
# ==========================================

frequency_error = abs(
    frequency - measured_frequency
)

print(
    f"\nFrequency Error    : "
    f"{frequency_error:.2f} Hz"
)


# ==========================================
# CHECK RESULT
# ==========================================

if frequency_error < 0.5:

    print(
        "\n✅ Frequency measurement is accurate."
    )

else:

    print(
        "\n⚠️ Frequency measurement needs review."
    )


# ==========================================
# PLOT SIGNAL
# ==========================================

plt.figure(
    figsize=(12, 6)
)

plt.plot(
    time,
    signal,
    linewidth=2
)

plt.axhline(
    0,
    linestyle="--",
    linewidth=1
)

plt.title(
    "AI Smart Oscilloscope - Signal Measurements",
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


# Save graph
plt.savefig(
    "signal_measurements.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


print(
    "\n✅ Signal measurements completed!"
)

print(
    "✅ Measurement graph saved!"
)

print(
    "\n🎉 STAGE 03 COMPLETED!"
)
