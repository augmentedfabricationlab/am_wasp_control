# from fabrication_manager import Task
# from extruder_control import ExtruderClient
# import time

# class EXTTask(Task):
#     def __init__(self, ext_address=("192.168.0.220", 50004), key=None):
#         super(EXTTask, self).__init__(key)
#         self.set_extruder_client(ext_address[0], ext_address[1])
#         self.function_dictionary = {
#             "send_motordata": self.ec.send_motordata,
#             "send_motorstate": self.ec.send_motorstate,
#             "send_set_do": self.ec.send_set_do,
#         }
#         self.execute_functions = []
        
#     def set_extruder_client(self, ip, port):
#         self.ec = ExtruderClient(ip, port)

#     def add_function(self, func, *args):
#         new_func = {self.function_dictionary[func]: args}
#         self.execute_functions.append(new_func)

#     def run(self, _stop_flag):
#         self._stop_flag = _stop_flag
#         self.ec.connect()
#         for func in self.execute_functions:
#             method = list(func.keys())[0]
#             args = list(func.values())[0]
#             method(*args)
#             # self.execute_functions.remove(func)
#         self.ec.close()
#         self.is_running = False
#         self.is_completed = True
#         return True


# if __name__ == "__main__":
#     exttask = EXTTask(ext_address=("192.168.0.220", 50004), key=0)
#     # exttask.add_function("send_set_do", 8, 1, True)
#     exttask.add_function("send_motordata", 1, 13500, 1000, True)
#     # exttask.add_function("send_motorstate", 0, True)
#     # exttask.add_function("send_set_do", 8, 0, True)
#     # exttask.add_function("send_motordata", 0, 24000, 1000, True)
#     exttask.run(lambda: False)
