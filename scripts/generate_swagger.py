import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.style.use('seaborn-v0_8-whitegrid')

PALETTE = {
    'blue': '#2E86AB', 'purple': '#A23B72', 'orange': '#F18F01',
    'green': '#43AA8B', 'teal': '#577590', 'red': '#D62828',
    'dark': '#333333', 'gray': '#888888', 'light_gray': '#CCCCCC',
}

OUT = '/Users/youssefbahy/Documents/Training/NexaLearnFullProject/newbook/images'
DPI = 300

fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 12)
ax.axis('off')

# Background
bg = mpatches.FancyBboxPatch((0.3, 0.3), 9.4, 11.4, boxstyle="round,pad=0.1",
                              facecolor='#F5F5F5', ec=PALETTE['light_gray'], lw=1.5)
ax.add_patch(bg)

# Header bar
header = mpatches.FancyBboxPatch((0.3, 10.8), 9.4, 0.9, boxstyle="round,pad=0.08",
                                  facecolor=PALETTE['dark'], ec=PALETTE['dark'], lw=0)
ax.add_patch(header)
ax.text(5.0, 11.25, 'Swagger UI — NexaLearn API', ha='center', va='center',
        fontsize=14, fontweight='bold', color='white')
ax.text(0.8, 11.25, '/api/docs', ha='left', va='center', fontsize=9, color='#AAAAAA')

# Helper: draw an API endpoint row
def api_row(y, method, path, summary, tag_color, has_auth=True):
    # Tag badge
    tag = mpatches.FancyBboxPatch((0.6, y-0.2), 1.5, 0.4, boxstyle="round,pad=0.05",
                                   facecolor=tag_color, ec=tag_color, lw=0)
    ax.add_patch(tag)
    ax.text(1.35, y, tag.get_label(), ha='center', va='center', fontsize=5, fontweight='bold', color='white')

    # Method badge
    method_colors = {'GET': '#27AE60', 'POST': '#2980B9', 'PATCH': '#F39C12', 'DELETE': '#E74C3C'}
    mc = method_colors.get(method, PALETTE['gray'])
    method_bg = mpatches.FancyBboxPatch((2.3, y-0.18), 0.7, 0.36, boxstyle="round,pad=0.03",
                                         facecolor=mc, ec=mc, lw=0)
    ax.add_patch(method_bg)
    ax.text(2.65, y, method, ha='center', va='center', fontsize=5.5, fontweight='bold', color='white')

    # Path
    ax.text(3.2, y, path, ha='left', va='center', fontsize=6, fontfamily='monospace', color=PALETTE['dark'])

    # Summary
    ax.text(8.2, y, summary, ha='right', va='center', fontsize=5.5, color=PALETTE['gray'], style='italic')

    # Lock icon for auth
    if has_auth and method != 'GET':
        ax.text(9.2, y, '[AUTH]', ha='center', va='center', fontsize=5, color='#E74C3C', fontweight='bold')

# Tag colors
tag_colors = ['#2E86AB', '#A23B72', '#F18F01', '#43AA8B', '#577590', '#D62828', '#8E44AD', '#1ABC9C']

# Auth endpoints
y = 10.3
ax.text(0.8, y, 'Auth Module', fontsize=9, fontweight='bold', color=tag_colors[0])
y -= 0.4
for m, p, s in [('POST','/auth/register','Register new user'),('POST','/auth/login','Login'),
                 ('POST','/auth/refresh','Refresh tokens'),('POST','/auth/verify-email','Verify email'),
                 ('POST','/auth/logout','Logout')]:
    api_row(y, m, p, s, tag_colors[0], has_auth=(m != 'POST'))
    y -= 0.4

# Course endpoints
y -= 0.1
ax.text(0.8, y, 'Course Module', fontsize=9, fontweight='bold', color=tag_colors[1])
y -= 0.4
for m, p, s in [('GET','/courses','List published courses'),('GET','/courses/{id}','Get course details'),
                 ('POST','/courses','Create course'),('PATCH','/courses/{id}','Update course')]:
    api_row(y, m, p, s, tag_colors[1], has_auth=(m != 'GET'))
    y -= 0.4

# Enrollment endpoints
y -= 0.1
ax.text(0.8, y, 'Enrollment Module', fontsize=9, fontweight='bold', color=tag_colors[2])
y -= 0.4
for m, p, s in [('POST','/enrollments','Enroll in course'),('GET','/enrollments','List enrollments'),
                 ('GET','/enrollments/{id}','Get enrollment')]:
    api_row(y, m, p, s, tag_colors[2])
    y -= 0.4

# Payment endpoints
y -= 0.1
ax.text(0.8, y, 'Payment Module', fontsize=9, fontweight='bold', color=tag_colors[3])
y -= 0.4
for m, p, s in [('POST','/payments/create-intent','Create payment intent'),
                 ('GET','/payments/intents','List intents'),
                 ('POST','/webhooks/stripe','Stripe webhook')]:
    api_row(y, m, p, s, tag_colors[3], has_auth=(m != 'POST'))
    y -= 0.4

# Media endpoints
y -= 0.1
ax.text(0.8, y, 'Media Module', fontsize=9, fontweight='bold', color=tag_colors[4])
y -= 0.4
for m, p, s in [('POST','/media/upload','Request upload URL'),
                 ('GET','/media/assets/{id}','Get asset status')]:
    api_row(y, m, p, s, tag_colors[4])
    y -= 0.4

# AI Pipeline
y -= 0.1
ax.text(0.8, y, 'AI Pipeline', fontsize=9, fontweight='bold', color=tag_colors[5])
y -= 0.4
for m, p, s in [('POST','/media/upload?generateQuiz=true','Upload + generate quiz'),
                 ('GET','/ai/jobs/{id}','Check generation status')]:
    api_row(y, m, p, s, tag_colors[5])
    y -= 0.4

# Assessment
y -= 0.1
ax.text(0.8, y, 'Assessment Module', fontsize=9, fontweight='bold', color=tag_colors[6])
y -= 0.4
for m, p, s in [('GET','/quizzes/{id}','Get quiz'),
                 ('POST','/quizzes/{id}/attempts','Submit attempt'),
                 ('GET','/attempts/{id}','Get graded result'),
                 ('POST','/quizzes/{id}/publish','Publish quiz')]:
    api_row(y, m, p, s, tag_colors[6])
    y -= 0.4

# Discussion
y -= 0.1
ax.text(0.8, y, 'Discussion', fontsize=9, fontweight='bold', color=tag_colors[7])
y -= 0.4
for m, p, s in [('POST','/courses/{id}/discussions','Create thread'),
                 ('POST','/discussions/{id}/replies','Post reply'),
                 ('PATCH','/discussions/{id}/resolve','Resolve thread')]:
    api_row(y, m, p, s, tag_colors[7])
    y -= 0.4

# Legend
ax.text(0.8, 0.5, '[AUTH] = Requires authentication  |  Swagger UI: http://localhost:3000/api/docs',
        ha='left', va='center', fontsize=7, color=PALETTE['gray'])

ax.set_title('', fontsize=1)  # dummy to override style
plt.savefig(f'{OUT}/swagger_mockup.png', dpi=DPI, bbox_inches='tight')
plt.savefig(f'{OUT}/swagger_mockup.pdf', bbox_inches='tight')
plt.close()
print('swagger_mockup.png/pdf generated.')
