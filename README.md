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

# Rationale behind the Graph
## Early Exploration
**1.** To construct a graph, there are 2 key elements: `vertice` and `edge`. There is no doubt that each log can play the role as vertice in the graph, and its fields become attributes of the vertice. However, what can be used as the edge? Through our investigation, we have found and testified 3 kinds of relations hide in the logs, and proposed a complete structuring process

<div align="center"> <img alt="1" src="https://www.baeldung.com/wp-content/uploads/sites/4/2020/07/graphs-set.png?raw=true" width="400px"></div><br>

**2.** Generally, the only relation that we can intuitively perceive from logs is their "time" attribute. To be more specific, all logs were generated and recorded **chronologically**. In other words, there is already a "line" that strings the logs together. However, the time attribute is necessary but not sufficient

**3.** Inspired by the [SysmonTools](https://github.com/nshalabi/SysmonTools), we got to known that there is a field called `ProcessGUID` that could help gather logs which belong to the same process together.

<div align="center"> <img alt="2" src="https://camo.githubusercontent.com/8a28df54b4bc74d12fe95af2b521cd0bf47f45ff425eae51b23fc7f57c005f55/68747470733a2f2f6e6f736563757265636f64652e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031382f30372f312e706e67" width="800px"></div><br>

**4.** At first, we thought the `Time` and `ProcessGUID` are already enough for us to correlate all logs together. Nevertheless, the situation was more complex than we thought. After browsing our dataset, we found that not all logs have such field. Does that mean there are plenty of logs that do not belong to any process? Yes, but do not think that you can simply put them aside as **dissociative** ones. 

## Further Development
**1.** Let me give a quick summary of the above:
 - *The achievement is now we've found 2 relations*
 - *The problems are:
  - *Firstly, the `ProcessGUID` field actually has a low coverage which results in lots of logs remain uncorrelated*
  - *Secondly, the 2 relation we have are all limited within individual process. To be specific, we can correlate logs into a group named "process", and they could be arranged chronologically within the group. However, **what about the relation between processes?***

<div align="center"> <img alt="arango8" src="https://github.com/jayzheng98/jayzheng98.github.io/blob/master/images/syslog.png?raw=true" width="380px"></div><br>
