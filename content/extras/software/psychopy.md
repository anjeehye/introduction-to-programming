<h1>Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Installation" data-toc-modified-id="Installation-1">Installation</a></span><ul class="toc-item"><li><span><a href="#macOS" data-toc-modified-id="macOS-1.1">macOS</a></span></li><li><span><a href="#Windows" data-toc-modified-id="Windows-1.2">Windows</a></span></li><li><span><a href="#Linux" data-toc-modified-id="Linux-1.3">Linux</a></span></li></ul></li><li><span><a href="#Test" data-toc-modified-id="Test-2">Test</a></span></li></ul></div>

# Psychopy

Psychopy is an additional package for Python that allows you to write programs that control the screen, keyboard, mouse, etc. in order to gather psychophysical data from users/subjects. You can read more about it at the [Psychopy website](https://www.psychopy.org).

## Installation

Because Psychopy needs to take some control over your computer's hardware, it is slightly more difficult to install. Because of Psychopy's special requirements, installing it can occasionally mess with the configuration of other installed Python packages. To avoid this problem, you can install Psychopy into its own 'virtual environment'. A virtual environment is a separate Python setup that stores its own configuration and versions of packages. If we install Psychopy into its own environment rather than in the main environment that you use for other Python tasks, we can minimize the risk that it may break other programs.

Follow the instructions for your operating system.

### macOS

Search for an application called the 'Terminal'. This is a command line where you can type in commands for your computer's operating system.

You will need first a piece of software called 'command line tools' for mac. You might already have it, as it is used by various other programs that you might have installed already. You can check by entering the following command in the terminal:

```
xcode-select --install
```

If you see a message telling you that this is already installed, then you are ready to move on. Otherwise, your computer will offer to install the command line tools. Answer 'yes' or 'ok' to any windows that pop up offering to install software.

Now follow the same instructions as for **Windows** below.

### Windows

It is probably a good idea to first close any open instances of the Anaconda Navigator or Spyder. The Anaconda Navigator will probably only recognize the changes you are about to make after it has been closed and then restarted. Now search for an application called 'Anaconda Prompt' (or if you are coming here from the **macOS** instructions above, continue in the 'Terminal' application).

The steps below involve typing text commands into the command prompt. When you type the commands in the instructions below, beware that the command prompt is not particularly forgiving. If something is slightly mistyped, the prompt may tell you that a command is not found, or syntax is not correct. Check things carefully if you encounter error messages. This includes the distinction between lowercase and UPPERCASE and the accidental placement of a space in front of the command if you copy and paste it.

First you need to find out which directory on your computer you are working in. The command prompt should show which directory you are in. For example, you might see something like:

```
(base) C:\Users\mildred>
```

In this case, `C:\Users\mildred` is the directory that you are in. If you don't see anything like this, or if you are not sure which directory this points to, you can try typing in a command that will display the name of the directory. If you are on **Windows**, type `cd`. If you are on **macOS**, type `pwd`. You should then see the name of a directory printed out. Make a note of it and then go find it in your file explorer.

The makers of Psychopy provide a file that Anaconda can use to create the necessary environment for Psychopy to run in. Download the file (called *psychopy-env.yaml*) by right-clicking on [this link](https://raw.githubusercontent.com/psychopy/psychopy/master/conda/psychopy-env.yml) and choosing 'Save Link As' or something similar, and make sure you download it into the directory that you saw displayed in the Anaconda Prompt above.

Now return to the command prompt and enter the following command (as described on the [Psychopy website](https://www.psychopy.org/download.html#anaconda-and-miniconda)):

```
conda env create -n psy -f psychopy-env.yml
```

This will create the necessary virtual environment under the name 'psy'. Now enter the following command:

```
conda activate psy
```

This 'activates' the new environment, so that any subsequent commands that you enter will take effect for this environment only. You should see that the prompt is now prefaced with the name of the 'psy' environment. Something like this:

```
(psy) C:\Users\mildred>
```

In order to be able to use Spyder to write Python programs in this new environment, you should also install Spyder into the 'psy' environment. Enter the following command, and it will be installed into this environment:

```
conda install spyder
```

When the installation has finished, you have finished setting up the environment and you can close the command prompt window.

You will now have two environments in your Anaconda installation. One is called 'base', which is the default environment that was already created when you installed Anaconda. The other is called 'psy', and is the one in which you just installed Psychopy. When you want to write Python programs that use Psychopy, instead of launching Spyder directly, first launch an application called 'Anaconda Navigator'. This is the main graphical interface to Anaconda. At the top of the 'Home' tab, you should see a drop-down selection menu titled 'Applications on:' This menu allows you to switch between virtual environments. To switch into the new virtual environment, select 'psy' from this drop-down menu. The Anaconda Navigator may take a moment to switch environments. Once it has done so and you see 'psy' selected, find Spyder among the applications listed there, and click on 'Launch' to launch Spyder in the 'psy' environment.

### Linux

You will need first to install a Python program for creating virtual environments. It is called 'virtualenv' and you can get it via your normal package manager. Make sure that you get the Python 3 version. Assuming you are on Ubuntu, the following command in the terminal will install it:

```shell
sudo apt-get install python3-virtualenv
```

Once you have installed virtualenv, you can use it as a command in the terminal to create virtual environments. First use `cd` to navigate into the directory where you would like to store your virtual environment (or just open the terminal there by right-clicking on the directory in the file explorer and selecting 'Open in Terminal'). Then enter the following command to create a virtual environment in which to install Psychopy:

```shell
virtualenv --python /usr/bin/python3 psy
```

The `--python` option with the path to the Python 3 interpreter `/usr/bin/python3` ensures that the environment will be a Python 3 environment and not Python 2. And 'psy' is the name of the environment.

(Note that it is generally not a good idea to call your virtual environment by the same name as a Python package, as Python may then try to import the contents of the virtual environment whenever you instruct it to import the package with the same name. This is why you should opt for a name other than 'psychopy' for your virtual environment.)

Still in the terminal, enter the following command to activate the virtual environment:

```shell
source psy/bin/activate
```

This runs a short file in the virtual environment directory that makes subsequent commands in that terminal session take effect in that environment only.

Now use the Python package manager program (pip) to install Psychopy. If you want to write your Psychopy programs using Spyder, you should also install Spyder into the new environment:

```shell
pip install psychopy spyder
```

Finally, to launch Spyder in the new environment, just enter the following command:

```shell
spyder3
```

To quit the virtual environment, you can just close the terminal window. Whenever you want to write Python programs that make use of Psychopy, just open the terminal in the directory where you created the virtual environment and enter the command to activate it, followed by the command to launch Spyder:

```shell
source psy/bin/activate
spyder3
```

The directory 'psy' that contains the files for the virtual environment is a directory like any other. If you ever want to delete your virtual environment, just delete the 'psy' directory. And if you want to move it somewhere else in your file system, just move the 'psy' directory.

Some more information about virtual environments is provided at the [Hitchhiker's Guide to Python](https://docs.python-guide.org/dev/virtualenvs/#basic-usage).

## Test

Once you have followed the instructions above for your operating system and you have launched Spyder in the 'psy' environment, you can check whether Psychopy works correctly. Try some Psychopy commands in the Spyder console.

First try importing its main modules:


```python
from psychopy import visual, core, event
```

If you do not see a `ModuleNotFoundError`, then Psychopy has at least been installed and can be imported. You might see a few warning messages, the exact content of which will depend on your computer, but these do not necessarily indicate a problem.

Now you can try to open a new window on your screen using Psychopy. The `Window()` function from the `visual` module does this. It is very important to make sure that you assign the result into a variable, as it is via this variable that you will be able to continue doing things with the window. If you open a window but do not assign it into a variable, you have no way of continuing to interact with the window from Python, and you might not even be able to close it.


```python
win = visual.Window()
```

You should see a new small blank window appear.

Finally, you can try drawing some text in the window. Try the following two commands:


```python
visual.TextStim(win).draw()
win.flip()
```




    2.3026592579999487



You will see a number output from the second command. How these two commands work and what this number means will be explained when we come to learn about Psychopy. For now, just try the commands out. You should see some text drawn into the window as a result.

Finally, to close the window, don't try to close it by clicking its close button as you would for a normal window. This usually won't work. Instead, close it from the Spyder console by calling the `close()` method.


```python
win.close()
```

    1.6359 	WARNING 	Monitor specification not found. Creating a temporary one...


The window should now have disappeared. You might again see a short warning message like the one above. This is not important.

If all of that worked out, then Psychopy is installed correctly and its most important features are working.
