import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title='Unit Circle and Sine Visualization',
    layout='wide',
)

st.title('단위원과 사인 함수 시각화')

angle_options = ['0', 'π/2', 'π', '3π/2', '2π']
selected_angle = st.selectbox('각도를 선택하세요', angle_options)

angle_map = {
    '0': 0.0,
    'π/2': np.pi / 2,
    'π': np.pi,
    '3π/2': 3 * np.pi / 2,
    '2π': 2 * np.pi,
}
angle_value = angle_map[selected_angle]

st.markdown(f'**선택된 각도: {selected_angle}**')

left_col, right_col = st.columns(2, gap='large')
figure_size = (4, 4)

with left_col:
    fig, ax = plt.subplots(figsize=figure_size)
    theta = np.linspace(0, 2 * np.pi, 400)

    ax.plot(np.cos(theta), np.sin(theta), color='black', linewidth=1)
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)

    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect('equal', adjustable='box')
    ax.grid(True, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
    ax.set_xticks([-1.0, -0.5, 0.0, 0.5, 1.0])
    ax.set_yticks([-1.0, -0.5, 0.0, 0.5, 1.0])

    if angle_value == 0.0:
        ax.scatter([1.0], [0.0], color='red', s=80, zorder=5)
    else:
        arc_x = np.cos(np.linspace(0, angle_value, 200))
        arc_y = np.sin(np.linspace(0, angle_value, 200))
        ax.plot(arc_x, arc_y, color='red', linewidth=2.5)
        ax.scatter([np.cos(angle_value)], [np.sin(angle_value)], color='red', s=80, zorder=5)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    st.pyplot(fig)

with right_col:
    fig, ax = plt.subplots(figsize=figure_size)
    x = np.linspace(0, 2 * np.pi, 400)

    ax.plot(x, np.sin(x), color='black', linewidth=1)
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)

    ax.set_xlim(0, 2 * np.pi)
    ax.set_ylim(-1.2, 1.2)
    ax.grid(True, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)

    tick_positions = [0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi]
    tick_labels = ['0', 'π/2', 'π', '3π/2', '2π']
    ax.set_xticks(tick_positions)
    ax.set_xticklabels(tick_labels)
    ax.set_yticks([-1, 0, 1])

    if angle_value == 0.0:
        ax.scatter([0.0], [0.0], color='red', s=80, zorder=5)
    else:
        x_red = np.linspace(0, angle_value, 200)
        ax.plot(x_red, np.sin(x_red), color='red', linewidth=2.5)
        ax.scatter([angle_value], [np.sin(angle_value)], color='red', s=80, zorder=5)

    ax.set_xlabel('x')
    ax.set_ylabel('sin(x)')
    st.pyplot(fig)
