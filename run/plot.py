from matplotlib import rc
from pylab import *
from numpy import *
from matplotlib.font_manager import FontProperties

# Formatter for ticks
majorFormatter = FormatStrFormatter('%.1f')

# Set visual styles
rc('axes', linewidth=1.5)
rc('lines', mew=1.5)
rc(('xtick.major', 'xtick.minor', 'ytick.major', 'ytick.minor'), pad=5)

# Load the data
data = np.loadtxt("monomer_DP.txt")

# Create the plot
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(data[::, 0], data[:, 1], 'm-o', color='limegreen', markevery=8, mew=1.5, ms=4, mec='limegreen', label = r'Particle Density',lw=1.5, ls='solid')

# Set labels and styles
ax.set_xlabel("Radius (nm)", fontsize=12)
ax.set_ylabel(r" $\psi(r)$", fontsize=12)
ax.set_title("Radial Density Profile", fontsize=14)

ax.legend()

# Tick formatting
ax.xaxis.set_major_formatter(majorFormatter)
ax.xaxis.set_tick_params(labelsize=12)
ax.yaxis.set_tick_params(labelsize=12)

# Layout and save
fig.tight_layout()
fig.savefig("monomer_density_profile.png", dpi=300)
plt.show()
