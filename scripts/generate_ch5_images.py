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
# Figure 5.1: Testing Pyramid
# ============================================================
fig, ax = plt.subplots(figsize=(6, 5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis('off')

# Pyramid tiers
tiers = [
    (4.0, 6.5, 2.0, 'E2E Tests', '#E74C3C', '34 tests\n9%'),
    (2.5, 4.2, 5.0, 'Integration Tests', '#F39C12', '89 tests\n23%'),
    (0.5, 1.0, 9.0, 'Unit Tests', '#27AE60', '263 tests\n68%'),
]

for x, y, w, label, color, detail in tiers:
    h = 2.0
    rect = mpatches.FancyBboxPatch((x, y), w, h,
                                    boxstyle="round,pad=0.08",
                                    facecolor=color, alpha=0.7, ec='#333', lw=1.5)
    ax.add_patch(rect)
    ax.text(x + w/2, y + h/2, label, ha='center', va='center',
            fontsize=11, fontweight='bold', color='white')
    ax.text(x + w/2, y + h/2 - 0.45, detail, ha='center', va='center',
            fontsize=9, color='white', alpha=0.9)

# Arrow labels on the side
ax.annotate('Faster', xy=(9.8, 7.5), xytext=(9.8, 1.0),
            arrowprops=dict(arrowstyle='->', color='#555', lw=2),
            fontsize=9, color='#555', va='center', ha='right')
ax.text(9.8, 0.5, 'Faster', ha='right', va='center', fontsize=9, color='#555', fontweight='bold')

ax.annotate('More isolated', xy=(0.2, 1.0), xytext=(0.2, 7.5),
            arrowprops=dict(arrowstyle='->', color='#555', lw=2),
            fontsize=9, color='#555', va='center', ha='left')
ax.text(0.2, 0.5, 'More isolated', ha='left', va='center', fontsize=9, color='#555', fontweight='bold')

ax.set_title('Testing Pyramid', fontsize=13, fontweight='bold', pad=10)
plt.tight_layout()
plt.savefig(f'{OUT}/testing_pyramid.png', dpi=180, bbox_inches='tight')
plt.close()
print('Generated testing_pyramid.png')


# ============================================================
# Figure 5.2: E2E Enrollment Flow Sequence Diagram
# ============================================================
fig, ax = plt.subplots(figsize=(10, 7))
ax.set_xlim(0, 12)
ax.set_ylim(0, 9)
ax.axis('off')

# Lifelines
lifelines = [
    (2.0, 'Test', '#333'),
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
    ax.text(x, 7.5, label, ha='center', va='center', fontsize=7.5, fontweight='bold', color=color)

# Messages: (y, from_x, to_x, label, arrow_direction)
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
                    arrowprops=dict(arrowstyle='->', color='#555', lw=1.0))
        ax.text(mx, y+0.15, label, ha='center', va='bottom', fontsize=6, color='#444', style='italic')
    else:
        ax.annotate('', xy=(fx+0.15, y), xytext=(tx-0.15, y),
                    arrowprops=dict(arrowstyle='->', color='#C0392B', lw=1.0))
        ax.text(mx, y-0.25, label, ha='center', va='top', fontsize=6, color='#C0392B', style='italic')

ax.set_title('E2E Test: Student Enrollment Flow', fontsize=12, fontweight='bold', pad=10)
plt.tight_layout()
plt.savefig(f'{OUT}/e2e_enrollment_flow.png', dpi=180, bbox_inches='tight')
plt.close()
print('Generated e2e_enrollment_flow.png')


# ============================================================
# Figure 5.3: Test Schedule Gantt Chart
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
    ax.barh(i, dur, left=start, height=0.6, color=color, alpha=0.8, ec='#333', lw=0.5)
    ax.text(start + 0.05, i, label, va='center', fontsize=8)

ax.set_xlim(0.5, 7.5)
ax.set_ylim(-1, len(phases))
ax.set_yticks([])
ax.set_xticks(range(1, 8))
ax.set_xticklabels([f'Week {i}' for i in range(1, 8)], fontsize=9)
ax.set_xlabel('Development Week', fontsize=10)

legend_elements = [
    mpatches.Patch(color='#27AE60', alpha=0.8, label='Unit Tests'),
    mpatches.Patch(color='#F39C12', alpha=0.8, label='Integration Tests'),
    mpatches.Patch(color='#E74C3C', alpha=0.8, label='E2E Tests'),
    mpatches.Patch(color='#8E44AD', alpha=0.8, label='CI / Reporting'),
]
ax.legend(handles=legend_elements, loc='lower right', fontsize=9)

ax.set_title('Testing Schedule — Gantt Chart', fontsize=12, fontweight='bold', pad=10)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig(f'{OUT}/test_schedule_gantt.png', dpi=180, bbox_inches='tight')
plt.close()
print('Generated test_schedule_gantt.png')
