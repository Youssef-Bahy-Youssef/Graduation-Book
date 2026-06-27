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
SM = f'{OUT}/statemachines'
DPI = 300

def state_machine(figsize, states, transitions, title, filename, cols=3):
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')

    n = len(states)
    rows = int(np.ceil(n / cols))
    positions = {}

    for i, (name, color) in enumerate(states):
        row, col = divmod(i, cols)
        x = 1.5 + col * (9.0 / max(cols - 1, 1))
        y = 6.5 - row * (5.5 / max(rows - 1, 1))
        positions[name] = (x, y)

        bw, bh = 2.4, 0.8
        rect = mpatches.FancyBboxPatch((x - bw/2, y - bh/2), bw, bh,
                                        boxstyle="round,pad=0.12",
                                        facecolor=color, alpha=0.1, ec=color, lw=2.5)
        ax.add_patch(rect)
        ax.text(x, y, name.replace('_', ' ').title(), ha='center', va='center',
                fontsize=12, fontweight='bold', color=color)

    drawn = set()
    for src, dst, label in transitions:
        if src not in positions or dst not in positions:
            continue
        key = (src, dst)
        if key in drawn:
            continue
        drawn.add(key)

        x1, y1 = positions[src]
        x2, y2 = positions[dst]
        dx, dy = x2 - x1, y2 - y1
        rad = 0.2
        if abs(dx) < 0.8 and abs(dy) < 0.8:
            rad = 0.5
        elif abs(dx) < 1.0:
            rad = 0.35

        ax.annotate('', xy=(x2, y2 - 0.4), xytext=(x1, y1 + 0.4),
                    arrowprops=dict(arrowstyle='->', color=PALETTE['dark'], lw=2,
                                    connectionstyle=f'arc3,rad={rad}'))

        mx, my = (x1 + x2) / 2, (y1 + y2) / 2 + 0.45
        ax.text(mx, my, label, ha='center', va='bottom', fontsize=9.5,
                color='#444444', style='italic',
                bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='#BBBBBB', lw=0.6, alpha=0.9))

    ax.set_title(title, fontsize=14, fontweight='bold', pad=10)
    plt.tight_layout()
    plt.savefig(f'{SM}/{filename}', dpi=DPI, bbox_inches='tight')
    pdf_name = filename.replace('.png', '.pdf')
    plt.savefig(f'{SM}/{pdf_name}', bbox_inches='tight')
    plt.close()
    print(f'{filename} -> {pdf_name}')

# === System Architecture (Figure 4.1) ===
fig, ax = plt.subplots(figsize=(12, 8.5))
ax.set_xlim(0, 13)
ax.set_ylim(0, 9)
ax.axis('off')

layers = [
    (0.5, 7.0, 12.0, 1.4, '#E8F4F8', PALETTE['blue'],
     'PRESENTATION LAYER', ['NestJS Controllers', 'Guards & Pipes', 'Interceptors', 'DTO Validation']),
    (0.5, 5.2, 12.0, 1.4, '#F0E6F6', PALETTE['purple'],
     'APPLICATION LAYER', ['Use Cases / Interactors', 'CQRS Commands', 'CQRS Queries', 'Mappers']),
    (0.5, 1.6, 5.8, 3.2, '#FFF3E0', PALETTE['orange'],
     'DOMAIN LAYER', ['Entities & Aggregates', 'Value Objects', 'Domain Events', 'Repository Ports']),
    (6.7, 1.6, 5.8, 3.2, '#E8F5E9', PALETTE['green'],
     'INFRASTRUCTURE LAYER', ['Prisma Repositories', 'Stripe SDK Adapter', 'Mux SDK Adapter', 'Redis Client', 'Transactional Outbox']),
    (0.5, 0.3, 12.0, 1.0, '#F5F5F5', PALETTE['gray'],
     'EXTERNAL INTEGRATIONS', ['PostgreSQL', 'Redis', 'Stripe API', 'Mux API', 'Resend (Email)', 'AWS S3']),
]

for x, y, w, h, bg, border, title, components in layers:
    rect = mpatches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1",
                                    facecolor=bg, ec=border, lw=2)
    ax.add_patch(rect)
    y_comp = y + h - 0.35
    for i, comp in enumerate(components):
        fc = 'white' if border == PALETTE['gray'] else bg
        bbox = dict(boxstyle='round,pad=0.2', fc=fc, ec=border, lw=0.8)
        ax.text(x + 0.3 + (i % 2) * 2.8, y_comp - (i // 2) * 0.45, f'  {comp}  ',
                fontsize=8, color='#222222', fontweight='bold', bbox=bbox, va='center')
    ax.text(x + w/2, y + h - 0.25, title, ha='center', va='top',
            fontsize=11, color=border, fontweight='bold')

# Protocol arrows on right side
arrows = [
    (12.2, 6.3, 12.2, 5.7, PALETTE['blue'], 'HTTP/JSON'),
    (12.2, 4.5, 12.2, 3.8, PALETTE['purple'], 'Method Calls'),
    (6.3, 3.4, 6.7, 3.4, PALETTE['orange'], 'Repository Port → Impl'),
    (6.3, 2.2, 6.7, 2.2, PALETTE['red'], 'Domain Events'),
    (12.2, 2.8, 12.2, 1.0, PALETTE['green'], 'TCP/HTTP SDK Calls'),
]

for x1, y1, x2, y2, color, label in arrows:
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=2.5))
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    ha = 'left' if x1 >= 12 else 'center'
    ax.text(mx + (0.3 if ha == 'left' else 0), my, label,
            ha=ha, va='center', fontsize=8, fontweight='bold', color=color)

# Bounded context modules in the Domain layer
modules = [
    ('Auth', 0.8, 4.0, PALETTE['blue']), ('Courses', 2.2, 4.0, PALETTE['green']),
    ('Enrollment', 3.6, 4.0, PALETTE['orange']), ('Payments', 5.0, 4.0, PALETTE['orange']),
    ('Media', 0.8, 3.3, PALETTE['teal']), ('AI-Pipeline', 2.2, 3.3, PALETTE['teal']),
    ('Assessment', 3.6, 3.3, PALETTE['purple']), ('Discussion', 5.0, 3.3, PALETTE['red']),
    ('Progress', 0.8, 2.6, PALETTE['blue']), ('Reviews', 2.2, 2.6, PALETTE['purple']),
    ('Certificates', 3.6, 2.6, PALETTE['teal']), ('Search', 5.0, 2.6, PALETTE['blue']),
    ('Notifications', 0.8, 1.9, PALETTE['purple']), ('Streak', 2.2, 1.9, PALETTE['orange']),
    ('Instructor', 3.6, 1.9, PALETTE['green']),
]

for name, x, y, color in modules:
    ax.text(x, y, name, fontsize=8, fontweight='bold', color='white',
            bbox=dict(boxstyle='round,pad=0.25', fc=color, ec='white', lw=0.8),
            ha='center', va='center')

ax.set_title('Figure 4.1 — NexaLearn System Architecture (Clean Architecture Layers)',
             fontsize=14, fontweight='bold', pad=12)
plt.savefig(f'{OUT}/system_arch.png', dpi=DPI, bbox_inches='tight')
plt.savefig(f'{OUT}/system_arch.pdf', bbox_inches='tight')
plt.close()
print('system_arch.png/pdf')

# === Module Interaction (Figure 4.2) ===
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, 13)
ax.set_ylim(0, 8)
ax.axis('off')

modules_mi = [
    ('Auth', 2.0, 6.8, PALETTE['blue']),
    ('Courses', 4.5, 6.8, PALETTE['green']),
    ('Enrollment', 7.0, 6.8, PALETTE['orange']),
    ('Payments', 9.5, 6.8, PALETTE['orange']),
    ('Media', 2.0, 5.2, PALETTE['teal']),
    ('AI-Pipeline', 4.5, 5.2, PALETTE['teal']),
    ('Assessment', 7.0, 5.2, PALETTE['purple']),
    ('Discussion', 9.5, 5.2, PALETTE['red']),
    ('Progress', 2.0, 3.6, PALETTE['blue']),
    ('Reviews', 4.5, 3.6, PALETTE['purple']),
    ('Certificates', 7.0, 3.6, PALETTE['teal']),
    ('Search', 9.5, 3.6, PALETTE['blue']),
    ('Streak', 2.0, 2.0, PALETTE['orange']),
    ('Notifications', 4.5, 2.0, PALETTE['purple']),
    ('Instructor', 7.0, 2.0, PALETTE['green']),
]

mod_dict = {name: (x, y, c) for name, x, y, c in modules_mi}

edges_mi = [
    ('Auth', 'Enrollment', 'HTTP'), ('Auth', 'Courses', 'HTTP'),
    ('Enrollment', 'Payments', 'HTTP'), ('Enrollment', 'Progress', 'Event'),
    ('Courses', 'Media', 'HTTP'), ('Courses', 'AI-Pipeline', 'HTTP'),
    ('AI-Pipeline', 'Assessment', 'Event'), ('Assessment', 'Progress', 'Event'),
    ('Progress', 'Certificates', 'Event'), ('Progress', 'Streak', 'Event'),
    ('Discussion', 'Notifications', 'Event'), ('Reviews', 'Notifications', 'Event'),
    ('Payments', 'Enrollment', 'Event'), ('Media', 'AI-Pipeline', 'Event'),
    ('Assessment', 'Reviews', 'Event'), ('Enrollment', 'Certificates', 'Event'),
    ('Progress', 'Instructor', 'HTTP'), ('Discussion', 'Instructor', 'HTTP'),
    ('Search', 'Courses', 'HTTP'),
]

for src, dst, ptype in edges_mi:
    if src in mod_dict and dst in mod_dict:
        x1, y1, _ = mod_dict[src]
        x2, y2, _ = mod_dict[dst]
        color = PALETTE['blue'] if ptype == 'HTTP' else PALETTE['orange']
        ls = 'solid' if ptype == 'HTTP' else 'dashed'
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color=color, lw=2,
                                    connectionstyle='arc3,rad=0.15', linestyle=ls))
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2 + 0.3
        ax.text(mx, my, ptype, ha='center', va='bottom',
                fontsize=7, color=color, fontweight='bold')

for name, x, y, color in modules_mi:
    ax.text(x, y, name, fontsize=10, fontweight='bold', color='white',
            bbox=dict(boxstyle='round,pad=0.35', fc=color, ec='white', lw=1.2),
            ha='center', va='center')

legend_y = 7.6
ax.plot([0.5, 1.0], [legend_y, legend_y], color=PALETTE['blue'], lw=2)
ax.text(1.1, legend_y, 'HTTP/Method Call', ha='left', va='center', fontsize=9, color=PALETTE['dark'])
ax.plot([4.5, 5.0], [legend_y, legend_y], color=PALETTE['orange'], lw=2, ls='dashed')
ax.text(5.1, legend_y, 'Domain Event (Outbox)', ha='left', va='center', fontsize=9, color=PALETTE['dark'])

ax.set_title('Figure 4.2 — Module Interaction Diagram (Bounded Context Dependencies)',
             fontsize=14, fontweight='bold', pad=10)
plt.savefig(f'{OUT}/module_interaction.png', dpi=DPI, bbox_inches='tight')
plt.savefig(f'{OUT}/module_interaction.pdf', bbox_inches='tight')
plt.close()
print('module_interaction.png/pdf')

# === State Machines (Figures 4.3–4.10) ===

state_machine((9, 5), [
    ('CREATED', PALETTE['blue']), ('PENDING', PALETTE['orange']),
    ('SUCCEEDED', PALETTE['green']), ('FAILED', PALETTE['red']), ('REFUNDED', PALETTE['teal']),
], [
    ('CREATED', 'PENDING', 'checkout initiated'),
    ('PENDING', 'SUCCEEDED', 'webhook confirmed'),
    ('PENDING', 'FAILED', 'payment declined'),
    ('SUCCEEDED', 'REFUNDED', 'refund processed'),
], 'Payment Intent State Machine', 'payment_intent_statemachine.png', cols=3)

state_machine((10, 5), [
    ('AWAITING_UPLOAD', PALETTE['blue']), ('UPLOADED', PALETTE['orange']),
    ('TRANSCODING', PALETTE['purple']), ('READY', PALETTE['green']), ('FAILED', PALETTE['red']),
], [
    ('AWAITING_UPLOAD', 'UPLOADED', 'upload complete'),
    ('UPLOADED', 'TRANSCODING', 'asset created'),
    ('TRANSCODING', 'READY', 'asset ready'),
    ('AWAITING_UPLOAD', 'FAILED', 'upload error'),
    ('UPLOADED', 'FAILED', 'asset errored'),
    ('TRANSCODING', 'FAILED', 'asset errored'),
], 'Video Asset State Machine', 'video_asset_statemachine.png', cols=3)

state_machine((9, 5), [
    ('PENDING', PALETTE['orange']), ('ACTIVE', PALETTE['green']),
    ('CANCELLED', PALETTE['red']), ('REFUNDED', PALETTE['teal']),
], [
    ('PENDING', 'ACTIVE', 'payment confirmed'),
    ('PENDING', 'CANCELLED', 'user cancelled'),
    ('ACTIVE', 'CANCELLED', 'user cancelled'),
    ('ACTIVE', 'REFUNDED', 'refund processed'),
], 'Enrollment State Machine', 'enrollment_statemachine.png', cols=2)

state_machine((9, 5), [
    ('IN_PROGRESS', PALETTE['blue']), ('SUBMITTED', PALETTE['orange']),
    ('GRADED', PALETTE['green']), ('ABANDONED', PALETTE['red']),
], [
    ('IN_PROGRESS', 'SUBMITTED', 'learner submits'),
    ('SUBMITTED', 'GRADED', 'grading completed'),
    ('IN_PROGRESS', 'ABANDONED', 'learner abandons'),
], 'Quiz Attempt State Machine', 'quiz_attempt_statemachine.png', cols=2)

state_machine((10, 5), [
    ('ACTIVE', PALETTE['green']), ('REFRESHED', PALETTE['orange']),
    ('REVOKED', PALETTE['red']), ('EXPIRED', PALETTE['gray']),
], [
    ('ACTIVE', 'REFRESHED', 'refresh used'),
    ('ACTIVE', 'REVOKED', 'logout / reuse'),
    ('ACTIVE', 'EXPIRED', 'access TTL'),
    ('REFRESHED', 'ACTIVE', 'new tokens issued'),
    ('REFRESHED', 'REVOKED', 'reuse detected'),
], 'Auth Session State Machine', 'auth_session_statemachine.png', cols=2)

state_machine((9, 5), [
    ('QUEUED', PALETTE['blue']), ('PROCESSING', PALETTE['orange']),
    ('READY_FOR_REVIEW', PALETTE['green']), ('FAILED', PALETTE['red']),
], [
    ('QUEUED', 'PROCESSING', 'job dispatched'),
    ('PROCESSING', 'READY_FOR_REVIEW', 'AI response received'),
    ('PROCESSING', 'FAILED', 'AI error'),
    ('QUEUED', 'FAILED', 'dispatch error'),
], 'AI Generation Job State Machine', 'ai_job_statemachine.png', cols=2)

state_machine((8, 4), [
    ('OPEN', PALETTE['green']), ('RESOLVED', PALETTE['blue']),
    ('HIDDEN', PALETTE['gray']),
], [
    ('OPEN', 'RESOLVED', 'instructor marks resolved'),
    ('OPEN', 'HIDDEN', 'moderation hides'),
], 'Discussion Thread State Machine', 'discussion_statemachine.png', cols=3)

state_machine((9, 5), [
    ('DRAFT', PALETTE['orange']), ('UNDER_REVIEW', PALETTE['purple']),
    ('PUBLISHED', PALETTE['green']), ('ARCHIVED', PALETTE['gray']),
], [
    ('DRAFT', 'UNDER_REVIEW', 'submit for review'),
    ('UNDER_REVIEW', 'PUBLISHED', 'admin approves'),
    ('DRAFT', 'PUBLISHED', 'instructor publishes'),
    ('PUBLISHED', 'ARCHIVED', 'end of term'),
], 'Course Status Lifecycle', 'course_curriculum_statemachine.png', cols=2)

print('\nAll state machine diagrams generated.')
