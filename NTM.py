"""
NIGHTMARE algorithm for uniprocessor architectures.

author: Heber Sales
"""

from simso.core import Scheduler


class NTM(Scheduler):
    def init(self):
        self.ready_list = []
        
    def on_activate(self, job):
        self.ready_list.append(job)
        job.cpu.resched()

    def on_terminated(self, job):
        self.ready_list.remove(job)
        job.cpu.resched()

    def schedule(self, cpu):
        if self.ready_list:
            job = min(self.ready_list, key=lambda x: x.wcet + x.absolute_deadline)
        else:
            job = None

        return (job, cpu)
