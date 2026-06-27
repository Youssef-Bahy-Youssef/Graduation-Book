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
SM = f'{OUT}/statemachines'

def state_machine(ax, states, transitions, title, filename):
    ax.clear()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')
    positions = {}
    cols = 3
    for i, (name, color) in enumerate(states):
        row, col = divmod(i, cols)
        x = 1.5 + col * 3.5
        y = 5 - row * 2.0
        positions[name] = (x, y)
        circle = mpatches.FancyBboxPatch((x-0.9, y-0.35), 1.8, 0.7, boxstyle="round,pad=0.1",
                                          color=color, alpha=0.15, ec=color, lw=2)
        ax.add_patch(circle)
        ax.text(x, y, name, ha='center', va='center', fontsize=8, fontweight='bold', color=color)
    for src, dst, label in transitions:
        if src in positions and dst in positions:
            x1, y1 = positions[src]
            x2, y2 = positions[dst]
            ax.annotate('', xy=(x2, y2-0.35), xytext=(x1, y1+0.35),
                        arrowprops=dict(arrowstyle='->', color='#666666', lw=1.2, connectionstyle='arc3,rad=0.2'))
            mx, my = (x1+x2)/2, (y1+y2)/2 + 0.3
            ax.text(mx, my, label, ha='center', va='bottom', fontsize=6.5, color='#555555',
                    style='italic')
    ax.set_title(title, fontsize=10, fontweight='bold', pad=8)
    plt.savefig(f'{SM}/{filename}', dpi=180, bbox_inches='tight')

# === System Architecture ===
fig, ax = plt.subplots(figsize=(10, 7))
ax.set_xlim(0, 12)
ax.set_ylim(0, 8)
ax.axis('off')

layers = [
    (0.5, 6.8, 11, 1.0, '#E8F4F8', '#2E86AB', 'Presentation Layer (NestJS Controllers, Guards, Interceptors)'),
    (0.5, 5.3, 11, 1.2, '#F0E6F6', '#A23B72', 'Application Layer (Use Cases / Interactors)'),
    (0.5, 1.5, 5.0, 3.5, '#FFF3E0', '#F18F01', 'Domain Layer (Entities, Aggregates, Value Objects, Domain Events, Repository Ports)'),
    (6.0, 1.5, 5.5, 3.5, '#E8F5E9', '#43AA8B', 'Infrastructure Layer (Prisma, Stripe SDK, Mux API, Redis, Outbox Publisher)'),
    (0.5, 0.2, 11, 1.0, '#F5F5F5', '#888888', 'External Integrations (PostgreSQL, Redis, Stripe, Mux, OpenAI, SendGrid, S3)'),
]

for x, y, w, h, fc, ec, label in layers:
    rect = mpatches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1", color=fc, ec=ec, lw=2)
    ax.add_patch(rect)
    ax.text(x + w/2, y + h/2, label, ha='center', va='center', fontsize=11, fontweight='bold', color=ec)

modules = ['Auth', 'Courses', 'Enrollment', 'Payments', 'Media', 'AI-Pipeline', 'Assessment', 'Discussion', 'Progress', 'Reviews', 'Certificates', 'Search', 'Streak', 'Notifications', 'Instructor']
x_start, y_start = 0.8, 2.8
for i, mod in enumerate(modules):
    col = i % 5
    row = i // 5
    x = 0.8 + col * 2.2
    y = 2.8 - row * 1.0
    ax.text(x + 0.1, y, mod, fontsize=6, color='#333333', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='#999999', lw=0.8))

ax.set_title('Figure 4.1 — NexaLearn System Architecture (Clean Architecture Layers)', fontsize=13, fontweight='bold', pad=10)
plt.savefig(f'{OUT}/system_arch.png', dpi=180, bbox_inches='tight')
plt.close()
print('✓ system_arch.png')

# === Module Interaction ===
fig, ax = plt.subplots(figsize=(10, 7))
ax.set_xlim(0, 12)
ax.set_ylim(0, 7)
ax.axis('off')

mod_pos = {
    'Auth': (1, 6), 'Courses': (3, 6), 'Enrollment': (5, 6), 'Payments': (7, 6), 'Media': (9, 6),
    'AI-Pl.': (1, 4.2), 'Assess.': (3, 4.2), 'Discuss.': (5, 4.2), 'Progress': (7, 4.2), 'Reviews': (9, 4.2),
    'Certif.': (1, 2.5), 'Search': (3, 2.5), 'Streak': (5, 2.5), 'Notif.': (7, 2.5), 'Instructor': (9, 2.5),
}
colors = ['#2E86AB','#A23B72','#F18F01','#43AA8B','#577590','#D62828','#2E86AB','#A23B72','#F18F01','#43AA8B',
          '#577590','#D62828','#2E86AB','#A23B72','#F18F01']

edges = [('Auth','Enrollment'),('Auth','Courses'),('Enrollment','Payments'),('Enrollment','Progress'),
         ('Courses','Media'),('Courses','AI-Pl.'),('AI-Pl.','Assess.'),('Assess.','Progress'),
         ('Progress','Certif.'),('Progress','Streak'),('Discuss.','Notif.'),('Reviews','Notif.'),
         ('Payments','Enrollment'),('Media','AI-Pl.'),('Assess.','Reviews'),('Enrollment','Certif.'),
         ('Progress','Instructor'),('Discuss.','Instructor'),('Search','Courses')]

for src, dst in edges:
    if src in mod_pos and dst in mod_pos:
        x1, y1 = mod_pos[src]
        x2, y2 = mod_pos[dst]
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color='#BBBBBB', lw=1.5, connectionstyle='arc3,rad=0.15'))

used = {}
for i, (mod, (x, y)) in enumerate(mod_pos.items()):
    c = colors[i % len(colors)]
    ax.scatter(x, y, color=c, s=400, zorder=5, edgecolors='white', linewidth=1.5)
    ax.text(x, y, mod, ha='center', va='center', fontsize=7, fontweight='bold', color='white', zorder=6)

ax.set_title('Figure 4.2 — Module Interaction Diagram', fontsize=13, fontweight='bold', pad=10)
plt.savefig(f'{OUT}/module_interaction.png', dpi=180, bbox_inches='tight')
plt.close()
print('✓ module_interaction.png')

# === Payment Intent State Machine ===
fig, ax = plt.subplots(figsize=(7, 4))
states = [('CREATED','#2E86AB'),('PROCESSING','#F18F01'),('SUCCEEDED','#43AA8B'),('FAILED','#D62828'),('REFUNDED','#577590')]
transitions = [('CREATED','PROCESSING','checkout initiated'),('PROCESSING','SUCCEEDED','webhook confirmed'),('PROCESSING','FAILED','payment declined'),('SUCCEEDED','REFUNDED','refund processed')]
state_machine(ax, states, transitions, 'Payment Intent State Machine', 'payment_intent_statemachine.png')

# === Video Asset State Machine ===
fig, ax = plt.subplots(figsize=(8, 4))
states = [('AWAITING_UPLOAD','#2E86AB'),('UPLOADING','#F18F01'),('TRANSCODING','#A23B72'),('READY','#43AA8B'),('ERROR','#D62828')]
transitions = [('AWAITING_UPLOAD','UPLOADING','upload URL created'),('UPLOADING','TRANSCODING','upload complete'),('TRANSCODING','READY','asset.ready'),('TRANSCODING','ERROR','asset.errored')]
state_machine(ax, states, transitions, 'Video Asset State Machine', 'video_asset_statemachine.png')

# === Enrollment State Machine ===
fig, ax = plt.subplots(figsize=(7, 4))
states = [('PENDING','#F18F01'),('ACTIVE','#43AA8B'),('COMPLETED','#2E86AB'),('CANCELLED','#D62828'),('EXPIRED','#888888')]
transitions = [('PENDING','ACTIVE','payment confirmed'),('PENDING','CANCELLED','user cancelled'),('ACTIVE','COMPLETED','all lessons done'),('ACTIVE','EXPIRED','time limit passed')]
state_machine(ax, states, transitions, 'Enrollment State Machine', 'enrollment_statemachine.png')

# === Quiz Attempt State Machine ===
fig, ax = plt.subplots(figsize=(7, 4))
states = [('IN_PROGRESS','#2E86AB'),('SUBMITTED','#F18F01'),('GRADING','#A23B72'),('COMPLETED','#43AA8B'),('TIMEOUT','#D62828')]
transitions = [('IN_PROGRESS','SUBMITTED','learner submits'),('SUBMITTED','GRADING','needs short-answer grading'),('GRADING','COMPLETED','AI grades'),('SUBMITTED','COMPLETED','auto-graded'),('IN_PROGRESS','TIMEOUT','time limit reached')]
state_machine(ax, states, transitions, 'Quiz Attempt State Machine', 'quiz_attempt_statemachine.png')

# === Auth Session State Machine ===
fig, ax = plt.subplots(figsize=(6, 3))
states = [('ACTIVE','#43AA8B'),('REFRESHED','#F18F01'),('REVOKED','#D62828'),('EXPIRED','#888888')]
transitions = [('ACTIVE','REFRESHED','refresh used'),('ACTIVE','REVOKED','logout / reuse'),('ACTIVE','EXPIRED','access TTL'),('REFRESHED','ACTIVE','new tokens issued'),('REFRESHED','REVOKED','reuse detected')]
state_machine(ax, states, transitions, 'Auth Session State Machine', 'auth_session_statemachine.png')

# === AI Generation Job State Machine ===
fig, ax = plt.subplots(figsize=(8, 4))
states = [('PENDING','#2E86AB'),('PROCESSING','#F18F01'),('COMPLETED','#43AA8B'),('FAILED','#D62828'),('CALLBACK_RECEIVED','#A23B72')]
transitions = [('PENDING','PROCESSING','job dispatched'),('PROCESSING','CALLBACK_RECEIVED','AI response received'),('CALLBACK_RECEIVED','COMPLETED','HMAC verified + persisted'),('PROCESSING','FAILED','AI error')]
state_machine(ax, states, transitions, 'AI Generation Job State Machine', 'ai_job_statemachine.png')

# === Discussion Thread State Machine ===
fig, ax = plt.subplots(figsize=(6, 3))
states = [('OPEN','#43AA8B'),('RESOLVED','#2E86AB'),('CLOSED','#888888')]
transitions = [('OPEN','RESOLVED','instructor marks resolved'),('OPEN','CLOSED','archived'),('RESOLVED','OPEN','re-opened')]
state_machine(ax, states, transitions, 'Discussion Thread State Machine', 'discussion_statemachine.png')

# === Course Curriculum Lifecycle ===
fig, ax = plt.subplots(figsize=(7, 3))
states = [('DRAFT','#F18F01'),('PUBLISHED','#43AA8B'),('ARCHIVED','#888888')]
transitions = [('DRAFT','PUBLISHED','instructor publishes'),('PUBLISHED','ARCHIVED','end of term'),('ARCHIVED','PUBLISHED','re-published')]
state_machine(ax, states, transitions, 'Course Status Lifecycle', 'course_curriculum_statemachine.png')

print('\nAll state machine diagrams generated.')
