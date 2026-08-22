import numpy as np
import matplotlib.pyplot as plt


# ==========================================
# AI SMART OSCILLOSCOPE
# STAGE 01 — SIGNAL GENERATOR
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
    sampling_frequency * duration,
    endpoint=False
)


# ------------------------------------------
# Generate sine wave
# ------------------------------------------

sine_signal = (
    amplitude
    * np.sin(
        2 * np.pi * frequency * time
    )
)


# ------------------------------------------
# Generate square wave
# ------------------------------------------

square_signal = np.sign(
    np.sin(
        2 * np.pi * frequency * time
    )
)


# ------------------------------------------
# Generate triangle wave
# ------------------------------------------

triangle_signal = (
    2 * np.abs(
        2 * (
            frequency * time
            - np.floor(
                frequency * time + 0.5
            )
        )
    ) - 1
)


# ------------------------------------------
# Generate noisy sine wave
# ------------------------------------------

noise = np.random.normal(
    0,
    0.25,
    len(time)
)


noisy_signal = (
    sine_signal + noise
)


# ==========================================
# DISPLAY INFORMATION
# ==========================================

print("=" * 60)

print(
    "        AI SMART OSCILLOSCOPE"
)

print(
    "             SIGNAL GENERATOR"
)

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
    f"Duration           : "
    f"{duration} second"
)

print(
    f"Number of Samples  : "
    f"{len(time)}"
)


# ==========================================
# PLOT SINE WAVE
# ==========================================

plt.figure(
    figsize=(10, 5)
)

plt.plot(
    time,
    sine_signal
)

plt.title(
    "Sine Wave"
)

plt.xlabel(
    "Time (seconds)"
)

plt.ylabel(
    "Amplitude"
)

plt.grid(
    True
)

plt.tight_layout()

plt.savefig(
    "sine_wave.png",
    dpi=300
)

plt.show()


# ==========================================
# PLOT SQUARE WAVE
# ==========================================

plt.figure(
    figsize=(10, 5)
)

plt.plot(
    time,
    square_signal
)

plt.title(
    "Square Wave"
)

plt.xlabel(
    "Time (seconds)"
)

plt.ylabel(
    "Amplitude"
)

plt.grid(
    True
)

plt.tight_layout()

plt.savefig(
    "square_wave.png",
    dpi=300
)

plt.show()


# ==========================================
# PLOT TRIANGLE WAVE
# ==========================================

plt.figure(
    figsize=(10, 5)
)

plt.plot(
    time,
    triangle_signal
)

plt.title(
    "Triangle Wave"
)

plt.xlabel(
    "Time (seconds)"
)

plt.ylabel(
    "Amplitude"
)

plt.grid(
    True
)

plt.tight_layout()

plt.savefig(
    "triangle_wave.png",
    dpi=300
)

plt.show()


# ==========================================
# PLOT NOISY SIGNAL
# ==========================================

plt.figure(
    figsize=(10, 5)
)

plt.plot(
    time,
    noisy_signal
)

plt.title(
    "Noisy Sine Wave"
)

plt.xlabel(
    "Time (seconds)"
)

plt.ylabel(
    "Amplitude"
)

plt.grid(
    True
)

plt.tight_layout()

plt.savefig(
    "noisy_sine_wave.png",
    dpi=300
)

plt.show()


# ==========================================
# COMPLETION
# ==========================================

print(
    "\n✅ Signals generated successfully!"
)

print(
    "✅ Waveform images saved!"
)

print(
    "\n🎉 STAGE 01 COMPLETED!"
)
