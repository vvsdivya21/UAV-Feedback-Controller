# UAV-Feedback-Controller
Here’s a README file tailored for a GitHub repository based on your project description:

UAV Feedback Controller

Overview

This project implements a feedback control system for a 2D simulated UAV, designed as part of a university coursework project. The objective of this controller is to achieve and maintain a desired position by controlling the thrust from two motors. The system is tested in a custom simulation environment that provides positional, velocity, and attitude data for a quadcopter, allowing the control algorithm to guide the UAV to target coordinates effectively.

Background

Feedback control systems have historical roots dating back to ancient water clocks, where a float regulator maintained water levels, much like modern control loops. Over the centuries, control mechanisms evolved significantly, with developments like Christiaan Huygens’ flyball governor for machinery in the 17th century, and James Watt’s steam engine speed regulator. The formal field of control theory advanced through the contributions of notable scientists like J.C. Maxwell, eventually leading to the PID controller, a fundamental control mechanism still widely applied today.

This project builds on these foundational control principles, applying them to UAV navigation. The implemented controller leverages real-time sensor data to compute necessary thrust adjustments, using feedback to minimize error between the UAV’s current position and a target position.

Project Objective

The goal is to implement a feedback controller that allows a 2D simulated UAV to reach and hold a specified position with minimal positional error. The control algorithm outputs normalized thrust values (ranging from 0 to 1) for two motors, dynamically adjusting them to maintain stability and position in the face of potential disturbances like gusts of wind.

Key Features

	1.	Feedback Control System: Calculates thrust output based on real-time positional and velocity data to minimize positional error.
	2.	Throttle Mixing: Controls two motors’ thrust to achieve stable and accurate UAV positioning.
	3.	Gust Resistance: Designed to maintain position even under wind disturbances, with extra credit for maintaining performance in gusty conditions.
	4.	Positional Accuracy: Position data collected over multiple tests determines the final average positional error, which is used for performance grading.

Task Requirements

	•	Implement a feedback control algorithm to move the UAV to target positions.
	•	Design the controller to operate within a simulation that includes a UAV and empty land environment.
	•	Tune the controller for optimal performance, considering thrust adjustments, positional stability, and gust handling.
	•	Test the controller across five different random target positions within ±4 meters from the starting point, with each test lasting 10 seconds.

Advanced Implementation

Extra credit is awarded for advanced methods, such as reinforcement learning, provided they are pre-approved for necessary library additions.

Files and Instructions

	•	controller.py: The main file to be submitted, containing the controller code with specified inputs and outputs. The top lines should indicate wind resistance capability and group number.
	•	targets.csv: Defines target positions for the UAV. Custom targets are encouraged for testing but are randomized during final evaluations.

Testing and Grading

The controller will be tested in an automated environment, where positional data is averaged across trials to determine performance. Key metrics include:

	•	Positional Error: Average deviation from target position.
	•	Stability: Consistency of positioning, measured by standard deviation over multiple trials.

Note: Ensure no modifications to input/output variable names, as it may interfere with the automated testing environment.

Simulator Setup

	1.	Use the provided Python environment with dependencies specified in the coursework folder.
	2.	Ensure virtual environment usage (e.g., Anaconda) for isolated testing.
	3.	Follow installation instructions in the provided ZIP file to set up the simulator and controller environment.

Usage

	1.	Clone this repository and set up the required environment.
	2.	Implement the control logic in controller.py, tuning the parameters for optimized UAV control.
	3.	Test in the simulator, adjusting the code for better accuracy, especially in gust conditions if wind handling is enabled.
	4.	Submit controller.py along with required video recordings showcasing the performance in various scenarios.

Acknowledgments

This project’s simulation framework and instructions were provided by the course instructors, with further insights on throttle mixing available via Cookie Robotics.

This README outlines the project’s purpose, historical context, and practical application in control theory, as well as instructions for setup, implementation, and testing. Let me know if you’d like additional sections or details!
