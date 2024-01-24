class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t) - ord('A')] += 1
        frequencies.sort(reverse=True)
        max_frequency = frequencies[0] - 1
        idle_slots = max_frequency * n
        for i in range(1, len(frequencies)):
            idle_slots -= min(frequencies[i], max_frequency)
        return len(tasks) + max(0, idle_slots)
