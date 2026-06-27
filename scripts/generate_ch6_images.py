import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 10,
    'axes.facecolor': '#FAFAFA',
    'figure.facecolor': 'white',
    'axes.edgecolor': '#CCCCCC',
})

OUT = '/Users/youssefbahy/Documents/Training/NexaLearnFullProject/newbook/images'

# ============================================================
# Figure 6.1: Skills Radar Chart
# ============================================================
categories = [
    'DDD &\nClean Arch.',
    'Event-Driven\nArchitecture',
    'Third-Party\nAPI Integration',
    'Idempotency &\nExactly-Once',
    'Redis &\nCaching',
    'Docker &\nDevOps',
    'API Design\n(Swagger)',
    'Testing\n(Jest/TC)',
]

values = [4.8, 4.5, 4.2, 4.6, 4.0, 3.8, 4.3, 4.7]

N = len(categories)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
values += values[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(7, 7), subplot_kw={'polar': True})
ax.fill(angles, values, color='#2980B9', alpha=0.25)
ax.plot(angles, values, color='#2980B9', linewidth=2, marker='o', markersize=8)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=9, fontweight='bold')
ax.set_ylim(0, 5)
ax.set_yticks([1, 2, 3, 4, 5])
ax.set_yticklabels(['1', '2', '3', '4', '5'], fontsize=8, color='#888')
ax.grid(True, alpha=0.3)

ax.set_title('Skills Gained — Self Assessment', fontsize=14, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig(f'{OUT}/skills_radar.png', dpi=180, bbox_inches='tight')
plt.close()
print('Generated skills_radar.png')


# ============================================================
# Figure 6.2: Video Rendition State Machine
# ============================================================
fig, ax = plt.subplots(figsize=(8, 4))
ax.set_xlim(0, 10)
ax.set_ylim(0, 4)
ax.axis('off')

states = [
    (1.5, 2.0, 'UPLOADED', '#E67E22', '#FEEED6'),
    (4.0, 2.0, 'PROCESSING', '#3498DB', '#D6EEFB'),
    (6.5, 2.0, 'READY', '#27AE60', '#D5F5E3'),
    (9.0, 2.0, 'MP4_AVAILABLE', '#2ECC71', '#D5F5E3'),
]
state_positions = {}

for x, y, name, ec, fc in states:
    state_positions[name] = (x, y)
    rect = mpatches.FancyBboxPatch((x-0.8, y-0.35), 1.6, 0.7,
                                    boxstyle="round,pad=0.1",
                                    facecolor=fc, ec=ec, lw=2.5)
    ax.add_patch(rect)
    ax.text(x, y, name, ha='center', va='center', fontsize=8, fontweight='bold', color=ec)

# Initial arrow
ax.annotate('', xy=(1.5-0.8, 2.0), xytext=(0.1, 2.0),
            arrowprops=dict(arrowstyle='->', color='#333', lw=1.5))
ax.text(0.0, 2.25, 'upload', ha='center', va='bottom', fontsize=7, color='#555', style='italic')

# Transitions
transitions = [
    ('UPLOADED', 'PROCESSING', 'upload\ncomplete'),
    ('PROCESSING', 'READY', 'transcode\ndone'),
    ('READY', 'MP4_AVAILABLE', 'mp4 rendition\nready'),
]

for src, dst, label in transitions:
    x1, y1 = state_positions[src]
    x2, y2 = state_positions[dst]
    x1r = x1 + 0.8
    x2l = x2 - 0.8
    ax.annotate('', xy=(x2l, y2), xytext=(x1r, y1),
                arrowprops=dict(arrowstyle='->', color='#555', lw=1.5, connectionstyle='arc3,rad=0.15'))
    mx = (x1r + x2l) / 2
    ax.text(mx, y1 + 0.35, label, ha='center', va='bottom', fontsize=6.5, color='#555', style='italic')

# Error transition
ax.annotate('', xy=(3.5, 3.0), xytext=(5.0, 3.0),
            arrowprops=dict(arrowstyle='->', color='#E74C3C', lw=1.2, connectionstyle='arc3,rad=0.3'))
ax.text(4.25, 3.4, 'error', ha='center', va='bottom', fontsize=6.5, color='#E74C3C', style='italic')

ax.set_title('Video Asset State Machine with MP4 Rendition', fontsize=11, fontweight='bold', pad=10)
plt.tight_layout()
plt.savefig(f'{OUT}/video_rendition_statemachine.png', dpi=180, bbox_inches='tight')
plt.close()
print('Generated video_rendition_statemachine.png')


# ============================================================
# Figure 6.3: Future Work Roadmap
# ============================================================
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# Timeline base
ax.plot([0.5, 9.5], [0.5, 0.5], color='#333', lw=2, zorder=1)
for x, label in [(1.5, 'Month 1'), (4.0, 'Month 6'), (6.5, 'Month 12'), (9.0, 'Month 18+')]:
    ax.plot([x, x], [0.3, 0.7], color='#333', lw=2, zorder=1)
    ax.text(x, 0.1, label, ha='center', va='top', fontsize=8, fontweight='bold')

# Phase labels
phases = [
    (1.5, 'Short Term\n(1--6 months)', '#2980B9', [
        ('WebSocket Real-Time', 2.5),
        ('OAuth2 Social Login', 2.0),
        ('Redis Rate Limiter', 1.5),
        ('React/Next.js Frontend', 1.0),
    ]),
    (5.0, 'Medium Term\n(7--12 months)', '#8E44AD', [
        ('Microservices Extraction', 6.0),
        ('GraphQL API Layer', 5.5),
        ('Multi-Tenant Isolation', 5.0),
        ('Push Notifications', 4.5),
    ]),
    (8.5, 'Long Term\n(12+ months)', '#27AE60', [
        ('Course Recommendation', 9.0),
        ('Blockchain Certificates', 8.5),
        ('Mobile SDK', 8.0),
    ]),
]

for phase_x, phase_label, phase_color, items in phases:
    item_ys = [item[1] for item in items]
    y_min = min(item_ys) - 0.5
    y_max = max(item_ys) + 0.5
    rect = mpatches.FancyBboxPatch((phase_x - 0.3, y_min - 0.3), 2.6, y_max - y_min + 0.6,
                                    boxstyle="round,pad=0.08",
                                    facecolor=phase_color, alpha=0.08, ec=phase_color, lw=1.5, ls='--')
    ax.add_patch(rect)

    # Phase title
    ax.text(phase_x + 1.0, y_max + 0.3, phase_label, ha='center', va='bottom',
            fontsize=9, fontweight='bold', color=phase_color)

    for item_label, item_y in items:
        ax.plot([phase_x + 0.3, 9.5], [item_y, item_y],
                color=phase_color, lw=1, alpha=0.3, ls='--')
        dot_x = phase_x + 0.3
        dot = mpatches.Circle((dot_x, item_y), 0.08, color=phase_color, zorder=3)
        ax.add_patch(dot)
        ax.text(dot_x + 0.2, item_y, item_label, va='center', fontsize=7.5, color='#333')

ax.set_title('Future Development Roadmap', fontsize=13, fontweight='bold', pad=15)
plt.tight_layout()
plt.savefig(f'{OUT}/future_work_roadmap.png', dpi=180, bbox_inches='tight')
plt.close()
print('Generated future_work_roadmap.png')
