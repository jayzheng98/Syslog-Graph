# Introduction
This is actually a follow-up to "[Mapping-Sysmonlogs-to-ATTACK](https://github.com/jayzheng98/Mapping-Sysmonlogs-to-ATTACK)". After you obtain the `syslog.csv` through program in that repository, you can further convert those logs into a graph structure with relations through this program
 - *I've uploaded my dataset as* `syslog.rar` *, you could directly use it for an experiment, don't worry*
 - *I also uploaded the output files based on my dataset in the* `Outputs` *directory*

# Prerequisite
 [Python3](https://www.python.org/downloads/): generate "collection" files for the graph
 
 [ArangoDB](https://www.arangodb.com/download-major/): a graph database for visualizing the log graph
<br>

# Usage
**1.** Put the `syslog.csv` in the same directory with the `syslog_correlation.py` (or change the file path in source code)

**2.** Execute the `syslog_correlation.py`. This program will automatically correlate your logs and output several files as components of a graph
<br>

# Description

<div align="center"> <img alt="arango8" src="https://github.com/jayzheng98/jayzheng98.github.io/blob/master/images/syslog.png?raw=true" width="380px"></div>
