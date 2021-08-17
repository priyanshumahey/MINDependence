# MINDependence


This is a repo made for the Emotivate hackathon. This project makes use of the cortex sdk and virtual brainwear. This project more or less serves as a technical demo and remains mostly unfinished

The goal of this project is to provide people with any kind of disability the capacity to use their minds for the purpose of home automation. This project makes use of pretrained mental commands to control requests the user chooses. The strength in this program lies in the control it provides the user. The aim is to let the user select the mental commands they prefer. The program itself connects to an emotiv device and through the use of the cortex.py script, it is able to provide users more control. 

The current demo version skips the home automation step for convience but it can easily be added. The current version makes use of pre-trained mental commands offered in the Virtual Brainwear device but future versions with real EEG headsets will be able to be easily trained and new mental commands will be able to be easily added.

---

The program structure currently contains a few important files that need to be run in order to be properly functional. First of all, Virtual Brainwear must be active. The user must also be able to use their secret key and own profile in order to test this.

One the necessary setup has been done, the user will first be required to open the server folder in a code editor. Then, the user needs to run app.py and open the Flask page. Afterwards, the user can run MINDependence.py. This enables the user to run the main script and make use of the actual GUI. From here, users need to enter the configure menu. There, the user needs to select the mental commands that they want to use and then need to set the corresponding ouputs. These outputs are colors but in the final version, this will be control over different smart home devices.
