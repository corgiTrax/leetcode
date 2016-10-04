import sys

from itertools import combinations
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        lightIDs = range(10)
        hours = [1,2,4,8]
        minutes = [1,2,4,8,16,32]
        # get all combinations of length num:
        combs = combinations(lightIDs, num)
        times = []
        for comb in combs:
            lights = list(comb)
            hour = minute = 0
            for light in lights:
                if light <= 3: hour += hours[light]
                else: minute += minutes[light - 4]
            if hour <= 11 and minute <= 59:
                str_time = "%d:%02d" % (hour, minute)
                #if minute < 10: str_time = '{}:0{}'.format(hour, minute)
                #else: str_time = '{}:{}'.format(hour, minute)
                times.append(str_time)
        return times

# a much fancier solution online 
class Solution1(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        return ["%d:%02d" % (hour, minute) for hour in range(12) for minute in range(60) if (bin(hour) + bin(minute)).count('1') == num]

    

if __name__ == '__main__':
    sol = Solution1()
    ans = sol.readBinaryWatch(int(sys.argv[1]))
    print(ans)
