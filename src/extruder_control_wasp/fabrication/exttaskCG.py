from fabrication_manager.task import Task
from extruder_control_wasp import ExtruderClient
import time

from threading import Thread

class ExtruderTask(Task):
    def __init__(self, key, host="192.168.125.22", port=50004 ):
        super(ExtruderTask, self).__init__(key)
        self.extruder_client = ExtruderClient(host, port)
        self.parallelizable = True  # Assuming tasks can be run in parallel

    def run(self, stop_thread):
        """Run the extruder task using the ExtruderClient."""
        try:
            self.extruder_client.connect()
            self.log("Connected to the extruder server")

            # Example operation: sending motor data
            self.extruder_client.send_motordata(True, 10000, 10000, wait_resp=True)
            self.log("Sent motor data")

            # Check for stop signal
            #while not stop_thread():
                # Perform necessary operations
                #time.sleep(1)  # Simulate work with sleep

        #except Exception as e:
            #self.log("Exception occurred: {e}")
        finally:
            self.extruder_client.close()
            self.log("Closed connection to the extruder server")
            self.is_completed = True
            self.is_running = False
            self.log("---COMPLETED TASK---")