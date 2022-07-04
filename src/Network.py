#DIMITRIOS VOURDOUGIANNIS 4326
#MOUTSOPOULOS GEORGIOS 4115

import ciw
import statistics
from collections import OrderedDict

def ciwNetwork(sim_time_secs, load_balancing, d, seed):
    N = ciw.create_network(
        arrival_distributions=[ciw.dists.Exponential(rate=1),
                                ciw.dists.NoArrivals(),
                                ciw.dists.NoArrivals(),
                                ciw.dists.NoArrivals(),
                               ciw.dists.NoArrivals(),
                               ciw.dists.NoArrivals(),
                               ciw.dists.NoArrivals(),
                               ciw.dists.NoArrivals(),
                               ciw.dists.NoArrivals()],

        service_distributions=[ciw.dists.Deterministic(value=0),
                                ciw.dists.Exponential(rate=0.125),
                                ciw.dists.Exponential(rate=0.125),
                                ciw.dists.Exponential(rate=0.125),
                               ciw.dists.Exponential(rate=0.125),
                               ciw.dists.Exponential(rate=0.125),
                               ciw.dists.Exponential(rate=0.2),
                               ciw.dists.Exponential(rate=0.2),
                               ciw.dists.Exponential(rate=0.2)],

        number_of_servers=[1, 1, 1, 1, 1, 1, 1, 1, 1],

        routing=[[0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]],
    )
    class RoutingDecision1(ciw.Node):
        def next_node (self, ind):
            min=self.simulation.nodes[2].number_of_individuals
            node_id= 2
            for i in range(3, 10):
                if(self.simulation.nodes[i].number_of_individuals<min):
                    min=self.simulation.nodes[i].number_of_individuals
                    node_id=i
            return self.simulation.nodes[node_id]  # return node id with min number of customers

    class RoutingDecision2(ciw.Node):

        def next_node(self, ind):

            Busynes = {node_id: self.simulation.nodes[node_id].number_of_individuals for node_id in range(2, 10)}  # dictionary of the nodes

            tups = list(Busynes.items())

            # reordering the nodes so fast nodes get first the customers
            reorder_list = [tups[5], tups[6], tups[7], tups[0], tups[1], tups[2], tups[3], tups[4]]
            Busyness = OrderedDict(reorder_list)
            Busyness = dict(Busyness)

            sorted_nodes = dict(sorted(Busyness.items(), key=lambda item: item[1]))

            if list(sorted_nodes.keys())[0] > 6:  # if node == fast node
                return self.simulation.nodes[list(sorted_nodes.keys())[0]]  # return this node

            else:
                for i in range(0, 10):
                    if list(sorted_nodes.keys())[i] > 6:  # if node == fast node
                        if list(sorted_nodes.values())[i] - d > list(sorted_nodes.values())[0]:  # if (fast node - d > first node)
                            return self.simulation.nodes[list(sorted_nodes.keys())[i]] # return the fast node
                        else:
                            break
            return self.simulation.nodes[list(sorted_nodes.keys())[0]] # return the first node (the slow node)

    ciw.seed(seed) # Same sequence of seed numbers for each expiriment
    utilization = []

    if load_balancing=="RoutingDecision1":
        Q = ciw.Simulation(
            N, tracker=ciw.trackers.SystemPopulation(),
            node_class=[RoutingDecision1, ciw.Node, ciw.Node, ciw.Node, ciw.Node, ciw.Node, ciw.Node, ciw.Node, ciw.Node])
        Q.simulate_until_max_time(sim_time_secs)  # sim_time_secs= 1540, 1 day for expiriment and 1 hour for warm-up
        recs = Q.get_all_records()
        waits = [r.waiting_time for r in recs if r.arrival_date > 100]  # warm-up, count after 100 timeunits
        servicetimes = [r.service_time for r in recs if r.arrival_date > 100]  # warm-up, count after 100 timeunits

        for i in range(0, 9):
            utilization.append(Q.transitive_nodes[i].server_utilisation)

        return statistics.mean(waits), statistics.mean(servicetimes), utilization  # return waiting time, service time, utilization

    elif load_balancing=="RoutingDecision2":
        Q = ciw.Simulation(
            N, tracker=ciw.trackers.SystemPopulation(),
            node_class=[RoutingDecision2, ciw.Node, ciw.Node, ciw.Node, ciw.Node, ciw.Node, ciw.Node, ciw.Node, ciw.Node])
        Q.simulate_until_max_time(sim_time_secs)  # sim_time_secs= 1540, 1 day for expiriment and 1 hour for warm-up
        recs = Q.get_all_records()
        waits = [r.waiting_time for r in recs if r.arrival_date > 100]  # warm-up, count after 100 timeunits
        servicetimes = [r.service_time for r in recs if r.arrival_date > 100]  # warm-up, count after 100 timeunits

        for i in range(0, 9):
            utilization.append(Q.transitive_nodes[i].server_utilisation)

        return statistics.mean(waits), statistics.mean(servicetimes), utilization  # return waiting time, service time, utilization


t_list = [6.314, 2.920, 2.353, 2.132, 2.015, 1.943, 1.895, 1.860, 1.833, 1.812, 1.796,
          1.782, 1.771, 1.761, 1.753, 1.746, 1.740, 1.734, 1.729, 1.725, 1.721]

def t_95_conf(sample_list, inter, i):
    t_95_conf_int = (inter[i - 2] * statistics.stdev(sample_list)) / (len(sample_list) ** (0.5))
    return t_95_conf_int

class automate():
    def loop(sim_time_secs, load_balancing, d):
        wait_list = []
        seed = [16, 3, 19, 1, 4, 9, 2, 15, 8, 12, 10, 13, 5, 17, 18, 7, 6, 14, 11, 0]  # Different seed number for each repetition of expiriment
        service_time_list = []
        utilization_list=[]

        need_more_runs = True
        runs = 0
        while need_more_runs == True:
            waits, service_times, utilization = ciwNetwork(sim_time_secs, load_balancing, d, seed[runs])
            wait_list.append(waits)
            service_time_list.append(service_times)
            utilization_list.append(utilization)

            if runs > 1:
                t = t_95_conf(wait_list, t_list, runs)
                mean = statistics.mean(wait_list)
                alpha = 0.05
                if t / mean < alpha:  # if 95% then stop
                    need_more_runs = False
            if runs == 19:  # if runs == 20 (0-19) then stop
                need_more_runs = False
            runs += 1

        return statistics.mean(wait_list), statistics.mean(service_time_list), utilization_list  # return waiting time, service time, utilization


