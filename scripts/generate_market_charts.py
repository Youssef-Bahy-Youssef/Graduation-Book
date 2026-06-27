import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.style.use('seaborn-v0_8-whitegrid')

PALETTE = {
    'blue': '#2E86AB', 'purple': '#A23B72', 'orange': '#F18F01',
    'green': '#43AA8B', 'teal': '#577590', 'red': '#D62828',
    'dark': '#333333', 'gray': '#888888', 'light_gray': '#CCCCCC',
}

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 11,
    'axes.facecolor': '#FAFAFA',
    'figure.facecolor': 'white',
    'axes.edgecolor': PALETTE['light_gray'],
    'axes.grid': True,
    'grid.alpha': 0.3,
    'grid.color': '#999999',
})

OUT = '/Users/youssefbahy/Documents/Training/NexaLearnFullProject/newbook/images'
DPI = 300

# ============================================================
# Chart 1: Global E-Learning Market by Segment (2025)
# Uses representative public market data
# ============================================================
segments = [
    'Corporate\ne-Learning',
    'Academic\nK-12',
    'Higher\nEducation',
    'Professional\nCertifications',
    'Language\nLearning',
    'STEM &\nCoding',
]
market_sizes = [38.0, 12.5, 24.0, 8.5, 6.0, 11.0]
colors = [PALETTE['blue'], PALETTE['teal'], PALETTE['green'],
          PALETTE['orange'], PALETTE['purple'], PALETTE['red']]

fig, ax = plt.subplots(figsize=(9, 5.5))
bars = ax.barh(segments, market_sizes, color=colors, edgecolor='white', linewidth=1.2, height=0.65)

for bar, val in zip(bars, market_sizes):
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
            f'${val}B', ha='left', va='center', fontsize=10, fontweight='bold', color=PALETTE['dark'])

ax.set_xlim(0, 50)
ax.set_xlabel('Market Size (USD Billion)', fontsize=13, fontweight='bold')
ax.set_title('Figure 2.4 — Global E-Learning Market by Segment (2025)', fontsize=14, fontweight='bold', pad=12)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(axis='y', labelsize=10)

plt.tight_layout()
fig.savefig(f'{OUT}/market_segments.png', dpi=DPI, bbox_inches='tight')
fig.savefig(f'{OUT}/market_segments.pdf', bbox_inches='tight')
plt.close()
print('market_segments.png/pdf')

# ============================================================
# Chart 2: Revenue Projection — Year 1 to Year 3
# Uses data from business case (section 2.3)
# ============================================================
years = ['Year 1', 'Year 2', 'Year 3']
revenue = [250000, 440000, 616000]
expenses = [170000, 210000, 260000]
profit = [r - e for r, e in zip(revenue, expenses)]

x = np.arange(len(years))
w = 0.25

fig, ax = plt.subplots(figsize=(8, 5.5))

bars1 = ax.bar(x - w, revenue, w, label='Revenue', color=PALETTE['blue'], alpha=0.85, edgecolor='white')
bars2 = ax.bar(x, expenses, w, label='Expenses', color=PALETTE['orange'], alpha=0.85, edgecolor='white')
bars3 = ax.bar(x + w, profit, w, label='Net Profit', color=PALETTE['green'], alpha=0.85, edgecolor='white')

def add_labels(bars):
    for bar in bars:
        val = bar.get_height()
        label = f'${val:,.0f}'
        if val >= 0:
            ax.text(bar.get_x() + bar.get_width()/2, val + 5000, label,
                    ha='center', va='bottom', fontsize=8.5, fontweight='bold', color=PALETTE['dark'])
        else:
            ax.text(bar.get_x() + bar.get_width()/2, val - 5000, label,
                    ha='center', va='top', fontsize=8.5, fontweight='bold', color=PALETTE['red'])

add_labels(bars1)
add_labels(bars2)
add_labels(bars3)

ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=11, fontweight='bold')
ax.set_ylabel('USD', fontsize=13, fontweight='bold')
ax.set_title('Figure 2.5 — Revenue Projection: Years 1–3', fontsize=14, fontweight='bold', pad=12)
ax.legend(fontsize=10, loc='upper left')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'${v/1000:.0f}K'))

plt.tight_layout()
fig.savefig(f'{OUT}/revenue_projection.png', dpi=DPI, bbox_inches='tight')
fig.savefig(f'{OUT}/revenue_projection.pdf', bbox_inches='tight')
plt.close()
print('revenue_projection.png/pdf')
