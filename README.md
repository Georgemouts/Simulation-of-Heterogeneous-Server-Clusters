# Simulation-of-heterogeneous-server-clusters

## Problem
The purpose of this project is to understand how the distribution of client tasks to servers can be better done with different processing rate, so that overall resource utilization is maintained high.

## Solution :pencil:
To answer this question we compare two routing algorithms in a network with 1 dispatcher and 9 servers-workers the **workers 2-6 are slow nodes with average time of application completion 8 seconds** and the **workers 7-9 are fast nodes with average time of application completion 5 seconds** .The comparison conditions for the 2 algorithms are **average waiting time**, **average rate application service** , **average total node utilization** and **average utilization per node**

## Network Architecture
![alt text](https://github.com/Georgemouts/Simulation-of-Heterogeneous-Server-Clusters/blob/main/img/network.png "Network")

## Results Algorithms-Comparison :chart_with_upwards_trend:

![alt text](https://github.com/Georgemouts/Simulation-of-Heterogeneous-Server-Clusters/blob/main/img/wating_time.png " ")

![alt text](https://github.com/Georgemouts/Simulation-of-Heterogeneous-Server-Clusters/blob/main/img/service_time.png " ")

![alt text](https://github.com/Georgemouts/Simulation-of-Heterogeneous-Server-Clusters/blob/main/img/avg_total_utilization.png " ")

The result is what we expected.The second algorithm is much more efficient because it uses the fast nodes to the max 
