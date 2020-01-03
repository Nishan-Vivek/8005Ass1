# BCIT COMP8005 Assignment 1 - Threads and Processes
Submitted 1-18-2016

#TODO: Link to original docs

## Objective 

Use multiple processes and threads on either the Windows or Linux
operating systems and measure the performance and efficiency of each
mechanism.

## Initial Design

The assignment is composed of 3 separate small programs that perform the
same computational and I/O intensive task the same number of times. They
differ in that:

  - Program 1 is single threaded and performs the computation a number
    of times serially.

  - Program 2 is multi-threaded and performs the computation a number of
    times in parallel using threads.

  - Program 3 is multi-process and performs the computation a number
    of times in parallel using processes.



## Pseudo Code

### Single Threaded

```
START TIMER

  FOR EACH n in num\_times

  Perform\_complex\_operation()

    WRITE RESULT TO FILE

END FOR

END TIMER

PRINT TIME
```

### Multi-Threaded

```
START TIMER

FOR EACH n in num\_threads

  START THREAD -\> Perform\_complex\_operation()

    WRITE RESULT TO FILE

END FOR

FOR EACH n in num\_threads

WAIT FOR THREAD/JOIN

END FOR

END TIMER

PRINT TIME
```



### Multi-Process

```
START TIMER

FOR EACH n in num\_processes

  START PROCESS -\> Perform\_complex\_operation()

    WRITE RESULT TO FILE

END FOR

FOR EACH n in num\_processes

  WAIT FOR processes

END FOR

END TIMER

PRINT TIME

```

## Implementation 

The project was implemented in Python 2.7 and results generated on a
Windows 10 Environment. Three python programs were written. Single.py,
thread.py and process.py. For I/O activity each program wrote the
results of the computational operation to an equivalently named “.txt”
file in the working directory. Each program printed out the total time
taken to run the requested number of operations in seconds.

The computational operation used is identical in each program to allow
the results to be compared. It is adapted from the floating point prime
decomposition code example provided from the following:

[http://rosettacode.org/wiki/Prime\_decomposition\#Python:\_Using\_floating\_point](http://rosettacode.org/wiki/Prime_decomposition%23Python:_Using_floating_point)

The main changes to the example code were to hardcode the parameters and
have the results written to a file.

The test system details are as follows:

CPU: Intel I5-2500K set at 4.1ghz.

Cores: 4 Cores and 4 Logical Threads (No Hyperthreading).

RAM: 8GB DDR-1300 dual channel.

HDD: Intel 320 SSD

OS: Windows 10 x64 Pro

## Testing Methodology 

Each program was run multiple times increasing the number of operations
performed and the time recorded. The inbuilt timer function was verified
by also doing several test runs utilizing the “Measure-Command” in
Windows PowerShell to verify the time taken. The time reported from the
programs and the Measure-Command were within milliseconds of each other
with the “Measure-Command” being higher accounting for its slight
additional overheard. Because of this it is assumed the programs
self-reported computation times are accurate for the purpose of this
test.

# Test Results

|          | **Time in seconds to complete N operations.** |              |              |              |               |               |                |
| -------- | --------------------------------------------- | ------------ | ------------ | ------------ | ------------- | ------------- | -------------- |
|          | **1**                                         | **2**        | **4**        | **10**       | **50**        | **100**       | **500**        |
| single   | 0.3710000515                                  | 0.7170000076 | 1.4270000458 | 3.5880000591 | 17.8599998951 | 35.8869998455 | 179.1630001070 |
| threaded | 0.3619999886                                  | 0.7200000286 | 1.4429998398 | 3.6059999466 | 17.8910000324 | 35.7430000305 | 180.3659999370 |
| process  | 0.4100000858                                  | 0.4119999409 | 0.4260001183 | 1.0420000553 | 5.0160000324  | 10.1750001907 | 49.6420001984  |

#TODO: Chart

As can be seen from the above results there was no improvement in the
time taken to complete the operations when using Python multi-threading
in windows in fact the time taken is basically identical. As well I
observed identical CPU usage (36%) between the single and multithreaded
programs. The multi-process version however showed considerably
different behaviour. When only performing one operation is it take a
small but noticeable increase in time to complete. This is likely from
the additional overhead of starting a processes. However there is no
significant increase between running 1 – 4 threads. This is likely due
the to the processor having 4 cores. Above 4 operations the time to
complete the program does increase as each core is now running multiple
processes however the program completes orders of magnitude faster than
the single and multi-threaded versions. It appears only the
muti-processes version of the program can take advantage of the multiple
cores on the machine. Indeed observed CPU usage maxed out at 100%
compared to 36% for the other versions. Ram usage was also significantly
higher.

## Explanation

By simple observation we can see that the multi-process version is
faster because it actually launches multiple instances of the python
interpreter which can then be managed by the OS scheduler to run
simultaneous across all available hardware threads/processors. Indeed
when the multi-process version of the program is run an equivalent
number of python interpreter process entries can be seen in the windows
task manager. This allows the program to complete much quicker at the
expense of maxing out CPU usage and much higher ram usage.

To find out why the multi-threaded version of the program acted
identically to the single threaded version I was required to perform
some research. According to the following:

<https://wiki.python.org/moin/GlobalInterpreterLock>

The python interpreter is not inherently threadsafe. So when using
multiple threads are used it implements a Global Interpreter Lock. In
the case of this program the lock prevents any benefits of
multithreading to be realised. Even in situations where the GIL is not
locking the program is it known to add significant overhead.

## Execution Instructions

Extract the submitted zip file on the respective host machines and
navigate to the “App” folder. Ensure python is installed on the host
machine and has been added to the Environment PATH. The program is run
with the following commands where “n” is the number of operations to be
performed. Results will be written to corresponding txt files in the
same directory.

`python single.py n`

`python thread.py n`

`python process.py n`

This has was tested in a Windows environment however it should work in
linux and OSX as well.
