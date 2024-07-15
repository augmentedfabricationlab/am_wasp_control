from fabrication_manager.task import Task
from extruder_control_wasp import ExtruderClient
import time



class EXTTaskJL(Task):
    #def __init__(self, ext_address=("192.168.125.22", 50004), key=None):
    def __init__(self, host = None, port = None, key=None):
        super(EXTTaskJL, self).__init__(key)
        self.client = ExtruderClient(host, port)
        # self.set_extruder_client(ext_address[0], ext_address[1])
        #self.function_dictionary = {
            #"send_motordata": self.ec.send_motordata,
            #"send_motorstate": self.ec.send_motorstate,
            #"send_set_do": self.ec.send_set_do,
        #}
        #self.execute_functions = []
        
    # def set_extruder_client(self, ip, port):
    #     self.ec = ExtruderClient(ip, port)

    #def add_function(self, func, *args):
        #new_func = {self.function_dictionary[func]: args}
        #self.execute_functions.append(new_func)
    	
    def content(self):
        # To be executed in sequence, from the self.execute_functions list
        ## Can override with your own instructions instead
        #for func in self.execute_functions:
            #method = list(func.keys())[0]
            #args = list(func.values())[0]
            #method(*args)
        future = self.client.connect()
        return future

    def run(self, stop_thread):
        future = self.content()
        if future is None:
            raise ValueError("future is None, please set a command to wait for")
        while not future.done:
            if stop_thread():
                self.log("Forced to stop...")
                #self.robot.abb_client.send(rrc.Stop())
                self.is_running = False
                self.is_completed = False
                break   
        else:
            self.is_completed = True
            return True


#if __name__ == "__main__":
    #exttask = EXTTask(ext_address=("192.168.125.22", 50004), key=0)
    #exttask.add_function("send_set_do", 8, 1, True)
    #exttask.add_function("send_motordata", True, 10000, 10000, True)
    #exttask.add_function("send_motorstate", 0, True)
    # exttask.add_function("send_set_do", 8, 0, True)
    # exttask.add_function("send_motordata", 0, 24000, 1000, True)
    #exttask.run(lambda: False)
