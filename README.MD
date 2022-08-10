# FL Studio Scripts 

Useful script(s) to automate or improve FL Studio work, file management, etc.

## flp_naming.py 

- Automated FLP naming/creation system.

  - Naming convention: MMDDYYx.
- Full directory system (based on date).

#### Usage 

Change your custom location on the script for your Projects and Template. 
Just run the script and FL will open with a new session based on your Template. 

Configure manually the data folder by going to Project Data and 
clicking on `Data Folder >> Auto`. Save your project.

To access the script faster you can add the following lines to your
.bashrc/.zshrc (on Mac). 

```bash
alias flp="python PATH_FOR_THE_SCRIPT"
```

Run the script by typing `flp` on your terminal.

### About

This script stems from years of manually creating folders and flps
following my own naming convention 
(which starts with OP, for my own music).
