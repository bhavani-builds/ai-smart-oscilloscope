# 📡 AI Smart Oscilloscope & Signal Analyzer

An interactive Python-based virtual oscilloscope that combines **Digital Signal Processing (DSP), FFT analysis, noise analysis, Machine Learning, and interactive visualization** to analyze signal quality.

---

## 🚀 Project Overview

Traditional oscilloscopes display electrical signals in the time domain.

This project extends that concept by adding software-based signal analysis and AI.

The system can:

- Generate test signals.
- Display waveforms.
- Measure signal characteristics.
- Perform FFT frequency analysis.
- Analyze noise.
- Calculate SNR.
- Extract signal features.
- Classify signal quality using Machine Learning.
- Generate a 0–100 signal quality score.
- Provide engineering recommendations.
- Display results through an interactive dashboard.
- Generate an automated engineering report.

---

# 🎯 Project Objective

The objective is to build a **software-based intelligent oscilloscope prototype** that combines ECE signal-processing concepts with Machine Learning.

```text
Signal
   ↓
Waveform Analysis
   ↓
Signal Measurements
   ↓
FFT Analysis
   ↓
Noise Analysis
   ↓
Feature Extraction
   ↓
Machine Learning
   ↓
Signal Quality
   ↓
Engineering Recommendation
```

---

# 🧠 System Architecture

```text
                SIGNAL SOURCE
                     │
                     ▼
              Signal Generator
                     │
                     ▼
              Time-Domain Signal
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
    Measurements              FFT
          │                     │
          │              Frequency Spectrum
          │                     │
          └──────────┬──────────┘
                     ▼
               Noise Analysis
                     │
                     ▼
                   SNR
                     │
                     ▼
             Feature Extraction
                     │
                     ▼
             Machine Learning
                     │
                     ▼
            Signal Classification
                     │
                     ▼
            Quality Score 0–100
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
     Dashboard             Engineering
                              Report
```

---

# ✨ Features

## 🌊 Signal Generation

The project supports generated signals such as:

- Sine wave
- Square wave
- Triangle wave
- Noisy sine wave

---

## 📊 Signal Measurements

The system calculates:

- Maximum value
- Minimum value
- Peak-to-peak value
- Mean
- RMS
- Standard deviation
- Zero crossings
- Estimated frequency

---

## 📡 FFT Analysis

FFT is used to transform the signal from:

```text
Time Domain
     ↓
    FFT
     ↓
Frequency Domain
```

The system identifies the dominant frequency component.

---

## 📢 Noise Analysis

The system compares the clean signal and noisy signal and calculates:

- Signal RMS
- Noise RMS
- Total RMS
- SNR
- Noise percentage

### SNR

```text
SNR = Signal Strength / Noise Strength
```

The result is expressed in decibels.

---

## 🧠 Feature Extraction

Signal-processing measurements are converted into Machine Learning features:

```text
RMS
Standard Deviation
Peak-to-Peak
Dominant Frequency
SNR
```

These features are used by the classification model.

---

# 🤖 AI Signal Classification

A **Random Forest Classifier** is used to classify signal quality.

The model predicts:

| Class | Meaning |
|---|---|
| GOOD | High-quality signal |
| MODERATE | Noticeable noise |
| POOR | High noise / poor quality |

The training dataset used in this prototype is synthetically generated.

---

# 📊 Signal Quality Score

The project produces a simple **0–100 signal quality score**.

```text
70–100 → GOOD
40–69  → MODERATE
0–39   → POOR
```

The score combines SNR-based analysis with the AI classification confidence.

> This is a project-defined metric, not a standardized oscilloscope specification.

---

# 🖥️ Interactive Dashboard

The Streamlit dashboard provides controls for:

- Frequency
- Amplitude
- Noise level
- Sampling frequency

It displays:

- Live waveform
- FFT spectrum
- RMS
- Peak-to-peak
- Dominant frequency
- SNR
- Signal quality
- Quality score
- Engineering recommendation

---

# 🔧 Engineering Recommendation

Based on the signal quality, the system provides recommendations.

Example:

```text
GOOD
↓
No immediate action required.
```

```text
MODERATE
↓
Check signal connections and
measurement conditions.
```

```text
POOR
↓
Inspect the signal source,
connections and measurement setup.
```

---

# 📄 Automated Engineering Report

The project automatically generates:

```text
signal_analysis_report.txt
```

The report contains:

- Signal parameters
- Signal measurements
- FFT analysis
- Noise analysis
- SNR
- Signal quality
- Engineering recommendation

---

# 📂 Project Structure

```text
ai-smart-oscilloscope/
│
├── 01_signal_generator/
│   ├── generate_signal.py
│   ├── sine_wave.png
│   ├── square_wave.png
│   ├── triangle_wave.png
│   └── noisy_sine_wave.png
│
├── 02_oscilloscope_view/
│   ├── oscilloscope_view.py
│   ├── oscilloscope_waveform.png
│   └── oscilloscope_zoomed.png
│
├── 03_signal_measurements/
│   ├── measure_signal.py
│   └── signal_measurements.png
│
├── 04_fft_analysis/
│   ├── fft_analysis.py
│   └── fft_frequency_spectrum.png
│
├── 05_noise_analysis/
│   ├── noise_analysis.py
│   ├── clean_signal.png
│   └── noisy_signal.png
│
├── 06_feature_extraction/
│   ├── extract_features.py
│   └── signal_features.csv
│
├── 07_ai_classification/
│   ├── train_signal_classifier.py
│   ├── ai_signal_training_data.csv
│   └── signal_classifier_confusion_matrix.png
│
├── 08_signal_quality/
│   ├── calculate_quality.py
│   └── signal_quality_result.csv
│
├── 09_dashboard/
│   └── app.py
│
├── 10_automated_report/
│   ├── generate_report.py
│   └── signal_analysis_report.txt
│
└── README.md
```

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core development |
| NumPy | Numerical computation |
| Pandas | Data processing |
| Matplotlib | Signal visualization |
| Scikit-learn | Machine Learning |
| Streamlit | Interactive dashboard |

---

# 📚 ECE / DSP Concepts Used

This project demonstrates practical concepts including:

- Continuous/discrete signal representation
- Sampling
- Time-domain analysis
- Frequency-domain analysis
- FFT
- RMS
- Peak-to-peak measurement
- Noise
- Signal-to-Noise Ratio
- Frequency detection
- Feature extraction
- Signal classification

---

# ⚙️ Installation

Install the required libraries:

```bash
pip install numpy pandas matplotlib scikit-learn streamlit
```

---

# ▶️ Run the Project

Run the modules in order:

```bash
python 01_signal_generator/generate_signal.py
```

```bash
python 02_oscilloscope_view/oscilloscope_view.py
```

```bash
python 03_signal_measurements/measure_signal.py
```

```bash
python 04_fft_analysis/fft_analysis.py
```

```bash
python 05_noise_analysis/noise_analysis.py
```

```bash
python 06_feature_extraction/extract_features.py
```

```bash
python 07_ai_classification/train_signal_classifier.py
```

```bash
python 08_signal_quality/calculate_quality.py
```

---

# 🖥️ Launch Dashboard

Run:

```bash
python -m streamlit run 09_dashboard/app.py
```

The dashboard will open in your browser.

---

# 📄 Generate Engineering Report

Run:

```bash
python 10_automated_report/generate_report.py
```

This creates:

```text
signal_analysis_report.txt
```

---

# 🎯 Applications

The concepts demonstrated by this project can be useful for:

- Signal testing
- Electronics debugging
- Communication systems
- Embedded systems
- DSP applications
- Sensor signal analysis
- Noise monitoring
- Vibration analysis
- Educational laboratories
- Hardware troubleshooting

---

# 🚀 Future Improvements

The project can be extended with:

- Real oscilloscope data import
- CSV waveform loading
- Serial communication
- Arduino integration
- ESP32 integration
- Raspberry Pi integration
- Real-time ADC acquisition
- Digital filters
- Band-pass filtering
- Low-pass filtering
- High-pass filtering
- Spectrogram
- Wavelet analysis
- Automatic anomaly detection
- Deep Learning
- Hardware fault classification
- Cloud monitoring

---

# ⚠️ Limitations

This project is an **educational software prototype**.

The current implementation:

- Uses generated/synthetic signals.
- Does not directly acquire real oscilloscope hardware data.
- Uses project-defined signal-quality thresholds.
- Uses synthetic data for the ML demonstration.
- Should not replace calibrated laboratory instrumentation.

Real engineering deployment would require validation using measured hardware signals and appropriate calibration.

---

# 🎓 Learning Outcomes

Through this project, the following skills are demonstrated:

```text
Python
   +
NumPy
   +
Signal Processing
   +
FFT
   +
Noise Analysis
   +
Machine Learning
   +
Data Visualization
   +
Streamlit
   +
Technical Reporting
```

---

# 🏆 Project Status

| Module | Status |
|---|---|
| Signal Generator | ✅ Complete |
| Oscilloscope Visualization | ✅ Complete |
| Signal Measurements | ✅ Complete |
| FFT Analysis | ✅ Complete |
| Noise Analysis | ✅ Complete |
| Feature Extraction | ✅ Complete |
| AI Classification | ✅ Complete |
| Signal Quality Score | ✅ Complete |
| Interactive Dashboard | ✅ Complete |
| Automated Report | ✅ Complete |
| Documentation | ✅ Complete |

---

# 👨‍💻 Author

Developed as an **ECE + DSP + Machine Learning** portfolio project.

---

# ⭐ Project Summary

**AI Smart Oscilloscope & Signal Analyzer** is an end-to-end signal-analysis prototype combining traditional **ECE/DSP techniques** with modern **Machine Learning and interactive visualization**.

```text
📡 Signal
   ↓
📈 Waveform
   ↓
📊 Measurements
   ↓
📡 FFT
   ↓
📢 Noise Analysis
   ↓
🧠 Feature Extraction
   ↓
🤖 AI Classification
   ↓
🎯 Quality Score
   ↓
🖥️ Dashboard
   ↓
📄 Engineering Report
```

---

## 🚀 Future Vision

The ultimate goal is to evolve this project from a software-generated signal analyzer into a **real-time intelligent oscilloscope** capable of receiving data from ADCs, microcontrollers, or laboratory instruments and automatically identifying abnormal signal behavior.
