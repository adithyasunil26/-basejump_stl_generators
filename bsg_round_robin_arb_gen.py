#!/usr/bin/env python
from fusesoc.capi2.generator import Generator
import os
import shutil
import subprocess
import tempfile

class BSGRoundRobinArbGenerator(Generator):
    def run(self):
        channels = self.config.get('channels', 16)
        
        args = ['python', 'bsg_round_robin_arb.py', str(channels)]
        
        cwd = self.files_root
        f=open("bsg_round_robin_arb.v","w")
        
        rc = subprocess.call(args, cwd=cwd, stdout=f)
        
        if rc:
            exit(1)
        
        self.add_files([{ 'bsg_round_robin_arb.v' : {'file_type' : 'verilogSource'}}])

g = BSGRoundRobinArbGenerator()
g.run()
g.write()
