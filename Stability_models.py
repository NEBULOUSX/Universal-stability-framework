"""
Theory of Universal Stability: Non-Equilibrium State Visualizations
Author: Ashmith Dev Vijayaraju
Description: Computational models demonstrating Case 1 (Static, S = 0) 
             and Case 2 (Dynamic, S ~ 0) system trajectories.
"""

import numpy as np
import matplotlib.pyplot as plt

# Initialize time domain for temporal evolution profiles
t = np.linspace(0, 10, 500)
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 5))

# =============================================================================
# SYSTEM 1: Simple Pendulum (Case 1: Static Outcome, S = 0)
# =============================================================================
# Simulates exponential mechanical energy dissipation via ambient friction
theta = np.exp(-0.4 * t) * np.cos(2 * np.pi * 0.5 * t)
omega = np.exp(-0.4 * t) * np.sin(2 * np.pi * 0.5 * t)
S_pendulum = theta**2 + omega**2

ax1.plot(t, S_pendulum, color='crimson', linewidth=2.5, label=r'$S(t)$ Evolution')
ax1.axhline(0, color='black', linestyle='--', alpha=0.5)
ax1.set_title("1. Dissipative Pendulum\n[Case 1: Static (S = 0)]", fontsize=12, fontweight='bold')
ax1.set_xlabel("Time ($t$)")
ax1.set_ylabel("Stability Factor ($S$)")
ax1.grid(True, alpha=0.3)
ax1.legend()

# =============================================================================
# SYSTEM 2: Planetary Orbit (Case 2: Dynamic Outcome, S ~ 0)
# =============================================================================
# Models a stable bound orbit, demonstrating S remaining tightly minimized near 0
r_normalized = 0.15 + 0.02 * np.cos(2 * np.pi * 0.8 * t) 
vr_normalized = 0.02 * np.sin(2 * np.pi * 0.8 * t)
S_orbit = r_normalized**2 + vr_normalized**2

ax2.plot(t, S_orbit, color='royalblue', linewidth=2.5, label=r'$S(t)$ Bound Trajectory')
ax2.set_ylim(-0.05, 0.5)
ax2.set_title("2. Planetary Orbit\n[Case 2: Dynamic (S ~ 0)]", fontsize=12, fontweight='bold')
ax2.set_xlabel("Time ($t$)")
ax2.set_ylabel("Stability Factor ($S$)")
ax2.grid(True, alpha=0.3)
ax2.legend()

# =============================================================================
# SYSTEM 3: Hydrogen Electron (Case 2: Dynamic Outcome, S ~ 0)
# =============================================================================
# Models zero-point boundary constraints preventing absolute structural collapse
r_quantum = 0.2 + 0.01 * np.random.normal(0, 0.3, size=len(t)) 
p_quantum = 0.2 + 0.01 * np.random.normal(0, 0.3, size=len(t))
S_atom = r_quantum**2 + p_quantum**2

ax3.plot(t, S_atom, color='darkgreen', linewidth=1.5, alpha=0.8, label=r'$S(t)$ Ground Floor')
ax3.set_ylim(-0.05, 0.5)
ax3.set_title("3. Hydrogen Atom Electron\n[Case 2: Dynamic (S ~ 0)]", fontsize=12, fontweight='bold')
ax3.set_xlabel("Time ($t$)")
ax3.set_ylabel("Stability Factor ($S$)")
ax3.grid(True, alpha=0.3)
ax3.legend()

# Export configuration for LaTeX integration
plt.tight_layout()
plt.savefig('universal_stability_cases.pdf', dpi=300)
plt.show()
