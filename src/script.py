#DIMITRIOS VOURDOUGIANNIS 4326
#MOUTSOPOULOS GEORGIOS 4115
import Network
import matplotlib.pyplot as plt

d = [0, 1, 2, 3, 4, 5, 6, 7]
load_balancing = ["RoutingDecision1", "RoutingDecision2"]
sim_time_secs = 1540
seed = [16, 3, 19, 1, 4, 9, 2, 15, 8, 12, 10, 13, 5, 17, 18, 7, 6, 14, 11, 0]

f = open('results.txt', 'w')
f.write('==========================================================\n')
f.write('=========== Simulation inviroment and hardware ===========\n')
f.write('==========================================================\n\n')
f.write('OS: Microsoft Windows 10 Home\nCpu: intel core i5-7200U 2.5 GHz\n'
        'Processor(s): 1 Processor(s) Installed. [01]: Intel64 Family 6 Model 142 Stepping 9 GenuinelIntel ~2700Mhz\n'
        'System Type: x64-based PC\nRAM: 8 GB\nVirtual Memory: Max Size: 14,166 MB\n'
        'Virtual Memory: Available: 3,422 MB\nVirtual Memory: In Use: 10,744 MB\nDisk storage: 250 GB \n')
f.write('\n==============================================================\n')
f.write('====================== Input Parameters ======================\n')
f.write('==============================================================\n\n')

f.write('sim_time_secs: ' + str(sim_time_secs) + '\nload_balancing = ' + str(load_balancing) + '\nd = ' + str(d) + ' \n')

f.write('For the network (N): \n\n')
f.write('arrival_distributions=[ciw.dists.Exponential(rate=1), ciw.dists.NoArrivals(), '
        'ciw.dists.NoArrivals(),\n ciw.dists.NoArrivals(), ciw.dists.NoArrivals(), ciw.dists.NoArrivals(),\n '
        'ciw.dists.NoArrivals(), ciw.dists.NoArrivals() ,ciw.dists.NoArrivals()],\n\n')
f.write('service_distributions=[ciw.dists.Deterministic(value=0), ciw.dists.Exponential(rate=0.125), '
        'ciw.dists.Exponential(rate=0.125),\n ciw.dists.Exponential(rate=0.125), ciw.dists.Exponential(rate=0.125), '
        'ciw.dists.Exponential(rate=0.125),\n ciw.dists.Exponential(rate=0.2), ciw.dists.Exponential(rate=0.2), '
        'ciw.dists.Exponential(rate=0.2)],\n\n')
f.write('number_of_servers=[1, 1, 1, 1, 1, 1, 1, 1, 1],\n\n')
f.write('routing=[[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0] ,[0, 0, 0, 0, 0, 0, 0, 0, 0],\n '
        '[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],\n '
        '[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]],\n')
f.write('\n=====================================================\n')
f.write('====================== Results ======================\n')
f.write('=====================================================\n')

# For Routing Decision 1 algorithm
wait, service, utilization = Network.automate.loop(sim_time_secs, load_balancing[0], d[0])

node1_util=0
node2_util=0
node3_util=0
node4_util=0
node5_util=0
node6_util=0
node7_util=0
node8_util=0
node9_util=0
c=0

for nodes in utilization:
    node1_util += nodes[0]
    node2_util += nodes[1]
    node3_util += nodes[2]
    node4_util += nodes[3]
    node5_util += nodes[4]
    node6_util += nodes[5]
    node7_util += nodes[6]
    node8_util += nodes[7]
    node9_util += nodes[8]
    c+=1

# Utilization for each node
node1_util=node1_util/c
node2_util=node2_util/c
node3_util=node3_util/c
node4_util=node4_util/c
node5_util=node5_util/c
node6_util=node6_util/c
node7_util=node7_util/c
node8_util=node8_util/c
node9_util=node9_util/c

# Average total Utilization
sum_of_util = (node2_util + node3_util + node4_util + node5_util + node6_util + node7_util + node8_util + node9_util) / 8

f.write('\nAlgorithm RoutingDecision1: \n Waiting_time: ' + str(wait)+'\t Service_time: ' + str(service) + '\t Average total Utilization: '+str(sum_of_util) + ' \n Utilization for node 1: '+str(node1_util) +
        '\t Utilization for node 2: ' + str(node2_util) + '\t Utilization for node 3: ' + str(node3_util) + '\n Utilization for node 4: '+ str(node4_util) + '\t Utilization for node 5: ' + str(node5_util) +
        '\t Utilization for node 6: ' + str(node6_util) + '\n Utilization for node 7: ' + str(node7_util) + '\t Utilization for node 8: '+ str(node8_util) + '\t Utilization for node 9: ' + str(node9_util) + '\n')

wait1_list = []
service1_list = []
total_util1 = []
for i in range(len(d)):
    wait1_list.append(wait)
    service1_list.append(service)
    total_util1.append(sum_of_util)

# For Routing Decision 2 algorithm
wait_plot_list = []
service_plot_list = []
utilization_plot_list = []
for i in d:
    wait, service, utilization = Network.automate.loop(sim_time_secs, load_balancing[1], i)
    wait_plot_list.append(wait)
    service_plot_list.append(service)

    node1_util = 0
    node2_util = 0
    node3_util = 0
    node4_util = 0
    node5_util = 0
    node6_util = 0
    node7_util = 0
    node8_util = 0
    node9_util = 0
    c = 0

    for nodes in utilization:
        node1_util += nodes[0]
        node2_util += nodes[1]
        node3_util += nodes[2]
        node4_util += nodes[3]
        node5_util += nodes[4]
        node6_util += nodes[5]
        node7_util += nodes[6]
        node8_util += nodes[7]
        node9_util += nodes[8]
        c += 1

    # Utilization for each node
    node1_util = node1_util / c
    node2_util = node2_util / c
    node3_util = node3_util / c
    node4_util = node4_util / c
    node5_util = node5_util / c
    node6_util = node6_util / c
    node7_util = node7_util / c
    node8_util = node8_util / c
    node9_util = node9_util / c

    # Average total Utilization
    sum_of_util = (node2_util + node3_util + node4_util + node5_util + node6_util + node7_util + node8_util + node9_util) / 8

    utilization_plot_list.append(sum_of_util)
    f.write('\nAlgorithm RoutingDecision2 (D='+str(i)+'): \n Waiting_time: ' + str(wait) + '\t Service_time: ' + str(service) + '\t Average total Utilization: ' + str(sum_of_util) + ' \n Utilization for node 1: ' +
            str(node1_util) + '\t Utilization for node 2: ' + str(node2_util) + '\t Utilization for node 3: ' + str(node3_util) + '\n Utilization for node 4: ' + str(node4_util) + '\t Utilization for node 5: ' +
            str(node5_util) + '\t Utilization for node 6: ' + str(node6_util) + '\n Utilization for node 7: ' + str(node7_util) + '\t Utilization for node 8: ' + str(node8_util) + '\t Utilization for node 9: '+ str(node9_util) + '\n')

# Plots for Routing Decision 2 algorithm
# Plot for mean waiting time
plt.scatter(d, wait_plot_list)
plt.plot(d, wait_plot_list)
plt.xlabel('d')
plt.ylabel('Mean waiting time (second)')
plt.title('Algorithm 2 - Waiting_time for each d')
plt.ylim(ymin=0)
plt.legend(['Algorithm 2'])
plt.show()

# Plot for mean service time
plt.scatter(d, service_plot_list)
plt.plot(d, service_plot_list)
plt.xlabel('d')
plt.ylabel('Mean service time (second)')
plt.title('Algorithm 2 - Service_time for each d')
plt.ylim(ymin=0)
plt.ylim(ymax=4.0)
plt.legend(['Algorithm 2'])
plt.show()

# Plot for mean total utilization
plt.scatter(d, utilization_plot_list)
plt.plot(d, utilization_plot_list)
plt.xlabel('d')
plt.ylabel('Mean Total utilization')
plt.title('Algorithm 2 - Avg Total utilization for each d')
plt.ylim(ymin=0)
plt.ylim(ymax=1.0)
plt.legend(['Algorithm 2'])
plt.show()


# Plots for comparsion between 2 algorithms
# Plot for mean waiting time
plt.scatter(d, wait1_list,color='r')
plt.scatter(d, wait_plot_list, color='g')
plt.plot(d, wait1_list, color='r', label='Algorithm 1')
plt.plot(d, wait_plot_list, color='g', label='Algorithm 2')
plt.xlabel('d')
plt.ylabel('Mean waiting time (second)')
plt.title('Waiting_time for each d')
plt.ylim(ymin=0)
plt.legend(['Algorithm 1', 'Algorithm 2'])
plt.show()

# Plot for mean waiting time # with zoom
plt.scatter(d, wait1_list,color='r')
plt.scatter(d, wait_plot_list, color='g')
plt.plot(d, wait1_list, color='r', label='Algorithm 1')
plt.plot(d, wait_plot_list, color='g', label='Algorithm 2')
plt.xlabel('d')
plt.ylabel('Mean waiting time (second)')
plt.title('Zoom in the difference between 2 algorithms waiting_time for each d')
plt.ylim(ymin=0)
plt.ylim(ymax=5.0)
plt.legend(['Algorithm 1', 'Algorithm 2'])
plt.show()

# Plot for mean service time
plt.scatter(d, service1_list, color='r')
plt.scatter(d, service_plot_list, color='g')
plt.plot(d, service1_list, color='r', label='Algorithm 1')
plt.plot(d, service_plot_list, color='g', label='Algorithm 2')
plt.xlabel('d')
plt.ylabel('Mean service time (second)')
plt.title('Service_time for each d')
plt.ylim(ymin=0)
plt.ylim(ymax=4.0)
plt.legend(['Algorithm 1', 'Algorithm 2'])
plt.show()

# Plot for mean total utilization
plt.scatter(d, total_util1, color='r')
plt.scatter(d, utilization_plot_list, color='g')
plt.plot(d, total_util1,color='r', label='Algorithm 1')
plt.plot(d, utilization_plot_list, color='g', label='Algorithm 2')
plt.xlabel('d')
plt.ylabel('Mean Total utilization')
plt.title('Avg Total utilization for each d')
plt.ylim(ymin=0)
plt.ylim(ymax=1.0)
plt.legend(['Algorithm 1', 'Algorithm 2'])
plt.show()

f.close()