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

# ──────────────────────────────────────────────
# Figure 2.1  Break-even chart
# ──────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 5.5))

q = np.linspace(0, 1000, 200)
fixed = 20000
unit_var = 40
price = 90

revenue = price * q
total_cost = fixed + unit_var * q
fixed_line = np.full_like(q, fixed)

ax.plot(q, revenue, color=PALETTE['blue'], linewidth=2.8, label='Revenue')
ax.plot(q, total_cost, color=PALETTE['purple'], linewidth=2.8, label='Total Cost')
ax.plot(q, fixed_line, color=PALETTE['gray'], linewidth=1.8, linestyle='--', label='Fixed Cost')

be_q = fixed / (price - unit_var)
be_r = price * be_q
ax.scatter([be_q], [be_r], color=PALETTE['red'], zorder=5, s=100)
ax.annotate(f'Break-even\n({int(be_q)} units, ${int(be_r):,})',
            xy=(be_q, be_r), xytext=(be_q + 120, be_r + 30000),
            arrowprops=dict(arrowstyle='->', color=PALETTE['red'], lw=1.5),
            fontsize=11, color=PALETTE['red'], fontweight='bold')

ax.fill_between(q, revenue, total_cost, where=(revenue >= total_cost),
                interpolate=True, color=PALETTE['blue'], alpha=0.08)
ax.fill_between(q, revenue, total_cost, where=(revenue < total_cost),
                interpolate=True, color=PALETTE['purple'], alpha=0.08)

ax.set_xlim(0, 1000)
ax.set_ylim(0, 100000)
ax.set_xlabel('Units Sold', fontsize=13, fontweight='bold')
ax.set_ylabel('Dollars ($)', fontsize=13, fontweight='bold')
ax.legend(fontsize=11, loc='upper left', framealpha=0.9)
ax.set_title('Figure 2.1 — Break-even Analysis', fontsize=15, fontweight='bold', pad=12)

plt.tight_layout()
fig.savefig(f'{OUT}/break_even_chart.png', dpi=DPI, bbox_inches='tight')
fig.savefig(f'{OUT}/break_even_chart.pdf', bbox_inches='tight')
plt.close()
print('break_even_chart.png/pdf')

# ──────────────────────────────────────────────
# Figure 2.2  Customer segments
# ──────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 5.5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

segments = [
    (1.8, 3.0, 1.8, PALETTE['blue'], 'Students', 'Price-sensitive,\ndigital natives'),
    (5.0, 3.0, 1.8, PALETTE['purple'], 'Professionals', 'Career changers,\nskill upgraders'),
    (8.2, 3.0, 1.8, PALETTE['orange'], 'Enterprises', 'Corporate training,\nbulk licensing'),
    (3.4, 1.2, 1.4, PALETTE['teal'], 'Educators', 'Curriculum\nintegration'),
    (6.6, 1.2, 1.4, PALETTE['green'], 'Institutions', 'Accreditation\npartners'),
]

for x, y, r, color, title, desc in segments:
    circle = mpatches.Circle((x, y), r, color=color, alpha=0.15, ec=color, lw=2.5)
    ax.add_patch(circle)
    ax.text(x, y + 0.1, title, ha='center', va='center', fontsize=13,
            fontweight='bold', color=color)
    ax.text(x, y - 0.65, desc, ha='center', va='center', fontsize=9.5,
            color='#555555', linespacing=1.4)

ax.set_title('Figure 2.2 — Customer Segments', fontsize=15, fontweight='bold', pad=12)

plt.tight_layout()
fig.savefig(f'{OUT}/customer_segments.png', dpi=DPI, bbox_inches='tight')
fig.savefig(f'{OUT}/customer_segments.pdf', bbox_inches='tight')
plt.close()
print('customer_segments.png/pdf')

# ──────────────────────────────────────────────
# Figure 2.3  Competitive positioning
# ──────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 5.5))

ax.axhline(5, color=PALETTE['dark'], lw=1.2)
ax.axvline(5, color=PALETTE['dark'], lw=1.2)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_xticks([2.5, 7.5])
ax.set_xticklabels(['Low Price', 'High Price'], fontsize=11, fontweight='bold')
ax.set_yticks([2.5, 7.5])
ax.set_yticklabels(['Basic Features', 'Advanced Features'], fontsize=11, fontweight='bold')
ax.set_xlabel('Price', fontsize=13, fontweight='bold', labelpad=8)
ax.set_ylabel('Feature Set', fontsize=13, fontweight='bold', labelpad=8)

ax.text(2.5, 7.5, 'Cost Leaders', ha='center', va='center', fontsize=12,
        fontweight='bold', color=PALETTE['gray'], alpha=0.4)
ax.text(7.5, 7.5, 'Premium Players', ha='center', va='center', fontsize=12,
        fontweight='bold', color=PALETTE['gray'], alpha=0.4)
ax.text(2.5, 2.5, 'Budget Options', ha='center', va='center', fontsize=12,
        fontweight='bold', color=PALETTE['gray'], alpha=0.4)
ax.text(7.5, 2.5, 'Niche Specialists', ha='center', va='center', fontsize=12,
        fontweight='bold', color=PALETTE['gray'], alpha=0.4)

competitors = [
    (2.0, 8.5, PALETTE['blue'], 'Competitor A', 320),
    (3.5, 6.5, PALETTE['teal'], 'Competitor B', 260),
    (7.0, 8.0, PALETTE['purple'], 'Competitor C', 280),
    (8.5, 7.0, PALETTE['red'], 'Competitor D', 220),
    (1.5, 3.0, PALETTE['green'], 'Competitor E', 300),
    (6.0, 2.5, PALETTE['orange'], 'Competitor F', 240),
]

for x, y, color, name, _ in competitors:
    ax.scatter(x, y, color=color, s=180, zorder=5, edgecolors='white', linewidth=1.5)
    ax.annotate(name, (x, y), textcoords='offset points', xytext=(8, 6),
                fontsize=10, fontweight='bold', color=color)

ax.scatter(4.0, 7.2, color=PALETTE['dark'], s=260, zorder=6, edgecolors='#FFD166', linewidth=2.5,
           marker='*')
ax.annotate('Us', (4.0, 7.2), textcoords='offset points', xytext=(10, 8),
            fontsize=12, fontweight='bold', color=PALETTE['dark'])

ax.set_title('Figure 2.3 — Competitive Positioning Map', fontsize=15, fontweight='bold', pad=12)

plt.tight_layout()
fig.savefig(f'{OUT}/competitive_positioning.png', dpi=DPI, bbox_inches='tight')
fig.savefig(f'{OUT}/competitive_positioning.pdf', bbox_inches='tight')
plt.close()
print('competitive_positioning.png/pdf')

print('\nAll figures generated.')
