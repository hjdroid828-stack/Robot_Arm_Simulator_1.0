import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class RobotPlot:

    def __init__(self, frame):

        self.fig, self.ax = plt.subplots(figsize=(6, 5))

        self.canvas = FigureCanvasTkAgg(
            self.fig,
            master=frame
        )

        self.canvas.get_tk_widget().pack(
            fill="both",
            expand=True
        )

        self.draw_empty()

    def draw_empty(self):

        self.ax.clear()

        self.ax.set_xlim(-500, 500)
        self.ax.set_ylim(-500, 500)

        self.ax.set_aspect("equal")

        self.ax.grid(True)

        self.ax.set_xlabel("X (mm)")
        self.ax.set_ylabel("Y (mm)")

        self.canvas.draw()

    def draw_robot(self, link1, link2, theta1, theta2):

        import numpy as np

        t1 = np.radians(theta1)
        t2 = np.radians(theta2)

        x0 = 0
        y0 = 0

        x1 = link1*np.cos(t1)
        y1 = link1*np.sin(t1)

        x2 = x1 + link2*np.cos(t1+t2)
        y2 = y1 + link2*np.sin(t1+t2)

        self.ax.clear()

        self.ax.plot(
            [x0, x1],
            [y0, y1],
            linewidth=4
        )

        self.ax.plot(
            [x1, x2],
            [y1, y2],
            linewidth=4
        )

        # Base
        self.ax.plot(x0, y0, "ko", markersize=8)

        # Joint
        self.ax.plot(x1, y1, "ko", markersize=8)

        # End Effector
        self.ax.plot(x2, y2, "ro", markersize=10)

        self.ax.scatter(x2, y2, s=80)

        self.ax.set_xlim(-500, 500)
        self.ax.set_ylim(-500, 500)

        self.ax.set_aspect("equal")

        self.ax.grid(True)

        self.ax.set_xlabel("X (mm)")
        self.ax.set_ylabel("Y (mm)")

        if theta1 is not None:

            t1 = np.radians(theta1)
            t2 = np.radians(theta2)

            x1 = link1*np.cos(t1)
            y1 = link1*np.sin(t1)

            x2 = x1 + link2*np.cos(t1+t2)
            y2 = y1 + link2*np.sin(t1+t2)

            self.ax.plot([0, x1], [0, y1], linewidth=4)
            self.ax.plot([x1, x2], [y1, y2], linewidth=4)

            self.ax.plot(0, 0, "ko", markersize=8)
            self.ax.plot(x1, y1, "ko", markersize=8)
            self.ax.plot(x2, y2, "ro", markersize=10)

        self.canvas.draw()

    def draw_workspace(self, link1, link2, theta1=None, theta2=None):

        import numpy as np

        self.ax.clear()

        theta1 = np.linspace(-180, 180, 120)
        theta2 = np.linspace(-180, 180, 120)

        X = []
        Y = []

        for t1 in theta1:
            for t2 in theta2:

                t1r = np.radians(t1)
                t2r = np.radians(t2)

                x = link1*np.cos(t1r) + link2*np.cos(t1r+t2r)
                y = link1*np.sin(t1r) + link2*np.sin(t1r+t2r)

                X.append(x)
                Y.append(y)

        self.ax.scatter(
            X,
            Y,
            s=1,
            alpha=0.25
        )

        r = link1 + link2

        self.ax.set_xlim(-r-20, r+20)
        self.ax.set_ylim(-r-20, r+20)

        self.ax.set_aspect("equal")
        self.ax.grid(True)

        self.canvas.draw()
