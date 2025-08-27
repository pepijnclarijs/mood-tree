# mood-tree
Mobile app that helps the user track their mood over time.

# Setup
There are a couple of steps to take to stream the app to your phone for development. 

## Step 1: Setup a connection between the phone and the computer
We can setup a connection using adb (android debugging bridge) between a phone and the computer. 
This involves a couple of extra steps when you are on WSL. 

### Step 1.1: Download adb on Windows
Install the latest adb cli tool on windows. Can be done using winget.

### Step 1.2: Download adb on WSL
Install the latest adb cli tool on WSL via the terminal. Can be done with apt.

### Step 1.3: Connect phone via USB and setup developer tools settings on phone
The connection can be streamed wirelessly, but this connection must be setup first. This can be done
by first plugging in the phone via usb and running some commands with the right settings. Make sure
your phone is connected to the same wifi as your computer.

Settings on your phone:
There is some hacky thing where you can enable developer settings on your phone by navigating to
the system information and pressing the build number 7 times. When enabled, you must enable the 
option to allow for debugging.

### Step 1.4: Connect adb to phone
Open up a powershell terminal and run ```adb tcpip 5555```. Then run ```adb kill-server``` followed 
by ```adb start-server```. Then connect your phone by running 
```adb connect <your_phone_ip>:5555```. There should be a pop up on your phone prompting to allow 
the connection. Allow it and run `adb devices`. This should show a connected device via the 5555 port. This means a successful connection is possible. To now unplug your phone safely, you must likely first terminate the adb task by running `adb kill-server`. If that's not enough and you still get a popup stating that some program is using your phone when you try to safely unpug it, try running: `taskkill /IM adb.exe /F`. 

### Step 1.5: Connect adb on WSL to phone
Finally, pull up a terminal on wsl and run `adb connect <your_phone_ip>:5555`. To be honest I am actually not sure if step 1.4 is needed, but this is the workflow I went through and it worked in the end. By the way, if the connection is unauthorized, there is an option on your phone in the developer options that say something like forget previous authorizations. You can try that option and retry making a connection. 

### Step 1.6: Run the app
Final finally, we can run the app and stream it to our phone by running `uv run kivy-reloader run`. Note that we first must have run `uv run kivy-reloader init` and configure the kivy-reloader.toml file. The `uv run kivy-reloader run` command will take 10 to 15 minutes the first time you run it. Subsequent request should not take long (a couple seconds or something?).