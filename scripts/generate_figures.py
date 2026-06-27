import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 11,
    'axes.facecolor': '#FAFAFA',
    'figure.facecolor': 'white',
    'axes.edgecolor': '#CCCCCC',
    'axes.grid': True,
    'grid.alpha': 0.3,
    'grid.color': '#999999',
})

OUT = '/Users/youssefbahy/Documents/Training/NexaLearnFullProject/newbook/images'

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

ax.plot(q, revenue, color='#2E86AB', linewidth=2.8, label='Revenue')
ax.plot(q, total_cost, color='#A23B72', linewidth=2.8, label='Total Cost')
ax.plot(q, fixed_line, color='#888888', linewidth=1.8, linestyle='--', label='Fixed Cost')

be_q = fixed / (price - unit_var)
be_r = price * be_q
ax.scatter([be_q], [be_r], color='#D62828', zorder=5, s=100)
ax.annotate(f'Break-even\n({int(be_q)} units, ${int(be_r):,})',
            xy=(be_q, be_r), xytext=(be_q + 120, be_r + 30000),
            arrowprops=dict(arrowstyle='->', color='#D62828', lw=1.5),
            fontsize=10, color='#D62828', fontweight='bold')

ax.fill_between(q, revenue, total_cost, where=(revenue >= total_cost),
                interpolate=True, color='#2E86AB', alpha=0.08)
ax.fill_between(q, revenue, total_cost, where=(revenue < total_cost),
                interpolate=True, color='#A23B72', alpha=0.08)

ax.set_xlim(0, 1000)
ax.set_ylim(0, 100000)
ax.set_xlabel('Units Sold', fontsize=12, fontweight='bold')
ax.set_ylabel('Dollars ($)', fontsize=12, fontweight='bold')
ax.legend(fontsize=10, loc='upper left', framealpha=0.9)
ax.set_title('Figure 2.1 — Break-even Analysis', fontsize=14, fontweight='bold', pad=12)

plt.tight_layout()
fig.savefig(f'{OUT}/break_even_chart.png', dpi=200, bbox_inches='tight')
plt.close()
print('✓ break_even_chart.png')

# ──────────────────────────────────────────────
# Figure 2.2  Customer segments
# ──────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 5.5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

segments = [
    (1.8, 3.0, 1.8, '#2E86AB', 'Students', 'Price-sensitive,\ndigital natives'),
    (5.0, 3.0, 1.8, '#A23B72', 'Professionals', 'Career changers,\nskill upgraders'),
    (8.2, 3.0, 1.8, '#F18F01', 'Enterprises', 'Corporate training,\nbulk licensing'),
    (3.4, 1.2, 1.4, '#577590', 'Educators', 'Curriculum\nintegration'),
    (6.6, 1.2, 1.4, '#43AA8B', 'Institutions', 'Accreditation\npartners'),
]

for x, y, r, color, title, desc in segments:
    circle = mpatches.Circle((x, y), r, color=color, alpha=0.15, ec=color, lw=2.5)
    ax.add_patch(circle)
    ax.text(x, y + 0.1, title, ha='center', va='center', fontsize=12,
            fontweight='bold', color=color)
    ax.text(x, y - 0.65, desc, ha='center', va='center', fontsize=8.5,
            color='#555555', linespacing=1.4)

ax.set_title('Figure 2.2 — Customer Segments', fontsize=14, fontweight='bold', pad=12)

plt.tight_layout()
fig.savefig(f'{OUT}/customer_segments.png', dpi=200, bbox_inches='tight')
plt.close()
print('✓ customer_segments.png')

# ──────────────────────────────────────────────
# Figure 2.3  Competitive positioning
# ──────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 5.5))

# 2x2 grid
ax.axhline(5, color='#333333', lw=1.2)
ax.axvline(5, color='#333333', lw=1.2)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_xticks([2.5, 7.5])
ax.set_xticklabels(['Low Price', 'High Price'], fontsize=10, fontweight='bold')
ax.set_yticks([2.5, 7.5])
ax.set_yticklabels(['Basic Features', 'Advanced Features'], fontsize=10, fontweight='bold')
ax.set_xlabel('Price', fontsize=12, fontweight='bold', labelpad=8)
ax.set_ylabel('Feature Set', fontsize=12, fontweight='bold', labelpad=8)

# quadrant labels
ax.text(2.5, 7.5, 'Cost Leaders', ha='center', va='center', fontsize=11,
        fontweight='bold', color='#888888', alpha=0.4)
ax.text(7.5, 7.5, 'Premium Players', ha='center', va='center', fontsize=11,
        fontweight='bold', color='#888888', alpha=0.4)
ax.text(2.5, 2.5, 'Budget Options', ha='center', va='center', fontsize=11,
        fontweight='bold', color='#888888', alpha=0.4)
ax.text(7.5, 2.5, 'Niche Specialists', ha='center', va='center', fontsize=11,
        fontweight='bold', color='#888888', alpha=0.4)

# competitors
competitors = [
    (2.0, 8.5, '#2E86AB', 'Competitor A', 320),
    (3.5, 6.5, '#577590', 'Competitor B', 260),
    (7.0, 8.0, '#A23B72', 'Competitor C', 280),
    (8.5, 7.0, '#D62828', 'Competitor D', 220),
    (1.5, 3.0, '#43AA8B', 'Competitor E', 300),
    (6.0, 2.5, '#F18F01', 'Competitor F', 240),
]

for x, y, color, name, _ in competitors:
    ax.scatter(x, y, color=color, s=180, zorder=5, edgecolors='white', linewidth=1.5)
    ax.annotate(name, (x, y), textcoords='offset points', xytext=(8, 6),
                fontsize=9, fontweight='bold', color=color)

# us
ax.scatter(4.0, 7.2, color='#111111', s=260, zorder=6, edgecolors='#FFD166', linewidth=2.5,
           marker='*')
ax.annotate('Us', (4.0, 7.2), textcoords='offset points', xytext=(10, 8),
            fontsize=11, fontweight='bold', color='#111111')

ax.set_title('Figure 2.3 — Competitive Positioning Map', fontsize=14, fontweight='bold', pad=12)

plt.tight_layout()
fig.savefig(f'{OUT}/competitive_positioning.png', dpi=200, bbox_inches='tight')
plt.close()
print('✓ competitive_positioning.png')

print('\nAll figures generated.')
