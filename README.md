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
```

> PLEASE NOTE - SHA1 was only chosen for its speed. This is a cryptographically broken hash function and I would NOT use, or recommend this in production environments

| Feature | Status | Notes |
|:--- | :---: |:--- |
| Main .py for capturing files | ✅ | |
| Separate hashing module file | ✅ | |
| Notification and/or reporting system on changes | ⚙ | |

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
<img alt="python program start" width="auto" height="300" src="https://user-images.githubusercontent.com/54426511/208776442-c533f9de-6c26-4fa6-bd9f-d529a064c3e3.PNG">
</p>
<p align="center">
3 - Locate directory to monitor and run captureTheHash.py
<img alt="python program start" width="auto" height="300" src="https://user-images.githubusercontent.com/54426511/208777350-7e41e2fb-cb46-4d6d-bda6-88def2527a75.PNG">
</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>
# fimsuite
