#################### SENSOR_PKG ROS PROJECT ###################
###############################################################
###############################################################

##################### PROJECT DESCRIPTION #####################
###############################################################

Sensor_pkg is a ROS Package that eases the use of the FTS3 and FTS1 pressure sensors from Seed Robotics.
The goal is to let the user communicate with these sensors without having to deal with serial port reading/writing.
Serial communication is done by the python script read_publish_sensor_node.py, all you have to do to communicate with the sensors is sending or reading ROS messages.
This package allows the user to easily read data from the sensors via ROS messages. This can be done either using ROS command lines in a terminal or via a Python script (with the rospy lib) or a C++ project (with the roscpp lib).
It also allows the user to send commands to the sensors via ROS messages, either using ROS command lines in a terminal or via a Python script (with the rospy lib) or a C++ project (with the roscpp lib).
There are four user code examples to interact with the sensors using ROS in the src/sensor_pkg/user_example folder. These samples are written in Python and will be explained later in this file.

######################## INSTALLATION #########################
###############################################################

In order to work with this package, you must intall ROS Noetic.
Please follow the instructions on the ROS Wiki website here http://wiki.ros.org/noetic/Installation. Please install the desktop-full version.
Please note that this version of the package has only been tested on Ubuntu 20.04.

In order to make this package work, you also need to have Python3 installed. This package have been developped using Python 3.8.10.
You also need to install the following python libs :
- rospy (should have been installed with ROS Noetic)
- std_msgs (should have been installed with ROS Noetic)
- pyserial
- numpy

Once this is done you can clone the root folder of this project. (i.e this folder)
Then, in the catkin_ws folder, open a terminal and type the following command :

catkin_make

Afterwards, you need to source your workspace. To do so, in the root folder type

source devel/setup.*    (* Being your CLI, for example setup.bash)

Note that if you want to use this package features in other terminal windows you will have to source each of these terminals aswell.

Now you should be set up to work with the ROS Package SENSOR_PKG.

######################## TROUBLESHOOTING ######################
###############################################################

If you have trouble with permissions on serial port (for example if you cannot open a serial port on GTKTerm), you can solve this issue by adding yourself to the dialout group. To do so, open a terminal and type :

sudo usermod -a -G dialout $USER

Then logout and log back for the changes to take effect.

######################## MESSAGES STRUCTURE ###################
###############################################################

In this package, you can find 3 types of custom ROS messages used to communicate with the sensors.
You can find their structure in the catkin_ws/src/sensor_pkg/msg folder.

The lone_sensor message is used to store data from a single sensor. Its structure is the following :

int8 id           # The ID of the sensor, usually going from 0 to 4. It can be set to 'None' if the sensor doesn't send any data.
int64 fx          # This is the force applied on the x axis
int64 fy          # This is the force applied on the y axis
int64 fz          # This is the force applied on the z axis
float64 abs       # This is the absolute value of the force, in mN. Used for spherical coordinates
float64 yaw       # This is the yaw of the force applied. Used for spherical coordinates
float64 pitch     # This is the pitch of the force applied. Used for spherical coordinates
bool is_present   # This is a boolean flag to let the program know if the sensor sends data. Set to 'True' if the sensor works, 'False' otherwise.
bool is_3D        # This is a boolean flag to tell if the sensor is a 3D or 1D. Set to 'True' for a 3D sensor, 'False' for a 1D sensor.

The AllSensors message stores the data for every sensor connected. Its structure is the following :

Header header                     # A ROS header, in which you can get the timestamp
int8 length                       # The length of the array, it should be equal to the number of sensors you're using.
sensor_pkg/lone_sensor[] data     # The array of lone_sensor messages. This is where all the sensors data is stored.

When you want to read data from the sensors, you need to access the AllSensors message and go through the 'data' array attribute to get data from each sensor.

The last message is the user_command message. This one is used to write commands to the sensor.
Its structure is the following :

bool calibrate          # If you want to calibrate the sensors, set this field to 'true'
bool setepoch           # If you want to set the epoch of the sensors, set this field to 'true' and set the epoch_sec and epoch_msec strings to the wanted epoch
string epoch_sec        # Epoch seconds
string epoch_msec       # Epoch miliseconds
bool diagnosis_request  # Set to 'true' in order to get a diagnosis from the sensors. The sensors diagnosis will be stored in ROS Logs.
bool set_frequency      # Set to 'true' if you want to change the sending frequency of the sensors. You also need to specify a frequency in to 'frequency' field.
int8 frequency          # The wanted frequency, between 1 and 50 (Hz)
bool raw_string         # Set to 'true' if you want to send a custom message, then fill the 'ra2w' field with your custom message.
string raw              # String used to store a custom message to be sent to the sensors.

To sum up, the lone_sensor and AllSensors messages are filled by the package at each new data from the sensors. These messages are meant to be read to get sensors data.
The user_command message will be filled by yourself if you need to send commands to the sensors. This can be done through a Python script / C++ file (as we'll see in the user_samples 3 and 4). It can also be done through command lines while the package is running.

To send commands via command lines, you need to use rostopic pub. Here is an example of how to do so :

rostopic pub -1 /user_command sensor_pkg/user_command "{calibrate: false, setepoch: false, epoch_sec: '', epoch_msec: '', diagnosis_request: true, set_frequency: false, frequency: 0, raw_string: false, raw: ''}"

This command will only ask for a diagnosis_request.
If you want to set the frequency to 20Hz, you can do as following :

rostopic pub -1 /user_command sensor_pkg/user_command "{calibrate: false, setepoch: false, epoch_sec: '', epoch_msec: '', diagnosis_request: false, set_frequency: true, frequency: 20, raw_string: false, raw: ''}"

######################## PACKAGE USE ##########################
###############################################################

In order to make the package work correctly with your setup, please open the 'sensor.launch' file located at catkin_ws/src/sensor_pkg/launch.

At line 2, please change "/dev/ttyUSB0" to the name of your serial port receiving the sensors data.
At line 6, please change '5' by the number of sensors connected. #SEE IF IT MAKES SENSE TO KEEP THIS FEATURE
Don't forget to save your changes.

Once this is done, you can start using the package.

In order to launch the package correctly, you need to use the 'roslaunch' command on the 'sensor.launch' file.
For example, if you are in the root folder, type the following command :

roslaunch src/sensor_pkg/launch/sensor.launch

Then you should see something like the following :

    $... logging to /home/lucas/.ros/log/fee8b144-f228-11ec-afcf-31e80bea7728/roslaunch-lucas-Standard-PC-Q35-ICH9-2009-2167.log
    $Checking log directory for disk usage. This may take a while.
    $Press Ctrl-C to interrupt
    $Done checking log file disk usage. Usage is <1GB.
    $
    $started roslaunch server http://lucas-Standard-PC-Q35-ICH9-2009:39259/
    $
    $SUMMARY
    $========
    $
    $PARAMETERS
    $ * /rosdistro: noetic
    $ * /rosversion: 1.15.14
    $ * /seed_fts3/port: /dev/ttyUSB0
    $ * /seed_fts3/sensor_number: 5
    $
    $NODES
    $  /
    $    seed_fts3 (sensor_pkg/read_publish_sensor_node.py)
    $
    $auto-starting new master
    $process[master]: started with pid [2177]
    $ROS_MASTER_URI=http://localhost:11311
    $
    $setting /run_id to fee8b144-f228-11ec-afcf-31e80bea7728
    $process[rosout-1]: started with pid [2187]
    $started core service [/rosout]
    $process[seed_fts3-2]: started with pid [2190]

This will run the Roscore and the main python script with the good parameters about the serial port and the number off sensors. These will run background until you press CTRL+C.

Then, you can open another terminal window. Don't forget to SOURCE it ! (source devel/setup.bash)

This is were you can start to interact with the sensors, either by sending them commands via command lines (as shown in the previous section), or by using python script and the rospy lib or C++ files with the roscpp lib.

There are 4 user code samples (in Python) to show you how to interact with the main node, how to read the messages or how to send messages.
These 4 samples will be explained in the next section. But if you, for example want to get the read data displayed, you can simply type the following command line in the new terminal window :

python3 src/sensor_pkg/user_example/user_sample_1_read_values.py

################### USER CODE SAMPLES #########################
###############################################################

As said, there are 4 user code samples for you to have to examples on how to interact with this package.
These examples are located in the catkin_ws/src/sensor_pkg/user_example folder.

The first one is user_sample_1_read_values.py. This script first sends a command to calibrate the sensors. Then it gets data from the sensors about the force on the X, Y and Z axis and display them on the terminal as they are received.

The second one is user_sample_2_abs_pitch_yaw.py. This script does the same as the first one, but instead of using the cartesian coordinates data, it uses the spherical coordinates data (abs, yaw, pitch).

The third one is user_sample_3_setfreq_calibrate.py. This script sends a command to the sensor in order to calibrate them and set the output frequency to 20Hz.

The fourth one is user_sample_4_diagnosis_request.py. This script simply sends a diagnosis request to the sensor.

The best way learn how to use the SENSOR_PKG is to play a bit with these samples and understand how to interact with the sensors data
