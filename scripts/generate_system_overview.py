import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines

plt.style.use('seaborn-v0_8-whitegrid')

PALETTE = {
    'blue': '#2E86AB', 'purple': '#A23B72', 'orange': '#F18F01',
    'green': '#43AA8B', 'teal': '#577590', 'red': '#D62828',
    'dark': '#333333', 'gray': '#888888', 'light_gray': '#CCCCCC',
}

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 11,
    'axes.facecolor': 'white',
    'figure.facecolor': 'white',
    'axes.edgecolor': PALETTE['light_gray'],
})

OUT = '/Users/youssefbahy/Documents/Training/NexaLearnFullProject/newbook/images'
DPI = 300

fig, ax = plt.subplots(figsize=(17, 10))
ax.set_xlim(0, 18)
ax.set_ylim(0, 10)
ax.axis('off')

# ─── ZONE BACKGROUNDS ───
zones = [
    (0.1, 0.25, 4.2, 9.5, '#F4F7FB', PALETTE['blue'], 'CLIENTS'),
    (4.8, 0.25, 8.4, 9.5, '#F7FBF7', PALETTE['green'], 'NEXALEARN MODULAR MONOLITH'),
    (13.7, 0.25, 4.2, 9.5, '#F8F5F0', PALETTE['gray'], 'EXTERNAL SERVICES'),
]
for zx, zy, zw, zh, zbg, zc, ztitle in zones:
    r = mpatches.FancyBboxPatch((zx, zy), zw, zh, boxstyle="round,pad=0.2",
                                 facecolor=zbg, ec=zc, lw=2, zorder=0)
    ax.add_patch(r)
    zcx = zx + zw / 2
    ax.plot([zcx - 1.2, zcx + 1.2], [zy + zh - 0.2, zy + zh - 0.2],
            color=zc, lw=2.5, zorder=1)
    ax.text(zcx, zy + zh - 0.45, ztitle, ha='center', va='top',
            fontsize=11, fontweight='bold', color=zc, zorder=1)

# ─── LEFT: CLIENTS ───
clients = [
    ('Web App', 'React SPA', 2.2, 7.6, PALETTE['blue']),
    ('Mobile App', 'React Native', 2.2, 5.6, PALETTE['teal']),
    ('Admin Dashboard', 'React SPA', 2.2, 3.6, PALETTE['purple']),
]
for ct, cs, cx, cy, cc in clients:
    r = mpatches.FancyBboxPatch((cx - 1.6, cy - 0.7), 3.2, 1.4,
                                 boxstyle="round,pad=0.12",
                                 facecolor='white', ec=cc, lw=2)
    ax.add_patch(r)
    ax.text(cx, cy + 0.12, ct, ha='center', va='center',
            fontsize=11, fontweight='bold', color=cc)
    ax.text(cx, cy - 0.35, cs, ha='center', va='center',
            fontsize=8, color=PALETTE['gray'])

# ─── CENTER: BACKEND ───
# API Gateway
gw_x, gw_y, gw_w, gw_h = 5.2, 7.8, 7.6, 0.8
gw_r = mpatches.FancyBboxPatch((gw_x, gw_y), gw_w, gw_h,
                                boxstyle="round,pad=0.08",
                                facecolor='#E8F5E9', ec=PALETTE['green'], lw=1.8)
ax.add_patch(gw_r)
ax.text(9.0, gw_y + gw_h - 0.2, 'REST API Gateway', ha='center', va='center',
        fontsize=10, fontweight='bold', color=PALETTE['green'])
ax.text(9.0, gw_y + 0.18, 'Controllers  ·  Guards  ·  Pipes  ·  DTO Validation',
        ha='center', va='center', fontsize=7.5, color=PALETTE['gray'])

# Modules area label
ax.text(9.0, 7.15, 'BOUNDED CONTEXTS', ha='center', va='center',
        fontsize=9, fontweight='bold', color=PALETTE['gray'])

# 2x6 grid of modules under the label
mods = [
    ('Auth', 5.6, 6.4, PALETTE['blue']),
    ('Courses', 7.2, 6.4, PALETTE['green']),
    ('Payments', 8.8, 6.4, PALETTE['orange']),
    ('Enrollment', 10.4, 6.4, PALETTE['orange']),
    ('Media', 5.6, 5.3, PALETTE['teal']),
    ('AI Pipeline', 7.2, 5.3, PALETTE['teal']),
    ('Assessment', 8.8, 5.3, PALETTE['purple']),
    ('Discussion', 10.4, 5.3, PALETTE['red']),
    ('Progress', 5.6, 4.2, PALETTE['blue']),
    ('Reviews', 7.2, 4.2, PALETTE['purple']),
    ('Certificates', 8.8, 4.2, PALETTE['teal']),
    ('Notifications', 10.4, 4.2, PALETTE['purple']),
]
for mn, mx, my, mc in mods:
    r = mpatches.FancyBboxPatch((mx - 0.7, my - 0.3), 1.4, 0.6,
                                 boxstyle="round,pad=0.08",
                                 facecolor=mc, ec='white', lw=1)
    ax.add_patch(r)
    ax.text(mx, my, mn, ha='center', va='center',
            fontsize=8.5, fontweight='bold', color='white')

# Extra smaller modules
extra_mods = [
    ('Search', 5.6, 3.3, PALETTE['blue']),
    ('Streak', 7.2, 3.3, PALETTE['orange']),
    ('Instructor', 8.8, 3.3, PALETTE['green']),
]
for en, ex, ey, ec in extra_mods:
    r = mpatches.FancyBboxPatch((ex - 0.55, ey - 0.22), 1.1, 0.44,
                                 boxstyle="round,pad=0.06",
                                 facecolor='white', ec=ec, lw=1.2)
    ax.add_patch(r)
    ax.text(ex, ey, en, ha='center', va='center',
            fontsize=7.5, fontweight='bold', color=ec)

# Infrastructure
infra_x, infra_y, infra_w, infra_h = 5.2, 2.0, 7.6, 0.9
infra_r = mpatches.FancyBboxPatch((infra_x, infra_y), infra_w, infra_h,
                                   boxstyle="round,pad=0.1",
                                   facecolor='#FFF8E1', ec=PALETTE['orange'], lw=1.8)
ax.add_patch(infra_r)
ax.text(9.0, infra_y + infra_h - 0.2, 'INFRASTRUCTURE', ha='center', va='center',
        fontsize=9, fontweight='bold', color=PALETTE['orange'])
ax.text(9.0, infra_y + 0.18, 'Transactional Outbox  ·  Domain Event Bus  ·  CQRS  ·  Prisma ORM',
        ha='center', va='center', fontsize=7.5, color=PALETTE['dark'])

# Database and Cache
db_items = [
    ('PostgreSQL', 'Primary Database', 5.2, 0.7, 3.4, 0.7, PALETTE['purple'], '#EDE7F6'),
    ('Redis', 'Sessions  ·  Cache  ·  Rate Limits', 9.4, 0.7, 3.4, 0.7, PALETTE['purple'], '#F3E5F5'),
]
for dn, dd, dx, dy, dw, dh, dc, dbg in db_items:
    r = mpatches.FancyBboxPatch((dx, dy), dw, dh, boxstyle="round,pad=0.08",
                                 facecolor=dbg, ec=dc, lw=1.5)
    ax.add_patch(r)
    ax.text(dx + dw / 2, dy + dh / 2 + 0.05, dn, ha='center', va='center',
            fontsize=9, fontweight='bold', color=dc)
    ax.text(dx + dw / 2, dy + dh / 2 - 0.3, dd, ha='center', va='center',
            fontsize=6.5, color=PALETTE['gray'])

# ─── RIGHT: EXTERNAL ───
exts = [
    ('Stripe', 'Payment Processing', 15.8, 7.6, '#E3F2FD', PALETTE['blue']),
    ('Mux', 'Video Transcoding', 15.8, 5.6, '#FFEBEE', PALETTE['red']),
    ('AI Workers', 'Whisper  ·  GPT / LLM', 15.8, 3.6, '#FFF3E0', PALETTE['orange']),
]
for et, es, ex, ey, ebg, ec in exts:
    r = mpatches.FancyBboxPatch((ex - 1.7, ey - 0.7), 3.4, 1.4,
                                 boxstyle="round,pad=0.12",
                                 facecolor='white', ec=ec, lw=2)
    ax.add_patch(r)
    ax.text(ex, ey + 0.12, et, ha='center', va='center',
            fontsize=11, fontweight='bold', color=ec)
    ax.text(ex, ey - 0.35, es, ha='center', va='center',
            fontsize=8, color=PALETTE['gray'])

# Smaller row
smalls = [
    ('Resend', 'Email', 15.0, 1.2, 1.5, 0.7, PALETTE['green'], '#E8F5E9'),
    ('AWS S3', 'Assets', 16.6, 1.2, 1.5, 0.7, PALETTE['red'], '#FFEBEE'),
]
for sn, sd, sx, sy, sw, sh, sc, sbg in smalls:
    r = mpatches.FancyBboxPatch((sx, sy), sw, sh, boxstyle="round,pad=0.08",
                                 facecolor='white', ec=sc, lw=1.5)
    ax.add_patch(r)
    ax.text(sx + sw / 2, sy + sh / 2 + 0.05, sn, ha='center', va='center',
            fontsize=9, fontweight='bold', color=sc)
    ax.text(sx + sw / 2, sy + sh / 2 - 0.3, sd, ha='center', va='center',
            fontsize=6, color=PALETTE['gray'])

# ─── ARROWS ───
# Clients → Backend (bidirectional)
for ay in [7.6, 5.6, 3.6]:
    ax.annotate('', xy=(4.7, ay), xytext=(3.8, ay),
                arrowprops=dict(arrowstyle='->', color=PALETTE['blue'], lw=2.5))
    ax.annotate('', xy=(3.8, ay - 0.35), xytext=(4.7, ay - 0.35),
                arrowprops=dict(arrowstyle='->', color=PALETTE['blue'], lw=1.5))

ax.text(4.25, 9.1, 'HTTP / JSON', ha='center', va='center',
        fontsize=8, fontweight='bold', color=PALETTE['blue'],
        bbox=dict(boxstyle='round,pad=0.15', fc='white', ec=PALETTE['blue'], lw=0.5))

# Backend → External
for ay in [7.6, 5.6, 3.6]:
    ax.annotate('', xy=(13.3, ay), xytext=(12.8, ay),
                arrowprops=dict(arrowstyle='->', color=PALETTE['gray'], lw=2,
                                connectionstyle='arc3,rad=0.05'))

ax.text(13.05, 9.1, 'HTTP / SDK', ha='center', va='center',
        fontsize=8, fontweight='bold', color=PALETTE['gray'],
        bbox=dict(boxstyle='round,pad=0.15', fc='white', ec=PALETTE['gray'], lw=0.5))

# Internal module arrows (sample)
ax.annotate('', xy=(6.4, 6.1), xytext=(5.0, 6.1),
            arrowprops=dict(arrowstyle='->', color=PALETTE['green'], lw=1.5,
                            connectionstyle='arc3,rad=0.15'))
ax.annotate('', xy=(8.1, 5.0), xytext=(6.4, 5.0),
            arrowprops=dict(arrowstyle='->', color=PALETTE['green'], lw=1.5,
                            connectionstyle='arc3,rad=0.15'))
ax.annotate('', xy=(10.1, 6.1), xytext=(8.8, 6.1),
            arrowprops=dict(arrowstyle='->', color=PALETTE['green'], lw=1.5,
                            connectionstyle='arc3,rad=0.15'))

ax.text(9.0, 7.45, 'Domain Events (Outbox)', ha='center', va='center',
        fontsize=8, fontweight='bold', color=PALETTE['green'],
        bbox=dict(boxstyle='round,pad=0.15', fc='white', ec=PALETTE['green'], lw=0.5))

# Infrastructure → DB/Cache
for dx in [6.9, 11.1]:
    ax.annotate('', xy=(dx, 0.7), xytext=(dx, 2.0),
                arrowprops=dict(arrowstyle='->', color=PALETTE['purple'], lw=2))

# ─── LEGEND ───
leg_items = [
    (PALETTE['blue'], 'HTTP/JSON (bidirectional)'),
    (PALETTE['gray'], 'HTTP/SDK (unidirectional)'),
    (PALETTE['green'], 'Domain Events (internal)'),
    (PALETTE['purple'], 'Database/Cache queries'),
]
lx = 0.8
for i, (lc, lt) in enumerate(leg_items):
    ax.plot([lx + i * 4.3, lx + i * 4.3 + 0.5], [0.12, 0.12],
            color=lc, lw=2.5)
    ax.text(lx + i * 4.3 + 0.7, 0.12, lt, ha='left', va='center',
            fontsize=7.5, color=PALETTE['dark'])

# ─── TITLE ───
ax.text(9.0, 0.02, 'Figure 1.1 — NexaLearn High-Level System Overview',
        ha='center', va='bottom', fontsize=13, fontweight='bold', color=PALETTE['dark'])

plt.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.06)
plt.savefig(f'{OUT}/system_overview.png', dpi=DPI)
plt.savefig(f'{OUT}/system_overview.pdf')
plt.close()
print('system_overview.png/pdf')
