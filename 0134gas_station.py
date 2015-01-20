#Solution 1 has a O(n^2) worst case complexity, which causes time limit exceeding
class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        n = len(gas) #number of gas stations

        for start_station in range(n):
            #start at station i
            cur_station = start_station
            cur_gas = gas[cur_station]
            complete = False

            #begin trip
            while not complete:
                cur_gas -= cost[cur_station]
                if cur_gas < 0:
                    break
                else: 
                    cur_station = (cur_station + 1) % n
                    cur_gas += gas[cur_station]
                    if cur_station == start_station:
                        return start_station

        return -1   
            

'''Solution 2 requires some mathematical thinking, but it is O(n)
We can prove that, if station_k is the maximum cumulative deficit,
we should start at station_k + 1
'''        
class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        cum_gas, cum_cost, max_deficit, station = 0, 0, 0, 0
        for i in range(len(gas)):
            cum_gas += gas[i]
            cum_cost += cost[i]
            deficit = cum_cost - cum_gas
            if deficit > max_deficit:
                max_deficit = deficit
                station = i
        
        if cum_gas < cum_cost:
            return -1
        
        #if there is solution, it should be station + 1
        station += 1
        
        return station % (len(gas))               
