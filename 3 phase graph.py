
import matplotlib.pyplot as plt
import numpy as np

# Define voltage amplitude, frequency, and phase angles
V_phase = 120  # Line voltage (RMS)
f = 60  # Frequency (Hz)
phi_12 = 0  # Phase angle between phases L1 and L2 (radians)
phi_23 = -2*np.pi/3  # Phase angle between phases L2 and L3 (radians)
phi_31 = 2*np.pi/3  # Phase angle between phases L3 and L1 (radians)

t = np.linspace(0, 1/f, 1000)  # Time samples for one cycle

# Calculate phase voltages
v_L1N = V_phase * np.cos(2*np.pi*f*t)
v_L2N = V_phase * np.cos(2*np.pi*f*t + phi_12)
v_L3N = V_phase * np.cos(2*np.pi*f*t + phi_23)

# Plot the waveforms
plt.figure(figsize=(10, 6))
plt.plot(t, v_L1N, label="L1-N")
plt.plot(t, v_L2N, label="L2-N")
plt.plot(t, v_L3N, label="L3-N")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("Three-Phase Voltages (Line-Neutral)")
plt.grid(True)
plt.legend()

# Calculate line-to-line voltages (optional)
v_L1L2 = V_phase * np.sqrt(3) * np.cos(2*np.pi*f*t + phi_12)
v_L2L3 = V_phase * np.sqrt(3) * np.cos(2*np.pi*f*t + phi_23)
v_L3L1 = V_phase * np.sqrt(3) * np.cos(2*np.pi*f*t + phi_31)

# Plot line-to-line voltages (optional)
plt.figure(figsize=(10, 6))
plt.plot(t, v_L1L2, label="L1-L2")
plt.plot(t, v_L2L3, label="L2-L3")
plt.plot(t, v_L3L1, label="L3-L1")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("Three-Phase Voltages (Line-to-Line)")
plt.grid(True)
plt.legend()

plt.show()