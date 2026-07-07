import numpy as np

class Kinematics:

    @staticmethod
    def forward(link1, link2, theta1, theta2):

        theta1 = np.radians(theta1)
        theta2 = np.radians(theta2)

        x = link1 * np.cos(theta1) + link2 * np.cos(theta1 + theta2)
        y = link1 * np.sin(theta1) + link2 * np.sin(theta1 + theta2)

        return x, y
    
    @staticmethod
    def inverse(link1, link2, x, y):

        import numpy as np

        d = (x ** 2 + y ** 2 - link1 ** 2 - link2 **2 ) / (2 * link1 * link2)

        if abs(d) > 1:
            raise ValueError("Target is outside workspace.")

        theta2 = np.arccos(d)

        theta1 = np.arctan2(y, x) - np.arctan2(
            link2 * np.sin(theta2),
            link1 + link2 * np.cos(theta2)
        )

        return np.degrees(theta1), np.degrees(theta2)
    

