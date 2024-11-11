# **Prefect Certification Course Tech Setup**

### **Course Slack channel**

* Please ensure that you are in the course Slack channel. We will share resources there.

### **Internet access**

* Please ensure that your laptop can use Wi-Fi to access and download files from GitHub and install packages from PyPI via pip.

### **Accounts required**

* [Prefect Cloud account](https://app.prefect.cloud/)    
* [GitHub account](https://github.com/)

### **Editor** 

* Please install a code editor prior to the start of instruction \- [Visual Studio Code (VS Code)](https://code.visualstudio.com/) is recommended. Any code editor you are comfortable with is fine.

### **Set up your environment**

* We suggest using a virtual environment to isolate your dependencies when working in the course.  
* For instructions to set up a virtual environment with conda or venv, see [this GitHub Gist](https://gist.github.com/discdiver/0bb3bf96f02c182f96d45278f9564551).

* ### Make sure you have Python 3.9 or newer installed in your environment.

### **Install Prefect**

* In the terminal with your virtual environment activated, run *pip install \-U prefect* to install or upgrade the most recent Prefect version.  
* See the versions of important Prefect-related components in your system by running the command *prefect version*  
* If you don’t see any results, Prefect is not installed in your active environment. You may need to activate your virtual environment.  
* If you have any issues installing Prefect, see the docs at [docs.prefect.io/latest/getting-started/installation/](https://docs.prefect.io/latest/getting-started/installation/)

### **Test Prefect setup**

1\. Create a file named [*flowtest.py*](http://flowtest.py) with the following contents:

import httpx  
from prefect import flow

@flow  
def test\_flow():  
    res \= httpx.get("[https://example.com](https://example.com)")  
    print(res)

if \_\_name\_\_ \== "\_\_main\_\_":  
    test\_flow()

2\. Execute [*flowtest.py*](http://flowtest.py) by running *python flowtest.py* in your virtual environment. You should see *\<Response \[200 OK\]\>* 

### **Install Docker**

Install [Docker](https://www.docker.com/) on your machine. Docker will be used in the latter portion of the course. If you don’t have Docker installed that’s okay. You will have other options for running workflows.

### **If taking a live online course, set up Zoom** 

Install Zoom and give Zoom access so that you can share your screen in breakout rooms. Instructions are [here](https://support.zoom.us/hc/en-us/articles/201362153-Sharing-your-screen-or-desktop-on-Zoom). You will have to exit out of Zoom after giving access, so it’s best to do this before the course starts.

If you have any issues, please reach out in the course Slack channel. We look forward to seeing you in the course\!