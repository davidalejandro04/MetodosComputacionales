"""
Fourier Analysis of Audio Signals
===================================
Reads two musical note recordings (Do / C4 and Sol / G4) from WAV files,
analyses their frequency content using the Fast Fourier Transform (FFT),
and applies basic signal processing filters.

Pipeline:
  1. Load WAV files and display waveforms.
  2. Compute FFT spectrum of the Do note.
  3. Compute FFT spectrum of the Sol note.
  4. Apply a low-pass filter  (keep f < 1000 Hz).
  5. Apply a peak filter      (suppress dominant frequency ± 60 bins).
  6. Reconstruct and write a pitch-shifted version (Do_shifted.wav).

All plots saved to outputs/fourier_audio_analysis.png.
Requires: Do.wav and Sol.wav in the same directory.
"""

import numpy as np
import scipy.io.wavfile as wavfile
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

SCRIPT_DIR = os.path.dirname(__file__)

# ── 1. Load WAV files ────────────────────────────────────────────────────────
rate_do,  data_do  = wavfile.read(os.path.join(SCRIPT_DIR, "Do.wav"))
rate_sol, data_sol = wavfile.read(os.path.join(SCRIPT_DIR, "Sol.wav"))

# Handle stereo → mono by taking first channel
if data_do.ndim > 1:
    data_do = data_do[:, 0]
if data_sol.ndim > 1:
    data_sol = data_sol[:, 0]

print(f"Do.wav  - sample rate: {rate_do} Hz,  samples: {len(data_do)}")
print(f"Sol.wav - sample rate: {rate_sol} Hz,  samples: {len(data_sol)}")

# ── 2. Compute FFT & frequency axes ─────────────────────────────────────────
timestep = 1.0 / rate_do

fft_do  = np.fft.fft(data_do.astype(float))
fft_sol = np.fft.fft(data_sol.astype(float))
freq_do  = np.fft.fftfreq(len(data_do),  d=timestep)
freq_sol = np.fft.fftfreq(len(data_sol), d=timestep)

# Frequency axis scaled for Sol (ratio Sol/Do ≈ 391/261)
# G4 ≈ 391 Hz,  C4 ≈ 261 Hz
PITCH_RATIO = 391 / 261
freq_do_shifted = np.fft.fftfreq(len(data_do), d=timestep * PITCH_RATIO)

# ── 3. Filters ───────────────────────────────────────────────────────────────
CUTOFF_HZ = 1000   # low-pass cut-off
PEAK_BINS  = 60    # half-width of the notch around the dominant peak

def low_pass_filter(spectrum: np.ndarray, freqs: np.ndarray, cutoff: float) -> np.ndarray:
    """Zero-out all frequency components above `cutoff` Hz."""
    filtered = spectrum.copy()
    filtered[np.abs(freqs) > cutoff] = 0
    return filtered


def suppress_peak(spectrum: np.ndarray) -> np.ndarray:
    """Find the dominant frequency bin and zero out a ±PEAK_BINS neighbourhood."""
    filtered = spectrum.copy()
    imax = int(np.argmax(np.abs(filtered)))
    lo, hi = max(0, imax - PEAK_BINS), min(len(filtered), imax + PEAK_BINS)
    filtered[lo:hi] = 0
    # Mirror (negative-frequency side)
    mirror = len(filtered) - imax
    lo2, hi2 = max(0, mirror - PEAK_BINS), min(len(filtered), mirror + PEAK_BINS)
    filtered[lo2:hi2] = 0
    return filtered


fft_lowpass  = low_pass_filter(fft_do, freq_do, CUTOFF_HZ)
fft_nopeak   = suppress_peak(fft_do)

# ── 4. Multi-panel spectrum plot ─────────────────────────────────────────────
fig, axes = plt.subplots(5, 1, figsize=(11, 14), sharex=False)
fig.suptitle("Fourier Analysis of Musical Notes (Do & Sol)", fontsize=13)

XLIM = (0, 8000)

axes[0].plot(freq_do,         np.abs(fft_do),        color='seagreen', lw=0.8)
axes[0].set_title("Do (C4) — Raw Spectrum");  axes[0].set_xlim(XLIM)

axes[1].plot(freq_sol,        np.abs(fft_sol),       color='royalblue', lw=0.8)
axes[1].set_title("Sol (G4) — Raw Spectrum"); axes[1].set_xlim(XLIM)

axes[2].plot(freq_do_shifted, np.abs(fft_do),        color='mediumpurple', lw=0.8)
axes[2].set_title("Do — Frequency Axis Scaled to Sol (pitch shift)"); axes[2].set_xlim(XLIM)

axes[3].plot(freq_do,         np.abs(fft_lowpass),   color='darkorange', lw=0.8)
axes[3].set_title(f"Do — Low-Pass Filter (cutoff = {CUTOFF_HZ} Hz)"); axes[3].set_xlim(XLIM)

axes[4].plot(freq_do,         np.abs(fft_nopeak),    color='crimson', lw=0.8)
axes[4].set_title("Do — Peak Suppression Filter"); axes[4].set_xlim(XLIM)

for ax in axes:
    ax.set_ylabel("|FFT|"); ax.grid(True, alpha=0.3)
axes[-1].set_xlabel("Frequency [Hz]")

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "fourier_audio_analysis.png"), dpi=150)
print("Saved outputs/fourier_audio_analysis.png")
plt.close()

# ── 5. Write pitch-shifted WAV ───────────────────────────────────────────────
# Reconstruct time-domain signal from the unmodified FFT, but play it back
# at a higher sample rate so the perceived pitch rises proportionally.
reconstructed = np.fft.ifft(fft_do).real.astype(np.int16)
shifted_rate  = int(rate_do * PITCH_RATIO)
output_wav    = os.path.join(SCRIPT_DIR, "Do_shifted.wav")
wavfile.write(output_wav, shifted_rate, reconstructed)
print(f"Written pitch-shifted audio: {output_wav}")
print(f"  Original rate: {rate_do} Hz -> Shifted rate: {shifted_rate} Hz")
