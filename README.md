<a name="readme-top"></a>
# FIM Suite

TABLE OF CONTENTS
   * [Project Tracker](#project-tracker)
   * [Environments Used](#environments-used)
   * [Program Walkthrough](#program-walkthrough)
      * [Powershell](#powershell)
      * [Python](#python)   

### Project details
This is an effort to emulate FIM tools and better understand how they operate. Depending on the OS environment being monitored, a different solution may be required so I wanted to create different implementations. Starting with two scripting languages I am most familiar with, <b>PowerShell</b> and <b>Python</b>.<br>


---

### Project Tracker

<b>Python</b>

```
captureTheHash.py
hashIt.py
checkHashedFiles.py
```

> PLEASE NOTE - SHA1 was only chosen for its speed. Depending on whats being hashed, I would choose SHA2, Argon2 etc. in a production environment.

| Feature | Status | Notes |
|:--- | :---: |:--- |
| Main .py for capturing files | ✅ | |
| Separate hashing module file | ✅ | I could not find a good way to check the files containing hashes so I created a seperate .py program to do this|
| Capture file changes | ✅ | This feature is 🍝 code for sure. Theres a Python API out there called watchdog. It monitors files in a similar fashion to my Powershell implementation. Much easier but I wanted to create a solution from scratch. It isnt optimal, but it does work |

<b>Powershell</b>

```captureTheHash.ps1```

| Feature | Status | Notes |
|:--- | :---: |:--- |
| Track file creation  | ✅  |  |
| Track file changes  | ✅ |
| Track file deletion  | ✅ |

---

### Environments Used

- Windows 10
- Windows Powershell ISE
- PyCharm

---

### Program Walkthrough:

#### POWERSHELL

<p align="center">
1 - launch the program and make sure you are in the directory to be monitored:
<img alt="start program" width="auto" height="300" src="https://user-images.githubusercontent.com/54426511/208581806-ee57bf07-3dc0-4025-87d2-8f33a97b5776.PNG">
</p>
<p align="center">
2 - Choose an action:
<img alt="program action" width="auto" height="300" src="https://user-images.githubusercontent.com/54426511/208582525-4d65a565-2c3f-4e88-9db7-09364ef861c8.PNG">
</p>
<p align="center">
3 - Program enters monitoring mode, 1 of 3 actions are captured: File changes, new files or file removals
</p>
<p align="center">
File Changes. This alert continues until the original file is restored. I just added additional text to change the hash value 
<img alt="file change alert" width="auto" height="300" src="https://user-images.githubusercontent.com/54426511/208582952-ce363dcd-1373-4350-bb37-277e6fc7bd60.PNG">
</p>
<p align="center">
File Creation. This alert continues until the new file is removed from the baseline folder or a new baseline is captured which is option 'A' in the program.
<img alt="file creation alert" width="auto" height="300" src="https://user-images.githubusercontent.com/54426511/208583783-723305da-881c-419d-af25-6c4bf39d565f.PNG">
</p>
<p align="center">
File Deletion. This alert can trigger if files in the baseline are deleted or simply moved from the directory being tracked 
<img alt="file deletion alert" width="auto" height="300" src="https://user-images.githubusercontent.com/54426511/208583945-c01711ed-15d2-4fbe-946a-a24063641617.PNG">
</p>

---

#### PYTHON

<p align="center">
1 - Verify .py files and import modules
<img alt="python program start" width="auto" height="300" src="https://user-images.githubusercontent.com/54426511/208584525-614600d0-1185-4c76-9f6d-4f01bd849df2.PNG">
</p>
<p align="center">
2 - Bulk of capture file
<img alt="python program start" width="auto" height="400" src="https://user-images.githubusercontent.com/54426511/208781722-38c5a377-2d8a-48f4-b3d6-91ea612a2f35.PNG">
</p>
<p align="center">
3 - Locate directory to monitor and run `captureTheHash.py`
  
<img alt="python program start" width="auto" height="300" src="https://user-images.githubusercontent.com/54426511/208777350-7e41e2fb-cb46-4d6d-bda6-88def2527a75.PNG">
</p>
<p align="center">
4 - I run the program twice. This generates two new files with hashes. One for storage and one to compare for any changes
</p>
<p align="center">
<img alt="python program start" width="auto" height="100" src="https://user-images.githubusercontent.com/54426511/208819595-e0aedef4-010f-43a2-8fa3-db5a891c4247.PNG">
<img alt="python program start" width="auto" height="100" src="https://user-images.githubusercontent.com/54426511/208819594-3762814c-1b40-4146-b1dc-ddb7acac72f1.PNG">
</p>
<p align="center">
5 - Testing `testA.txt`. The following is the original content and the files current hash
</p>
<p align="center">
<img alt="python program start" width="auto" height="100" src="https://user-images.githubusercontent.com/54426511/208820170-1b6355e2-decb-49c6-b316-b1eb1f107b35.PNG">
<img alt="python program start" width="auto" height="100" src="https://user-images.githubusercontent.com/54426511/208820174-811c3042-49f0-43cb-a4f3-a0d415cc3cbd.PNG">
</p>
<p align="center">
6 - Run new program to check each hash in both files for a 1 to 1 match or mismatch
<img alt="python program start" width="auto" height="300" src="https://user-images.githubusercontent.com/54426511/208821010-4681d2c4-4f00-4cd1-aae3-d9509bd38bd9.PNG">
</p>
<p align="center">
7 - Change the file content and re-run program to get new hash value (NOTE the different file `check_stored_hashes.txt` as this will be mapped against the stored file)
</p>
<p align="center">
<img alt="python program start" width="auto" height="auto" src="https://user-images.githubusercontent.com/54426511/208820821-2544cf52-7da6-490d-b12b-52b49f02b923.PNG">
<img alt="python program start" width="auto" height="100" src="https://user-images.githubusercontent.com/54426511/208821441-f55ab84c-d057-4d41-a599-b0e36916fe51.PNG">
</p>
<p align="center">
8 - 🥁 Drumroll please..... Re-run the hash check program, and you can see that `testA.txt` has a different hash value. Call the SOC team, we have lost File Integrity! 😎 
<img alt="python program start" width="auto" height="300" src="https://user-images.githubusercontent.com/54426511/208821915-2258a94c-1c10-4556-b4c3-2644abb4a38f.PNG">
</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>
