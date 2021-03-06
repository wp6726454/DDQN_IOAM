import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle
from math import pi
# data monitor during simulation
def data_viewer(x1, y1, u1, phit, rudder_angle, t,
                xlim_left, xlim_right,ylim_left, ylim_right,
                goal_x, goal_y,
                T='', Ffoil_x=''):

    plt.figure(1, figsize=(14, 7))
    grid = plt.GridSpec(3, 2, wspace=0.5, hspace=0.5)
    path = plt.subplot(grid[0:3, 0])
    path.plot(y1, x1, label='Sailing path', color='b')
    path.set_title('Path')
    path.axis([ylim_left, ylim_right, xlim_left, xlim_right])
    path.scatter(goal_y, goal_x, label='Goal', color='r')
    theta = np.arange(0,2*np.pi, 0.01)
    path.plot(0, 0, color='b') #start position
    path.plot(50 + 12 * np.cos(theta),  50 + 12 * np.sin(theta),color='k')  #obst1
    path.plot(10 + 10 * np.cos(theta), 70 + 10 * np.sin(theta), color='k')  #obst2
    path.plot(50 + 8 * np.cos(theta), 90 + 8 * np.sin(theta),color='k')  #obst3
    path.plot(80 + 8 * np.cos(theta), 70 + 8 * np.sin(theta), color='k')  # obst4
    path.plot(70 + 8 * np.cos(theta), 20 + 8 * np.sin(theta), color='k')  # obst5
    path.set_ylabel('x(m)')
    path.set_xlabel('y(m)')
    path.legend()


    heading = plt.subplot(grid[0, 1])
    heading.plot(t, phit, '-r', label='phit')
    heading.set_title('Heading')
    heading.set_ylabel('Course(rad)')

    speed_plot = plt.subplot(grid[1, 1])
    speed_plot.plot(t, u1, '-r')
    speed_plot.set_title('Sailing speed')
    speed_plot.set_ylabel('Speed(m/s)')

    rudder_angle_plot = plt.subplot(grid[2, 1])
    rudder_angle_deg = [i*180/pi for i in rudder_angle]
    rudder_angle_plot.plot(t, rudder_angle_deg, '-r')
    rudder_angle_plot.set_title('Rudder angle')
    rudder_angle_plot.set_ylabel('Rudder angle(deg)')
    rudder_angle_plot.set_xlabel('Time(s)')

    if T:
        plt.figure(2, figsize=(12, 4))
        T_plot = plt.subplot(1, 2, 1)
        T_plot.plot(t, T, '-r')
        T_plot.set_title('Tether force')
        T_plot.set_ylabel('T(N)')
        T_plot.set_xlabel('Time(s)')

    if Ffoil_x:
        plt.figure(2, figsize=(12, 4))
        Ffoil_x_plot = plt.subplot(1, 2, 2)
        Ffoil_x_plot.plot(t, Ffoil_x, '-r')
        Ffoil_x_plot.set_title('Foil force')
        Ffoil_x_plot.set_ylabel('Foil force(N)')
        Ffoil_x_plot.set_xlabel('Time(s)')

    plt.pause(0.00001)


