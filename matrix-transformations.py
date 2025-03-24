import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define the vertices of a cube
def get_cube():
    return np.array([
        [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
        [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]
    ])

# Define cube faces
def get_faces(vertices):
    return [
        [vertices[j] for j in [0, 1, 2, 3]],
        [vertices[j] for j in [4, 5, 6, 7]],
        [vertices[j] for j in [0, 1, 5, 4]],
        [vertices[j] for j in [2, 3, 7, 6]],
        [vertices[j] for j in [1, 2, 6, 5]],
        [vertices[j] for j in [4, 7, 3, 0]]
    ]

# Transformation matrices
def translation_matrix(tx, ty, tz):
    return np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ])

def scaling_matrix(sx, sy, sz):
    return np.array([
        [sx, 0, 0, 0],
        [0, sy, 0, 0],
        [0, 0, sz, 0],
        [0, 0, 0, 1]
    ])

def rotation_matrix_x(angle):
    c, s = np.cos(angle), np.sin(angle)
    return np.array([
        [1, 0, 0, 0],
        [0, c, -s, 0],
        [0, s, c, 0],
        [0, 0, 0, 1]
    ])

def rotation_matrix_y(angle):
    c, s = np.cos(angle), np.sin(angle)
    return np.array([
        [c, 0, s, 0],
        [0, 1, 0, 0],
        [-s, 0, c, 0],
        [0, 0, 0, 1]
    ])

def rotation_matrix_z(angle):
    c, s = np.cos(angle), np.sin(angle)
    return np.array([
        [c, -s, 0, 0],
        [s, c, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

# Apply transformations
def transform_cube(vertices, tx, ty, tz, sx, sy, sz, rx, ry, rz):
    cube_homogeneous = np.c_[vertices, np.ones(len(vertices))].T
    
    transform = (
        translation_matrix(tx, ty, tz) @ 
        rotation_matrix_x(rx) @ rotation_matrix_y(ry) @ rotation_matrix_z(rz) @ 
        scaling_matrix(sx, sy, sz)
    )
    
    transformed_vertices = (transform @ cube_homogeneous)[:3].T
    return transformed_vertices

# Interactive plot setup
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

def update(val):
    ax.clear()
    
    tx, ty, tz = sliders['tx'].val, sliders['ty'].val, sliders['tz'].val
    sx, sy, sz = sliders['sx'].val, sliders['sy'].val, sliders['sz'].val
    rx, ry, rz = np.radians(sliders['rx'].val), np.radians(sliders['ry'].val), np.radians(sliders['rz'].val)
    
    transformed = transform_cube(get_cube(), tx, ty, tz, sx, sy, sz, rx, ry, rz)
    faces = get_faces(transformed)
    ax.add_collection3d(Poly3DCollection(faces, color='cyan', alpha=0.6, edgecolor='black'))
    
    ax.set_xlim([-3, 3])
    ax.set_ylim([-3, 3])
    ax.set_zlim([-3, 3])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.draw()

# Create sliders
axcolor = 'lightgoldenrodyellow'
sliders = {}
slider_positions = ["tx", "ty", "tz", "sx", "sy", "sz", "rx", "ry", "rz"]
slider_ranges = [(-2, 2), (-2, 2), (-2, 2), (0.5, 2), (0.5, 2), (0.5, 2), (-180, 180), (-180, 180), (-180, 180)]

for i, (name, rng) in enumerate(zip(slider_positions, slider_ranges)):
    ax_slider = plt.axes([0.2, 0.02 + i * 0.03, 0.65, 0.02], facecolor=axcolor)
    sliders[name] = Slider(ax_slider, name, rng[0], rng[1], valinit=(rng[0] + rng[1]) / 2)
    sliders[name].on_changed(update)

# Initial plot
update(None)
plt.show()
