# Sujatro Majumder - Design Logger System - Sigmoid python mid-assessment
class LoggerException(Exception):
    pass
class InvalidTypeError(LoggerException):
    pass
class TimestampsNotInOrderError(LoggerException):
    pass

class Logger:
    def __init__(self):
        # hash table of k = message, v = timestamp
        self.hash_table = dict()

    def should_print_message(self, timestamp, message):
        if message not in self.hash_table:
            self.hash_table[message] = timestamp
            return True

        prev_timestamp = self.hash_table[message]
        if prev_timestamp + 10 <= timestamp:
            self.hash_table[message] = timestamp
            return True

        return False

    def answer_stream(self, queries):
        ans = list()
        prev_timestamp = 0
        for q in queries:
            if type(q[0]) is not int or type(q[1]) is not str:
                raise InvalidTypeError('invalid data types')
            elif q[0] < prev_timestamp:
                raise TimestampsNotInOrderError('timestamps in the stream of inputs are not in order')
            else:
                prev_timestamp = q[0]

        for q in queries:
            ans.append(self.should_print_message(q[0], q[1]))
        return ans


# log = Logger()
# queries = [[1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
# for q in queries:
#     print(f"For timestamp:{q[0]} and message:{q[1]} output:{log.should_print_message(q[0], q[1])}")
