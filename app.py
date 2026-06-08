import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title='단위원을 통해 알아보는 삼각함수',
    layout='wide',
)

st.title('단위원을 통해 알아보는 삼각함수')

angle_options = ['0', 'π/2', 'π', '3π/2', '2π']
selected_angle = st.selectbox('각도를 선택하세요', angle_options)
st.subheader('단위원과 sin함수')

angle_map = {
    '0': 0.0,
    'π/2': np.pi / 2,
    'π': np.pi,
    '3π/2': 3 * np.pi / 2,
    '2π': 2 * np.pi,
}
angle_value = angle_map[selected_angle]

st.write(f'선택된 각도: **{selected_angle}**')

# 전체 그래프 크기를 맞추기 위해 두 그래프에 동일한 figsize를 사용합니다.
figure_size = (4, 4)

left_col, right_col = st.columns(2, gap='large')

# 단위원 그래프
with left_col:
    fig, ax = plt.subplots(figsize=figure_size)

    theta = np.linspace(0, 2 * np.pi, 400)
    circle_x = np.cos(theta)
    circle_y = np.sin(theta)

    ax.plot(circle_x, circle_y, color='black', linewidth=1)
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)

    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect('equal', adjustable='box')
    ax.grid(True, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
    ax.set_xticks([-1.0, -0.5, 0.0, 0.5, 1.0])
    ax.set_yticks([-1.0, -0.5, 0.0, 0.5, 1.0])

    if angle_value == 0.0:
        ax.scatter([1.0], [0.0], color='red', s=70, zorder=5)
    else:
        arc_x = np.cos(np.linspace(0, angle_value, 200))
        arc_y = np.sin(np.linspace(0, angle_value, 200))
        ax.plot(arc_x, arc_y, color='red', linewidth=2.5)
        endpoint_x = np.cos(angle_value)
        endpoint_y = np.sin(angle_value)
        ax.scatter([endpoint_x], [endpoint_y], color='red', s=70, zorder=5)

    ax.set_xlabel('x')
    ax.xaxis.set_label_coords(1.05, 0.5)
    ax.set_ylabel('y', rotation=0, labelpad=15)
    ax.yaxis.set_label_coords(0.5, 1.05)
    st.pyplot(fig)

# 사인 함수 그래프
with right_col:
    fig, ax = plt.subplots(figsize=figure_size)

    x = np.linspace(0, 2 * np.pi, 400)
    y = np.sin(x)
    ax.plot(x, y, color='black', linewidth=1)

    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)

    ax.set_xlim(0, 2 * np.pi)
    ax.set_ylim(-1.2, 1.2)
    ax.grid(True, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)

    tick_positions = [0, np.pi/2, np.pi, 3 * np.pi / 2, 2 * np.pi]
    tick_labels = ['0', 'π/2', 'π', '3π/2', '2π']
    ax.set_xticks(tick_positions)
    ax.set_xticklabels(tick_labels)
    ax.set_yticks([-1, 0, 1])

    if angle_value == 0.0:
        ax.scatter([0.0], [0.0], color='red', s=70, zorder=5)
    else:
        x_red = np.linspace(0, angle_value, 200)
        y_red = np.sin(x_red)
        ax.plot(x_red, y_red, color='red', linewidth=2.5)
        ax.scatter([angle_value], [np.sin(angle_value)], color='red', s=70, zorder=5)

    ax.set_xlabel('x')
    ax.set_ylabel('sin(x)', rotation=0, labelpad=15)
    ax.yaxis.set_label_coords(0.0, 1.05)
    st.pyplot(fig)

st.subheader('단위원과 cos함수')

bottom_left, bottom_right = st.columns(2, gap='large')

with bottom_left:
    fig, ax = plt.subplots(figsize=figure_size)

    theta = np.linspace(0, 2 * np.pi, 400)
    circle_x = np.cos(theta)
    circle_y = np.sin(theta)

    ax.plot(circle_x, circle_y, color='black', linewidth=1)
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)

    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect('equal', adjustable='box')
    ax.grid(True, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
    ax.set_xticks([-1.0, -0.5, 0.0, 0.5, 1.0])
    ax.set_yticks([-1.0, -0.5, 0.0, 0.5, 1.0])

    if angle_value != 0.0:
        arc_x = np.cos(np.linspace(0, angle_value, 200))
        arc_y = np.sin(np.linspace(0, angle_value, 200))
        ax.plot(arc_x, arc_y, color='blue', linewidth=2.5)
        endpoint_x = np.cos(angle_value)
        endpoint_y = np.sin(angle_value)
        ax.scatter([endpoint_x], [endpoint_y], color='red', s=70, zorder=5)
    else:
        ax.scatter([1.0], [0.0], color='red', s=70, zorder=5)

    ax.set_xlabel('x')
    ax.xaxis.set_label_coords(1.05, 0.5)
    ax.set_ylabel('y', rotation=0, labelpad=15)
    ax.yaxis.set_label_coords(0.5, 1.05)
    st.pyplot(fig)

with bottom_right:
    fig, ax = plt.subplots(figsize=figure_size)

    x = np.linspace(0, 2 * np.pi, 400)
    y = np.cos(x)
    ax.plot(x, y, color='black', linewidth=1)

    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)

    ax.set_xlim(0, 2 * np.pi)
    ax.set_ylim(-1.2, 1.2)
    ax.grid(True, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)

    tick_positions = [0, np.pi/2, np.pi, 3 * np.pi / 2, 2 * np.pi]
    tick_labels = ['0', 'π/2', 'π', '3π/2', '2π']
    ax.set_xticks(tick_positions)
    ax.set_xticklabels(tick_labels)
    ax.set_yticks([-1, 0, 1])

    if angle_value != 0.0:
        x_blue = np.linspace(0, angle_value, 200)
        y_blue = np.cos(x_blue)
        ax.plot(x_blue, y_blue, color='blue', linewidth=2.5)
        ax.scatter([angle_value], [np.cos(angle_value)], color='red', s=70, zorder=5)
    else:
        ax.scatter([0.0], [1.0], color='red', s=70, zorder=5)

    ax.set_xlabel('x')
    ax.set_ylabel('cos(x)', rotation=0, labelpad=15)
    ax.yaxis.set_label_coords(0.0, 1.05)
    st.pyplot(fig)
