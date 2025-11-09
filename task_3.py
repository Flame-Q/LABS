import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots()
ax.set_aspect('equal')
plt.axis('off')

orange = "#e07a1f"

body = patches.Polygon([[0.5, 0.7], [1.5, 0.7], [1, 1.5]],
                       closed=True, edgecolor="black", facecolor=orange, linewidth=2)
ax.add_patch(body)

head = patches.Polygon([[0.95, 1.15], [0.7, 1.9], [1.5, 1.7]],
                       closed=True, edgecolor="black", facecolor=orange, linewidth=2)
ax.add_patch(head)

ear1 = patches.Polygon([[0.7, 1.9], [0.9, 2.2], [0.95, 1.84]], 
                       closed=True, edgecolor="black", facecolor=orange, linewidth=2) 
ear2 = patches.Polygon([[1.25, 1.765], [1.45, 2.065], [1.5, 1.7]], 
                       closed=True, edgecolor="black", facecolor=orange, linewidth=2) 
ax.add_patch(ear1) 
ax.add_patch(ear2)

ear1_white = patches.Polygon([[0.775, 1.94], [0.875, 2.09], [0.9, 1.91]],
                             closed=True, edgecolor="black", facecolor="white")
ear2_white = patches.Polygon([[1.325, 1.804], [1.425, 1.954], [1.45, 1.772]],
                             closed=True, edgecolor="black", facecolor="white")
ax.add_patch(ear1_white)
ax.add_patch(ear2_white)

tail = patches.Polygon([[1.5, 0.7], [1.8, 1.4], [2.2, 1.2]],
                       closed=True, edgecolor="black", facecolor=orange, linewidth=2)
ax.add_patch(tail)

tail_tip = patches.Polygon([[1.8, 1.4], [2.15, 1.55], [2.2, 1.2]],
                           closed=True, edgecolor="black", facecolor="white", linewidth=2)
ax.add_patch(tail_tip)

ax.plot(0.947, 1.15, marker='o', markersize=7, color='black')

ax.plot([0.947, 0.72], [1.15, 1.25], 'k-', linewidth=1.5)
ax.plot([0.947, 0.72], [1.15, 1.16], 'k-', linewidth=1.5)
ax.plot([0.947, 1.17], [1.15, 1.14], 'k-', linewidth=1.5)
ax.plot([0.947, 1.17], [1.15, 1.05], 'k-', linewidth=1.5)

ax.plot([0.9, 0.80], [0.8, 0.7], 'k-', linewidth=3)
ax.plot([0.7, 0.80], [0.8, 0.7], 'k-', linewidth=3)

ax.plot([1.3, 1.20], [0.8, 0.7], 'k-', linewidth=3)
ax.plot([1.1, 1.20], [0.8, 0.7], 'k-', linewidth=3)

eye_radius = 0.075

left_eye = patches.Circle((0.9, 1.65), eye_radius, facecolor='white', edgecolor='black', linewidth=2)
left_pupil = patches.Circle((0.9, 1.65), eye_radius/2, facecolor='black')
ax.add_patch(left_eye)
ax.add_patch(left_pupil)

right_eye = patches.Circle((1.2, 1.58), eye_radius, facecolor='white', edgecolor='black', linewidth=2)
right_pupil = patches.Circle((1.2, 1.58), eye_radius/2, facecolor='black')
ax.add_patch(right_eye)
ax.add_patch(right_pupil)

plt.xlim(0, 2.6)
plt.ylim(0.4, 2.7)
plt.show()
