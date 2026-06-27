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

def draw_sequence_diagram(fig, ax, lifelines, messages, title, filename):
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 9)
    ax.axis('off')

    for x, label, color in lifelines:
        ax.plot([x, x], [1.5, 8.0], color=color, lw=1.5, linestyle='--', alpha=0.5)
        rect = mpatches.FancyBboxPatch((x-0.8, 7.0), 1.6, 1.0,
                                        boxstyle="round,pad=0.08",
                                        facecolor=color, alpha=0.15, ec=color, lw=1.5)
        ax.add_patch(rect)
        ax.text(x, 7.5, label, ha='center', va='center', fontsize=8, fontweight='bold', color=color)

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

    ax.set_title(title, fontsize=13, fontweight='bold', pad=10)
    plt.tight_layout()
    plt.savefig(f'{OUT}/{filename}.png', dpi=DPI, bbox_inches='tight')
    plt.savefig(f'{OUT}/{filename}.pdf', bbox_inches='tight')
    print(f'{filename}.png/pdf')

# ============================================================
# Sequence 1: User Enrollment Flow (Paid)
# ============================================================
fig, ax = plt.subplots(figsize=(10, 7))
draw_sequence_diagram(fig, ax,
    lifelines=[
        (2.0, 'Learner\n(Client)', PALETTE['dark']),
        (4.5, 'Courses\nModule', PALETTE['green']),
        (6.5, 'Payment\nModule', PALETTE['orange']),
        (8.5, 'Enrollment\nModule', PALETTE['orange']),
        (10.5, 'Stripe /\nDatabase', '#D35400'),
    ],
    messages=[
        (6.5, 2.0, 4.5, 'GET /courses/{id}', 'right'),
        (6.3, 4.5, 2.0, '200 Course details', 'left'),
        (5.8, 2.0, 4.5, 'POST /enrollments { courseId }', 'right'),
        (5.5, 4.5, 10.5, 'Check course price → not free', 'right'),
        (5.2, 4.5, 2.0, '201 Created (PENDING)', 'left'),
        (4.7, 2.0, 8.5, 'POST /payments/create-intent', 'right'),
        (4.4, 8.5, 10.5, 'INSERT payment_intent (CREATED)', 'right'),
        (4.1, 10.5, 2.0, '201 { clientSecret }', 'left'),
        (3.6, 2.0, 6.5, 'Stripe Confirm Payment', 'right'),
        (3.3, 6.5, 10.5, 'UPDATE payment_intent → PENDING', 'right'),
        (2.8, 6.5, 8.5, 'Webhook: payment_intent.succeeded', 'right'),
        (2.5, 8.5, 10.5, 'UPDATE enrollment → ACTIVE', 'right'),
        (2.2, 8.5, 10.5, 'INSERT outbox: EnrollmentActivated', 'right'),
        (1.9, 10.5, 2.0, '200 Webhook acknowledged', 'left'),
        (1.6, 2.0, 4.5, 'GET /enrollments (polls)', 'right'),
        (1.3, 4.5, 2.0, '200 ACTIVE', 'left'),
    ],
    title='Sequence: Paid Enrollment Flow',
    filename='seq_enrollment_flow',
)
plt.close()

# ============================================================
# Sequence 2: AI Pipeline Flow (Upload → Transcript → Quiz)
# ============================================================
fig, ax = plt.subplots(figsize=(10, 7))
draw_sequence_diagram(fig, ax,
    lifelines=[
        (2.0, 'Instructor\n(Client)', PALETTE['dark']),
        (4.5, 'Media\nModule', PALETTE['teal']),
        (6.5, 'Mux\n(External)', '#2980B9'),
        (8.5, 'AI Pipeline\nModule', '#8E44AD'),
        (10.5, 'OpenAI /\nWhisper', '#D35400'),
    ],
    messages=[
        (6.5, 2.0, 4.5, 'POST /media/upload (file)', 'right'),
        (6.2, 4.5, 6.5, 'Mux Upload.create()', 'right'),
        (5.9, 6.5, 4.5, '200 { uploadUrl }', 'left'),
        (5.6, 4.5, 2.0, '201 { uploadUrl, assetId }', 'left'),
        (5.2, 2.0, 6.5, 'PUT file → Mux direct upload', 'right'),
        (4.8, 6.5, 4.5, 'Webhook: video.upload.asset_created', 'right'),
        (4.5, 4.5, 10.5, 'INSERT video_asset (UPLOADED)', 'right'),
        (4.2, 4.5, 8.5, 'VideoUploaded event', 'right'),
        (3.8, 8.5, 10.5, 'INSERT generation_job (QUEUED)', 'right'),
        (3.5, 8.5, 10.5, 'Dispatch to Whisper ASR', 'right'),
        (3.0, 10.5, 8.5, 'Callback: transcript ready', 'right'),
        (2.7, 8.5, 10.5, 'INSERT transcript (READY)', 'right'),
        (2.4, 8.5, 10.5, 'Dispatch to LLM (quiz gen)', 'right'),
        (1.9, 10.5, 8.5, 'Callback: quiz questions', 'right'),
        (1.6, 8.5, 10.5, 'INSERT questions (READY_FOR_REVIEW)', 'right'),
        (1.3, 8.5, 2.0, 'Notify instructor for review', 'left'),
    ],
    title='Sequence: AI Pipeline — Transcript & Quiz Generation',
    filename='seq_ai_pipeline',
)
plt.close()

# ============================================================
# Sequence 3: Video Streaming Flow (Upload → Transcode → Play)
# ============================================================
fig, ax = plt.subplots(figsize=(10, 7))
draw_sequence_diagram(fig, ax,
    lifelines=[
        (2.0, 'Instructor\n(Client)', PALETTE['dark']),
        (4.5, 'Media\nModule', PALETTE['teal']),
        (6.5, 'Mux\n(External)', '#2980B9'),
        (8.5, 'Auth /\nEnrollment', PALETTE['blue']),
        (10.5, 'Learner\n(Client)', PALETTE['dark']),
    ],
    messages=[
        (6.5, 2.0, 4.5, 'POST /media/upload', 'right'),
        (6.2, 4.5, 6.5, 'Mux Upload.create()', 'right'),
        (5.9, 6.5, 4.5, '200 { uploadUrl }', 'left'),
        (5.6, 4.5, 2.0, '201 AWAITING_UPLOAD', 'left'),
        (5.2, 2.0, 6.5, 'PUT file to uploadUrl', 'right'),
        (4.8, 6.5, 4.5, 'Webhook: video.upload.asset_created', 'right'),
        (4.5, 4.5, 10.5, 'State → UPLOADED → TRANSCODING', 'right'),
        (4.0, 6.5, 4.5, 'Webhook: video.asset.ready', 'right'),
        (3.7, 4.5, 10.5, 'State → READY, store playbackId', 'right'),
        (3.4, 4.5, 8.5, 'Publish VideoReady event', 'right'),
        (3.0, 10.5, 8.5, 'GET /lessons/{id} (auth check)', 'right'),
        (2.7, 8.5, 10.5, 'Verify enrollment → ACTIVE', 'right'),
        (2.4, 8.5, 10.5, 'Generate signed JWT playback URL', 'right'),
        (2.1, 10.5, 8.5, '200 { playbackUrl, token }', 'left'),
        (1.8, 10.5, 6.5, 'GET HLS .m3u8 + token', 'right'),
        (1.5, 6.5, 10.5, 'Stream HLS segments (CDN)', 'left'),
    ],
    title='Sequence: Video Upload, Transcoding & Playback',
    filename='seq_video_streaming',
)
plt.close()
