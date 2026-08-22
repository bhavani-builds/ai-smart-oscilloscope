import numpy as np
import matplotlib.pyplot as plt


# ==========================================
# AI SMART OSCILLOSCOPE
# STAGE 02 — OSCILLOSCOPE VIEW
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

time = np.linspace(
    0,
    duration,
    int(sampling_frequency * duration),
    endpoint=False
)


# ------------------------------------------
# Generate sine signal
# ------------------------------------------

signal = (
    amplitude
    * np.sin(
        2 * np.pi * frequency * time
    )
)


# ==========================================
# SIGNAL INFORMATION
# ==========================================

print("=" * 60)
print("           AI SMART OSCILLOSCOPE")
print("              OSCILLOSCOPE VIEW")
print("=" * 60)

print(
    f"\nSampling Frequency : "
    f"{sampling_frequency} Hz"
)

print(
    f"Signal Frequency   : "
    f"{frequency} Hz"
)

print(
    f"Amplitude          : "
    f"{amplitude}"
)

print(
    f"Number of Samples  : "
    f"{len(signal)}"
)


# ==========================================
# BASIC MEASUREMENTS
# ==========================================

maximum = np.max(signal)

minimum = np.min(signal)

peak_to_peak = (
    maximum - minimum
)

rms = np.sqrt(
    np.mean(signal ** 2)
)


print("\nSignal Measurements")
print("-" * 60)

print(
    f"Maximum Amplitude : "
    f"{maximum:.3f}"
)

print(
    f"Minimum Amplitude : "
    f"{minimum:.3f}"
)

print(
    f"Peak-to-Peak      : "
    f"{peak_to_peak:.3f}"
)

print(
    f"RMS Value         : "
    f"{rms:.3f}"
)


# ==========================================
# OSCILLOSCOPE DISPLAY
# ==========================================

plt.figure(
    figsize=(12, 6)
)


plt.plot(
    time,
    signal,
    linewidth=2
)


# Center horizontal axis

plt.axhline(
    0,
    linestyle="--",
    linewidth=1
)


plt.title(
    "AI Smart Oscilloscope — Waveform",
    fontsize=18,
    fontweight="bold"
)


plt.xlabel(
    "Time (seconds)"
)


plt.ylabel(
    "Amplitude"
)


plt.xlim(
    0,
    1
)


plt.ylim(
    -1.2,
    1.2
)


plt.grid(
    True,
    linestyle="--",
    alpha=0.5
)


plt.tight_layout()


# ------------------------------------------
# Save oscilloscope image
# ------------------------------------------

plt.savefig(
    "oscilloscope_waveform.png",
    dpi=300,
    bbox_inches="tight"
)


plt.show()


# ==========================================
# ZOOMED VIEW
# ==========================================

plt.figure(
    figsize=(12, 6)
)


plt.plot(
    time,
    signal,
    linewidth=2
)


plt.title(
    "Oscilloscope — Zoomed View",
    fontsize=18,
    fontweight="bold"
)


plt.xlabel(
    "Time (seconds)"
)


plt.ylabel(
    "Amplitude"
)


# Display first 0.4 seconds

plt.xlim(
    0,
    0.4
)


plt.grid(
    True,
    linestyle="--",
    alpha=0.5
)


plt.tight_layout()


plt.savefig(
    "oscilloscope_zoomed.png",
    dpi=300,
    bbox_inches="tight"
)


plt.show()


# ==========================================
# COMPLETION
# ==========================================

print(
    "\n✅ Oscilloscope waveform created!"
)

print(
    "✅ Measurements calculated!"
)

print(
    "✅ Zoomed waveform created!"
)

print(
    "\n🎉 STAGE 02 COMPLETED!"
)
