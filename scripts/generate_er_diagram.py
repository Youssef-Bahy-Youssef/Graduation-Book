import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.style.use('seaborn-v0_8-whitegrid')

PALETTE = {
    'blue': '#2E86AB', 'purple': '#A23B72', 'orange': '#F18F01',
    'green': '#43AA8B', 'teal': '#577590', 'red': '#D62828',
    'dark': '#333333', 'gray': '#888888', 'light_gray': '#CCCCCC',
}

OUT = '/Users/youssefbahy/Documents/Training/NexaLearnFullProject/newbook/images'
DPI = 300

fig, ax = plt.subplots(figsize=(15, 10))
ax.set_xlim(0, 16)
ax.set_ylim(0, 11)
ax.axis('off')

ctx_colors = {
    'auth': PALETTE['blue'], 'course': PALETTE['green'],
    'enroll': PALETTE['orange'], 'assessment': PALETTE['purple'],
    'discussion': PALETTE['red'], 'media': PALETTE['teal'],
    'review': '#7B68EE',
}

entities = [
    ('User', 7.5, 9.0, ctx_colors['auth']),
    ('Role', 11.5, 9.0, ctx_colors['auth']),
    ('Session', 3.5, 9.0, ctx_colors['auth']),

    ('Course', 7.5, 6.8, ctx_colors['course']),
    ('Module', 12.0, 6.8, ctx_colors['course']),
    ('Lesson', 1.0, 6.8, ctx_colors['course']),

    ('Quiz', 11.0, 4.5, ctx_colors['assessment']),
    ('Question', 13.5, 2.5, ctx_colors['assessment']),
    ('QOption', 13.5, 4.5, ctx_colors['assessment']),
    ('QuizAttempt', 7.5, 2.5, ctx_colors['assessment']),
    ('AttemptAnswer', 10.0, 0.5, ctx_colors['assessment']),

    ('Enrollment', 4.0, 4.5, ctx_colors['enroll']),
    ('PaymentIntent', 1.0, 4.5, ctx_colors['enroll']),
    ('Certificate', 7.5, 4.5, ctx_colors['enroll']),

    ('VideoAsset', 4.0, 6.8, ctx_colors['media']),
    ('GenerationJob', 1.0, 2.5, ctx_colors['media']),

    ('DiscussionThread', 4.0, 2.5, ctx_colors['discussion']),
    ('DiscussionPost', 1.0, 0.5, ctx_colors['discussion']),

    ('Review', 10.0, 2.5, '#7B68EE'),
]

for name, x, y, color in entities:
    rect = mpatches.FancyBboxPatch((x - 1.1, y - 0.35), 2.2, 0.7,
                                    boxstyle="round,pad=0.08",
                                    facecolor=color, alpha=0.12, ec=color, lw=2.5)
    ax.add_patch(rect)
    ax.text(x, y, name, ha='center', va='center',
            fontsize=10, fontweight='bold', color=color)

rels = [
    ('User', 'Role', '1', '*', ctx_colors['auth']),
    ('User', 'Session', '1', '*', ctx_colors['auth']),
    ('User', 'Course', '1', '*', ctx_colors['course']),
    ('User', 'Enrollment', '1', '*', ctx_colors['enroll']),
    ('User', 'PaymentIntent', '1', '*', ctx_colors['enroll']),
    ('User', 'QuizAttempt', '1', '*', ctx_colors['assessment']),
    ('User', 'DiscussionThread', '1', '*', ctx_colors['discussion']),
    ('User', 'DiscussionPost', '1', '*', ctx_colors['discussion']),
    ('User', 'Review', '1', '*', '#7B68EE'),
    ('Course', 'Module', '1', '*', ctx_colors['course']),
    ('Course', 'Enrollment', '1', '*', ctx_colors['enroll']),
    ('Course', 'PaymentIntent', '1', '*', ctx_colors['enroll']),
    ('Course', 'Review', '1', '*', '#7B68EE'),
    ('Module', 'Lesson', '1', '*', ctx_colors['course']),
    ('Lesson', 'Quiz', '1', '1', ctx_colors['course']),
    ('Lesson', 'VideoAsset', '1', '1', ctx_colors['media']),
    ('Lesson', 'GenerationJob', '1', '*', ctx_colors['media']),
    ('Quiz', 'Question', '1', '*', ctx_colors['assessment']),
    ('Quiz', 'QuizAttempt', '1', '*', ctx_colors['assessment']),
    ('Question', 'QOption', '1', '*', ctx_colors['assessment']),
    ('Question', 'AttemptAnswer', '1', '*', ctx_colors['assessment']),
    ('QuizAttempt', 'AttemptAnswer', '1', '*', ctx_colors['assessment']),
    ('Enrollment', 'PaymentIntent', '1', '1', ctx_colors['enroll']),
    ('Enrollment', 'Certificate', '1', '1', ctx_colors['enroll']),
    ('DiscussionThread', 'DiscussionPost', '1', '*', ctx_colors['discussion']),
    ('GenerationJob', 'Quiz', '1', '1', ctx_colors['media']),
]

entity_positions = {name: (x, y) for name, x, y, _ in entities}

for src, dst, card1, card2, color in rels:
    if src not in entity_positions or dst not in entity_positions:
        continue
    x1, y1 = entity_positions[src]
    x2, y2 = entity_positions[dst]
    dx, dy = x2 - x1, y2 - y1
    rad = 0.2
    if abs(dx) < 0.1:
        rad = 0.3
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=1.5,
                                connectionstyle=f'arc3,rad={rad}',
                                linestyle='dashed' if abs(rad) > 0.25 else 'solid'))
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    off = 0.15
    ax.text(x1 + dx * 0.1 + off, y1 + dy * 0.1 + off, card1,
            fontsize=8, fontweight='bold', color=color, ha='center', va='center')
    ax.text(x2 - dx * 0.1 + off, y2 - dy * 0.1 + off, card2,
            fontsize=8, fontweight='bold', color=color, ha='center', va='center')

legend_entries = [
    ('Auth / Identity', ctx_colors['auth']),
    ('Course Content', ctx_colors['course']),
    ('Enrollment / Payments', ctx_colors['enroll']),
    ('Assessment', ctx_colors['assessment']),
    ('Discussion', ctx_colors['discussion']),
    ('Media / AI Pipeline', ctx_colors['media']),
    ('Reviews', '#7B68EE'),
]
for i, (label, color) in enumerate(legend_entries):
    x = 1.0 + i * 2.1
    ax.plot(x, 10.5, 'o', color=color, markersize=10, markeredgecolor='white', markeredgewidth=1)
    ax.text(x, 10.5, label, ha='center', va='bottom', fontsize=7.5, color=PALETTE['dark'], fontweight='bold')

ax.set_title('Figure 4.x — Entity-Relationship Diagram (Core Domain)',
             fontsize=14, fontweight='bold', pad=15)
plt.tight_layout()
plt.savefig(f'{OUT}/er_diagram.png', dpi=DPI, bbox_inches='tight')
plt.savefig(f'{OUT}/er_diagram.pdf', bbox_inches='tight')
plt.close()
print('er_diagram.png/pdf')
