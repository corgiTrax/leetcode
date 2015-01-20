class Solution:
    # @param a, a string
    # @param b, a string
    # @return a boolean
    def compareVersion(self, version1, version2):
        version1_list = version1.split('.')
        version2_list = version2.split('.')
        #make them the same length
        if len(version1_list) == min(len(version1_list), len(version2_list)):
            for i in range(max(len(version1_list), len(version2_list)) - min(len(version1_list), len(version2_list))):
                version1_list.append('0')
        if len(version2_list) == min(len(version1_list), len(version2_list)):
            for i in range(max(len(version1_list), len(version2_list)) - min(len(version1_list), len(version2_list))):
                version2_list.append('0')                
       
        for i in range(min(len(version1_list), len(version2_list))):
            if int(version1_list[i]) > int(version2_list[i]):
                return 1
            elif int(version1_list[i]) < int(version2_list[i]):
                return -1
            
        return 0
