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
# Figure 5.1: Testing Pyramid — Redesigned
# ============================================================
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis('off')

pyramid_colors = [
    (PALETTE['red'], '#E74C3C'),
    (PALETTE['orange'], '#F39C12'),
    (PALETTE['green'], '#27AE60'),
]

tiers_data = [
    ('E2E Tests', 34, '9%', 2, 6.5, 0),
    ('Integration Tests', 89, '23%', 5, 4.2, 1),
    ('Unit Tests (Base)', 263, '68%', 9, 1.0, 2),
]

for label, count, pct, top_width, y_base, idx in tiers_data:
    color, fill = pyramid_colors[idx]
    bottom_width = top_width + 1.5
    cx = 5.0
    half_bot = bottom_width / 2
    half_top = top_width / 2
    h = 2.0
    x_bot_l = cx - half_bot
    x_bot_r = cx + half_bot
    x_top_l = cx - half_top
    x_top_r = cx + half_top

    verts = [(x_bot_l, y_base), (x_bot_r, y_base),
             (x_top_r, y_base + h), (x_top_l, y_base + h)]
    poly = plt.Polygon(verts, closed=True, facecolor=fill, alpha=0.85,
                       ec=PALETTE['dark'], lw=2, joinstyle='round')
    ax.add_patch(poly)

    ax.text(cx, y_base + h / 2 + 0.15, label, ha='center', va='center',
            fontsize=14, fontweight='bold', color='white')
    ax.text(cx, y_base + h / 2 - 0.45, f'{count} tests  ·  {pct}', ha='center', va='center',
            fontsize=11, color='white', alpha=0.95)

# Left axis: isolation
ax.annotate('', xy=(0.3, 1.2), xytext=(0.3, 7.8),
            arrowprops=dict(arrowstyle='->', color=PALETTE['gray'], lw=2.5))
for i, txt in enumerate(['More\nIsolated', '', '', '', 'Faster']):
    ax.text(0.15, 1.2 + i * 1.6, txt, ha='left', va='center',
            fontsize=10, color=PALETTE['gray'], fontweight='bold')

# Right axis: speed
ax.annotate('', xy=(9.7, 7.8), xytext=(9.7, 1.2),
            arrowprops=dict(arrowstyle='->', color=PALETTE['gray'], lw=2.5))
for i, txt in enumerate(['Faster', '', '', '', 'More\nIsolated']):
    ax.text(9.95, 7.8 - i * 1.6, txt, ha='right', va='center',
            fontsize=10, color=PALETTE['gray'], fontweight='bold')

# Icon labels
ax.text(5.0, 0.3, '▲  Wider base = more confidence  ▲', ha='center', va='center',
        fontsize=10, color=PALETTE['gray'], fontstyle='italic')

ax.set_title('NexaLearn Testing Pyramid', fontsize=16, fontweight='bold', pad=12)
plt.tight_layout()
plt.savefig(f'{OUT}/testing_pyramid.png', dpi=DPI, bbox_inches='tight')
plt.savefig(f'{OUT}/testing_pyramid.pdf', bbox_inches='tight')
plt.close()
print('testing_pyramid.png/pdf')

# ============================================================
# Figure 5.2: E2E Enrollment Flow
# ============================================================
fig, ax = plt.subplots(figsize=(10, 7))
ax.set_xlim(0, 12)
ax.set_ylim(0, 9)
ax.axis('off')

lifelines = [
    (2.0, 'Test', PALETTE['dark']),
    (4.5, 'Auth\nModule', '#2980B9'),
    (6.5, 'Payment\nModule', '#8E44AD'),
    (8.5, 'Enrollment\nModule', '#27AE60'),
    (10.5, 'Database', '#D35400'),
]

for x, label, color in lifelines:
    ax.plot([x, x], [1.5, 8.0], color=color, lw=1.5, linestyle='--', alpha=0.5)
    rect = mpatches.FancyBboxPatch((x-0.8, 7.0), 1.6, 1.0,
                                    boxstyle="round,pad=0.08",
                                    facecolor=color, alpha=0.15, ec=color, lw=1.5)
    ax.add_patch(rect)
    ax.text(x, 7.5, label, ha='center', va='center', fontsize=8.5, fontweight='bold', color=color)

messages = [
    (6.5, 2.0, 4.5, 'POST /auth/register (email, password)', 'right'),
    (6.0, 4.5, 10.5, 'INSERT user (tx)', 'right'),
    (5.7, 10.5, 2.0, '201 Created + activation token', 'left'),
    (5.0, 2.0, 4.5, 'POST /auth/login (email, password)', 'right'),
    (4.7, 4.5, 10.5, 'SELECT user + password hash', 'right'),
    (4.4, 10.5, 2.0, '200 OK + access/refresh tokens', 'left'),
    (3.8, 2.0, 6.5, 'POST /payments/create-intent (courseId)', 'right'),
    (3.5, 6.5, 10.5, 'INSERT payment_intent', 'right'),
    (3.2, 10.5, 2.0, '201 { clientSecret }', 'left'),
    (2.6, 2.0, 6.5, 'POST /webhooks/stripe (payment_intent.succeeded)', 'right'),
    (2.3, 6.5, 10.5, 'UPDATE payment_intent → SUCCEEDED', 'right'),
    (2.0, 6.5, 8.5, 'DomainEvent: PaymentSucceeded', 'right'),
    (1.7, 8.5, 10.5, 'INSERT enrollment (ACTIVE)', 'right'),
]

for y, fx, tx, label, direction in messages:
    mx = (fx + tx) / 2
    if direction == 'right':
        ax.annotate('', xy=(tx-0.15, y), xytext=(fx+0.15, y),
                    arrowprops=dict(arrowstyle='->', color=PALETTE['gray'], lw=1.0))
        ax.text(mx, y+0.15, label, ha='center', va='bottom', fontsize=6.5, color='#444', style='italic')
    else:
        ax.annotate('', xy=(fx+0.15, y), xytext=(tx-0.15, y),
                    arrowprops=dict(arrowstyle='->', color='#C0392B', lw=1.0))
        ax.text(mx, y-0.25, label, ha='center', va='top', fontsize=6.5, color='#C0392B', style='italic')

ax.set_title('E2E Test: Student Enrollment Flow', fontsize=14, fontweight='bold', pad=10)
plt.tight_layout()
plt.savefig(f'{OUT}/e2e_enrollment_flow.png', dpi=DPI, bbox_inches='tight')
plt.savefig(f'{OUT}/e2e_enrollment_flow.pdf', bbox_inches='tight')
plt.close()
print('e2e_enrollment_flow.png/pdf')

# ============================================================
# Figure 5.3: Test Schedule Gantt
# ============================================================
fig, ax = plt.subplots(figsize=(10, 6))

phases = [
    ('Unit: Framework Setup', 1, 1, '#27AE60'),
    ('Unit: Domain Entities (Auth/Courses/Media)', 1, 1, '#27AE60'),
    ('Unit: Domain Entities (Assessment/Payment)', 2, 1, '#27AE60'),
    ('Unit: Domain Entities (Remaining)', 2, 1, '#27AE60'),
    ('Unit: Domain Services', 2, 2, '#2ECC71'),
    ('Unit: Pure Function Tests', 3, 1, '#2ECC71'),
    ('Integration: Testcontainers Setup', 3, 1, '#F39C12'),
    ('Integration: DB Tests (Auth/Courses)', 4, 1, '#F39C12'),
    ('Integration: DB Tests (Payment)', 4, 1, '#F39C12'),
    ('Integration: Outbox Processor', 4, 1, '#F39C12'),
    ('Integration: Cross-Module', 5, 1, '#F39C12'),
    ('E2E: Test Bootstrap', 5, 0.5, '#E74C3C'),
    ('E2E: Auth & Course Flows', 5, 0.5, '#E74C3C'),
    ('E2E: AI Pipeline & Payment', 6, 0.5, '#E74C3C'),
    ('E2E: Remaining Flows', 6, 0.5, '#E74C3C'),
    ('Coverage Report & CI', 6, 1, '#8E44AD'),
]

for i, (label, start, dur, color) in enumerate(phases):
    ax.barh(i, dur, left=start, height=0.6, color=color, alpha=0.8, ec=PALETTE['dark'], lw=0.5)
    ax.text(start + 0.05, i, label, va='center', fontsize=9)

ax.set_xlim(0.5, 7.5)
ax.set_ylim(-1, len(phases))
ax.set_yticks([])
ax.set_xticks(range(1, 8))
ax.set_xticklabels([f'Week {i}' for i in range(1, 8)], fontsize=10)
ax.set_xlabel('Development Week', fontsize=12)

legend_elements = [
    mpatches.Patch(color='#27AE60', alpha=0.8, label='Unit Tests'),
    mpatches.Patch(color='#F39C12', alpha=0.8, label='Integration Tests'),
    mpatches.Patch(color='#E74C3C', alpha=0.8, label='E2E Tests'),
    mpatches.Patch(color='#8E44AD', alpha=0.8, label='CI / Reporting'),
]
ax.legend(handles=legend_elements, loc='lower right', fontsize=10)

ax.set_title('Testing Schedule — Gantt Chart', fontsize=14, fontweight='bold', pad=10)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig(f'{OUT}/test_schedule_gantt.png', dpi=DPI, bbox_inches='tight')
plt.savefig(f'{OUT}/test_schedule_gantt.pdf', bbox_inches='tight')
plt.close()
print('test_schedule_gantt.png/pdf')
