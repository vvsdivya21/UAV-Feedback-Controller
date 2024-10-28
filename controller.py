import numpy as np

wind_active = True # Select whether you want to activate wind or not
group_number = 37  # Enter your group number here

# Veichle parameters
m   = 1.0456 # UAV mass
g   = 9.81   #  gravity acceleration
Ixx = 0.2729 # UAV inertia
arm_length  = 0.25 # UAV arm length

# Initialization of the integral terms and plot inputs
integral_x = 0 
integral_y = 0
integral_attitude=0

def controller(state, target_pos, dt):
     # Refer to the integral term of the global variable
     global integral_x,integral_y,integral_attitude

     # Horizontal PID controllers
     # PID gains
     kp_x = 2.67  # Proportional gain 
     ki_x = 0.003 # Integral gain (control steady state error)
     kd_x = 2.69  # Differential gain (Damping term)
     
     error_x = state[0] - target_pos[0] # Horizontal error
     integral_x += error_x * dt         # Update the horizontal integral
    
     # Vertical PID controller 
     # PID gains
     kp_y = 135   # Proportional gain
     ki_y = -0.06 # Integral gain (control steady state error)
     kd_y = 58.75 # Differential gain (Damping term)
     
     error_y = state[1] - target_pos[1] # Vertical error
     integral_y += error_y * dt         # Update the vertical integral

     #Inner loop input
     phi=-1/g*(kp_x*error_x + ki_x*integral_x + kd_x*(state[2])) # Calculate attitude control targets
    
     # Attitude PID controller 
     # PID gains
     kp_attitude = 20   # Proportional gain
     ki_attitude = 0.08 # Integral gain (control steady state error)
     kd_attitude = 5.75 # Differential gain (Damping term)

     error_attitude = state[4] - phi          # Attitude error
     integral_attitude += error_attitude * dt # Update the integral term of the attitude

     # Motor mixing algorithm inputs
     F=m*(g + kp_y*error_y + ki_y*integral_y + kd_y*state[3]) # motor thrust
     M=Ixx*(kp_attitude*error_attitude + ki_attitude*integral_attitude+kd_attitude*(state[5])) # motor torque


     u1=0.5*(F - M/arm_length) # throttle output: left motor
     u2=0.5*(F + M/arm_length) # throttle output: right motor

     u_1 = min(max(0, u1), 1) # Limits the throttle settin
     u_2= min(max(0, u2), 1)  # Limits the throttle setting 

     return (u_1, u_2) # Return the throttle output
 
