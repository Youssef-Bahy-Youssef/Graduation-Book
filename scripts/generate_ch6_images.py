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
})

OUT = '/Users/youssefbahy/Documents/Training/NexaLearnFullProject/newbook/images'
DPI = 300

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
ax.fill(angles, values, color=PALETTE['blue'], alpha=0.25)
ax.plot(angles, values, color=PALETTE['blue'], linewidth=2, marker='o', markersize=8)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10, fontweight='bold')
ax.set_ylim(0, 5)
ax.set_yticks([1, 2, 3, 4, 5])
ax.set_yticklabels(['1', '2', '3', '4', '5'], fontsize=9, color=PALETTE['gray'])
ax.grid(True, alpha=0.3)

ax.set_title('Skills Gained — Self Assessment', fontsize=15, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig(f'{OUT}/skills_radar.png', dpi=DPI, bbox_inches='tight')
plt.savefig(f'{OUT}/skills_radar.pdf', bbox_inches='tight')
plt.close()
print('skills_radar.png/pdf')

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
    ax.text(x, y, name, ha='center', va='center', fontsize=9, fontweight='bold', color=ec)

ax.annotate('', xy=(1.5-0.8, 2.0), xytext=(0.1, 2.0),
            arrowprops=dict(arrowstyle='->', color=PALETTE['dark'], lw=1.5))
ax.text(0.0, 2.25, 'upload', ha='center', va='bottom', fontsize=8, color=PALETTE['gray'], style='italic')

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
                arrowprops=dict(arrowstyle='->', color=PALETTE['gray'], lw=1.5, connectionstyle='arc3,rad=0.15'))
    mx = (x1r + x2l) / 2
    ax.text(mx, y1 + 0.35, label, ha='center', va='bottom', fontsize=7.5, color=PALETTE['gray'], style='italic')

ax.annotate('', xy=(3.5, 3.0), xytext=(5.0, 3.0),
            arrowprops=dict(arrowstyle='->', color='#E74C3C', lw=1.2, connectionstyle='arc3,rad=0.3'))
ax.text(4.25, 3.4, 'error', ha='center', va='bottom', fontsize=7.5, color='#E74C3C', style='italic')

ax.set_title('Video Asset State Machine with MP4 Rendition', fontsize=13, fontweight='bold', pad=10)
plt.tight_layout()
plt.savefig(f'{OUT}/video_rendition_statemachine.png', dpi=DPI, bbox_inches='tight')
plt.savefig(f'{OUT}/video_rendition_statemachine.pdf', bbox_inches='tight')
plt.close()
print('video_rendition_statemachine.png/pdf')

# ============================================================
# Figure 6.3: Future Work Roadmap
# ============================================================
fig, ax = plt.subplots(figsize=(11, 5.5))
ax.set_xlim(0, 12)
ax.set_ylim(0, 7)
ax.axis('off')

timeline_y = 6.2
ax.plot([0.8, 11.2], [timeline_y, timeline_y], color=PALETTE['dark'], lw=2, zorder=1)
ticks = [(2.0, 'Month 1'), (4.5, 'Month 6'), (7.0, 'Month 12'), (9.5, 'Month 18'), (11.0, '24+')]
for x, label in ticks:
    ax.plot([x, x], [timeline_y - 0.2, timeline_y + 0.2], color=PALETTE['dark'], lw=2, zorder=1)
    ax.text(x, timeline_y - 0.5, label, ha='center', va='top', fontsize=8, fontweight='bold', color=PALETTE['dark'])
ax.text(0.8, timeline_y + 0.4, 'Timeline', ha='left', va='bottom', fontsize=9, fontweight='bold', color=PALETTE['dark'])

phases = [
    ('Short Term\n(1–6 months)', PALETTE['blue'], 1.5, 3.0, [
        ('WebSocket Real-Time Updates', 5.0, PALETTE['blue']),
        ('OAuth2 Social Login (Google/GitHub)', 4.2, PALETTE['blue']),
        ('Redis Rate Limiter & Caching', 3.4, PALETTE['blue']),
        ('React / Next.js Frontend', 2.6, PALETTE['blue']),
    ]),
    ('Medium Term\n(7–12 months)', '#8E44AD', 4.0, 3.0, [
        ('Microservices Extraction (Bounded Contexts)', 5.0, '#8E44AD'),
        ('GraphQL API Layer (code-first)', 4.2, '#8E44AD'),
        ('Multi-Tenant Organisation Isolation', 3.4, '#8E44AD'),
        ('Push Notifications (FCM / APNs)', 2.6, '#8E44AD'),
    ]),
    ('Long Term\n(12+ months)', PALETTE['green'], 6.5, 3.0, [
        ('AI Course Recommendation Engine', 5.0, PALETTE['green']),
        ('Blockchain-Backed Certificates', 4.2, PALETTE['green']),
        ('Mobile SDK for iOS / Android', 3.4, PALETTE['green']),
    ]),
    ('Vision\n(24+ months)', PALETTE['teal'], 9.0, 2.8, [
        ('Full LMS Marketplace', 5.0, PALETTE['teal']),
        ('White-Label Deployments', 3.4, PALETTE['teal']),
    ]),
]

for phase_label, phase_color, px, pw, items in phases:
    item_ys = [iy for _, iy, _ in items]
    y_min = min(item_ys) - 0.5
    y_max = max(item_ys) + 0.5
    bg = mpatches.FancyBboxPatch((px - 0.3, y_min - 0.3), pw + 0.6, y_max - y_min + 0.6,
                                  boxstyle="round,pad=0.1",
                                  facecolor=phase_color, alpha=0.06, ec=phase_color, lw=1.5, ls='-')
    ax.add_patch(bg)
    ax.text(px + pw / 2, y_max + 0.3, phase_label, ha='center', va='bottom',
            fontsize=10, fontweight='bold', color=phase_color)
    for item_label, item_y, _ in items:
        bar_w = pw * 0.75
        bar_h = 0.3
        bar_x = px + pw * 0.1
        ax.barh(item_y, bar_w, height=bar_h, left=bar_x, color=phase_color, alpha=0.6,
                edgecolor=phase_color, lw=1, zorder=3)
        ax.text(bar_x + bar_w + 0.15, item_y, item_label, va='center', fontsize=8.5,
                color=PALETTE['dark'], fontweight='bold')

ax.set_title('Future Development Roadmap', fontsize=15, fontweight='bold', pad=15)
plt.tight_layout()
plt.savefig(f'{OUT}/future_work_roadmap.png', dpi=DPI, bbox_inches='tight')
plt.savefig(f'{OUT}/future_work_roadmap.pdf', bbox_inches='tight')
plt.close()
print('future_work_roadmap.png/pdf')
