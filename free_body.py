import matplotlib
matplotlib.use('TkAgg')  # Use the TkAgg backend

import matplotlib.pyplot as plt

# Set the font to Arial
plt.rcParams['font.family'] = 'Arial'

# Create a figure and an axis
fig, ax = plt.subplots(figsize=(8, 6))

# Add the mass
ax.text(0.5, 0.5, 'Mass (m)', ha='center', va='center', fontsize=12, bbox=dict(facecolor='red', alpha=0.5))

# Add the spring to the left of the mass
ax.annotate('',
            xy=(0.2, 0.5), xycoords='axes fraction',
            xytext=(0.45, 0.5), textcoords='axes fraction',
            arrowprops=dict(arrowstyle='<->', lw=1.5))
ax.text(0.28, 0.5, 'Spring (k)', ha='center', va='center', fontsize=12)

# Add the damper above the mass
ax.annotate('',
            xy=(0.5, 0.8), xycoords='axes fraction',
            xytext=(0.5, 0.55), textcoords='axes fraction',
            arrowprops=dict(arrowstyle='<->', lw=1.5))
ax.text(0.5, 0.7, 'Damper (c)', ha='center', va='center', fontsize=12)

# Add forces on the mass
# Spring force opposite to the displacement
ax.annotate('',
            xy=(0.35, 0.5), xycoords='axes fraction',
            xytext=(0.35, 0.35), textcoords='axes fraction',
            arrowprops=dict(arrowstyle='->', lw=1.5, color='blue'))
ax.text(0.42, 0.35, 'Spring Force', ha='center', va='center', fontsize=12, color='blue')

# Damping force opposite to the velocity
ax.annotate('',
            xy=(0.5, 0.45), xycoords='axes fraction',
            xytext=(0.5, 0.35), textcoords='axes fraction',
            arrowprops=dict(arrowstyle='->', lw=1.5, color='green'))
ax.text(0.57, 0.35, 'Damping Force', ha='center', va='center', fontsize=12, color='green')

# Add the ground for reference
ax.plot([0.1, 0.9], [0.2, 0.2], color='black', lw=2)
ax.text(0.5, 0.15, 'Ground', ha='center', va='center', fontsize=12)

plt.show()
