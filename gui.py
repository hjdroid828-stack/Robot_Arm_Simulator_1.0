import customtkinter as ctk
from kinematics import Kinematics
from visualization import RobotPlot


class RobotArmGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        # ==========================
        # Window
        # ==========================
        self.title("2-DOF Robot Arm Kinematics Simulator")
        self.geometry("1100x700")

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.create_widgets()

    def create_widgets(self):

        # ==========================
        # Left Panel
        # ==========================
        left = ctk.CTkFrame(self, width=280)
        left.pack(side="left", fill="y", padx=15, pady=15)

        title = ctk.CTkLabel(
            left,
            text="Input Parameters",
            font=("Arial", 22, "bold")
        )
        title.pack(pady=20)

        # Link1
        ctk.CTkLabel(left, text="Link1 (mm)").pack(anchor="w", padx=20)
        self.link1_entry = ctk.CTkEntry(left)
        self.link1_entry.pack(fill="x", padx=20, pady=5)
        self.link1_entry.insert(0, "250")

        # Link2
        ctk.CTkLabel(left, text="Link2 (mm)").pack(anchor="w", padx=20)
        self.link2_entry = ctk.CTkEntry(left)
        self.link2_entry.pack(fill="x", padx=20, pady=5)
        self.link2_entry.insert(0, "180")

        # Theta1
        ctk.CTkLabel(left, text="Theta1 (deg)").pack(anchor="w", padx=20)
        self.theta1_entry = ctk.CTkEntry(left)
        self.theta1_entry.pack(fill="x", padx=20, pady=5)
        self.theta1_entry.insert(0, "30")

        # Theta2
        ctk.CTkLabel(left, text="Theta2 (deg)").pack(anchor="w", padx=20)
        self.theta2_entry = ctk.CTkEntry(left)
        self.theta2_entry.pack(fill="x", padx=20, pady=5)
        self.theta2_entry.insert(0, "45")

        # Target X

        ctk.CTkLabel(left, text="Target X (mm)").pack(anchor="w", padx=20)

        self.target_x_entry = ctk.CTkEntry(left)
        self.target_x_entry.pack(fill="x", padx=20, pady=5)
        self.target_x_entry.insert(0, "250")

        # Target Y
        ctk.CTkLabel(left, text="Target Y (mm)").pack(anchor="w", padx=20)

        self.target_y_entry = ctk.CTkEntry(left)
        self.target_y_entry.pack(fill="x", padx=20, pady=5)
        self.target_y_entry.insert(0, "200")

        # ==========================
        # Buttons
        # ==========================

        self.forward_button = ctk.CTkButton(
            left,
            text="Forward Kinematics",
            command=self.forward_kinematics
        )
        self.forward_button.pack(fill="x", padx=20, pady=(25, 10))

        self.inverse_button = ctk.CTkButton(
            left,
            text="Inverse Kinematics",
            command=self.inverse_kinematics
        )
        self.inverse_button.pack(fill="x", padx=20, pady=10)

        self.workspace_button = ctk.CTkButton(
            left,
            text="Workspace",
            command=self.show_workspace
        )
        self.workspace_button.pack(fill="x", padx=20, pady=10)

        self.reset_button = ctk.CTkButton(
            left,
            text="Reset",
            command=self.reset_inputs
        )
        self.reset_button.pack(fill="x", padx=20, pady=10)

        # ==========================
        # Right Panel
        # ==========================

        right = ctk.CTkFrame(self)
        right.pack(side="right", expand=True, fill="both", padx=15, pady=15)

        title2 = ctk.CTkLabel(
            right,
            text="Robot Visualization",
            font=("Arial", 22, "bold")
        )
        title2.pack(pady=15)

        self.graph_frame = ctk.CTkFrame(
            right,
            width=700,
            height=450
        )
        self.graph_frame.pack(padx=20, pady=10)

        self.graph_frame.pack_propagate(False)

        self.plot = RobotPlot(self.graph_frame)

        self.result_label = ctk.CTkLabel(
            right,
            text="X :\nY :\nReachable :",
            font=("Consolas", 18)
        )
        self.result_label.pack(pady=20)

    # ==========================================
    # Forward Kinematics
    # ==========================================

    def forward_kinematics(self):

        try:

            link1 = float(self.link1_entry.get())
            link2 = float(self.link2_entry.get())

            theta1 = float(self.theta1_entry.get())
            theta2 = float(self.theta2_entry.get())

            x, y = Kinematics.forward(
                link1,
                link2,
                theta1,
                theta2
            )
            self.plot.draw_robot(
                link1,
                link2,
                theta1,
                theta2
            )

            self.result_label.configure(
                text=f"""X : {x:.2f}
Y : {y:.2f}
Reachable : YES"""
            )

        except ValueError:

            self.result_label.configure(
                text="Please enter valid numbers."
            )

    # ==========================================
    # Reset
    # ==========================================

    def reset_inputs(self):

        self.link1_entry.delete(0, "end")
        self.link2_entry.delete(0, "end")
        self.theta1_entry.delete(0, "end")
        self.theta2_entry.delete(0, "end")

        self.link1_entry.insert(0, "250")
        self.link2_entry.insert(0, "180")
        self.theta1_entry.insert(0, "30")
        self.theta2_entry.insert(0, "45")

        self.target_x_entry.delete(0, "end")
        self.target_y_entry.delete(0, "end")

        self.target_x_entry.insert(0, "250")
        self.target_y_entry.insert(0, "200")

        self.result_label.configure(
            text="X :\nY :\nReachable :"
        )
        self.plot.draw_empty()
        
    def inverse_kinematics(self):

        try:

            link1 = float(self.link1_entry.get())
            link2 = float(self.link2_entry.get())

            target_x = float(self.target_x_entry.get())
            target_y = float(self.target_y_entry.get())

            theta1, theta2 = Kinematics.inverse(
                link1,
                link2,
                target_x,
                target_y
            )

            self.theta1_entry.delete(0, "end")
            self.theta2_entry.delete(0, "end")

            self.theta1_entry.insert(0, f"{theta1:.2f}")
            self.theta2_entry.insert(0, f"{theta2:.2f}")

            self.plot.draw_robot(
                link1,
                link2,
                theta1,
                theta2
            )

            self.result_label.configure(
                text=f"""Inverse Kinematics

            Theta1 : {theta1:.2f}°
            Theta2 : {theta2:.2f}°

            Target X : {target_x:.2f}
            Target Y : {target_y:.2f}
            """
            )

        except Exception as e:
            self.result_label.configure(text=str(e))
    
    def show_workspace(self):

        try:

            link1 = float(self.link1_entry.get())
            link2 = float(self.link2_entry.get())

            theta1 = float(self.theta1_entry.get())
            theta2 = float(self.theta2_entry.get())

            self.plot.draw_workspace(
                link1,
                link2,
                theta1,
                theta2
            )

            self.result_label.configure(
                text=f"""Workspace
            Link1 : {link1:.0f} mm
            Link2 : {link2:.0f} mm
                Workspace Generated"""
            )

        except Exception as e:

            self.result_label.configure(
                text=str(e)
            )