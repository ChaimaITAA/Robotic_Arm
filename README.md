# Robotic_Arm
![tri](tri.png) 
![robot](robot.PNG)
# 
As part of my end-of-year project, I chose to work on this theme,
which we found quite interesting, as it offers us an excellent opportunity to
implement all the skills I have acquired up to this point in our training in robotics and mechatronics and image processing/industrial vision.
I am also interested in the industrial context of this project, which offers us an opportunity to manipulate robots in their exact operating environments and to take all these conditions into account from the the design phase.
# Mechanical design
![rob](rob.png)
# 
I have opted for a design that allows us to 3D print the prototype in the right dimensions and
the prototype in the right size and with the right function.
For the mechanical design, I worked on SolidWorks, for the realization of the components as well as their assembly. 
# Impression 3D
![print](print.png)
#  
To do this, I export the parts to be printed separately in STL format. I used Slicer Ultimaker Cura, to prepare the printing. 
# Simulation
#  
To perform the simulation I needed the SolidWorks design file of the robot:
The SolidWorks to URDF exporter is a SolidWorks add-on that allows the convenient export of
parts and software assemblies into a URDF file. The exporter will create a package that contains a directory for meshes, textures and robots (URDF files). 
For assemblies, the exporter will build the links and create a tree structure based on the SW assembly hierarchy. The exporter can automatically determine the joint type,
joint transformations and appropriate axes.
#  
![urdf](urdf.PNG)
#  
The next step is to export the URDF files from SolidWorks and use them to generate the
URDF package using Moveit setup assistant.
![moveit](moveit.PNG)

We load the URDF file into the setup wizard and start configuring it:
  * Generate a self-collision. 
  * Define vitual joints.
  * define a planning group.
  * define robot poses.
  * define end effectors.
  * set-up ros controller.

![simulation](simulation.png)
