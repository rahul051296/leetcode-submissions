class Solution:
    def originalDigits(self, s: str) -> str:
        
        count = collections.Counter(s)
        
        mapping = {}
        mapping["0"] = count["z"]
        mapping["2"] = count["w"]
        mapping["4"] = count["u"]
        mapping["6"] = count["x"]
        mapping["8"] = count["g"]
        
        mapping["3"] = count["h"] - mapping["8"]
        mapping["5"] = count["f"] - mapping["4"]
        mapping["7"] = count["s"] - mapping["6"]
        
        mapping["9"] = count["i"] - mapping['5'] - mapping['6'] - mapping['8']
        mapping['1'] = count["n"] - mapping["7"] - 2 * mapping["9"]
        
        output = []
        for key in sorted(mapping.keys()):
            output.append(key*mapping[key])
            
        return "".join(output)