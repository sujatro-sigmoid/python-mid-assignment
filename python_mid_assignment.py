# Sujatro Majumder - Design Logger System - Sigmoid python mid-assessment

class Logger:
    def __init__(self):
        # hash table of k = message, v = timestamp
        self.hash_table = dict()

    def shouldPrintMessage(self, timestamp, message):
        if message not in self.hash_table:
            self.hash_table[message] = timestamp
            return True

        prev_timestamp = self.hash_table[message]
        if prev_timestamp + 10 <= timestamp:
            self.hash_table[message] = timestamp
            return True

        return False


log = Logger()
queries = [[1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
for q in queries:
    print(f"For timestamp:{q[0]} and message:{q[1]} output:{log.shouldPrintMessage(q[0],q[1])}")
