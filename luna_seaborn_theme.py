import seaborn as sns

# Define a global sizes
font_size = 9
linewidth = 0.5

# Define reusable theme
custom_theme = {
    'font.size': font_size,
    'axes.titlesize': font_size,
    'axes.labelsize': font_size,
    'legend.fontsize': font_size,
    'legend.edgecolor': 'black',
    'legend.frameon': False,
    'lines.linewidth': linewidth,
    'font.family': 'Arial',
    "svg.fonttype": 'none',
    "pdf.fonttype": 'truetype',
    'axes.spines.top': True,
    'axes.spines.right': True,
    'axes.spines.left': True,
    'axes.spines.bottom': True,
    'axes.linewidth': linewidth,
    'xtick.major.width': linewidth,
    'ytick.major.width': linewidth,
    'xtick.labelsize': font_size,
    'ytick.labelsize': font_size
}


def apply_luna_theme():
    sns.set_theme(style="ticks", rc=custom_theme)
