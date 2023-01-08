import multiprocessing


class DAG:
    
    def __init__(self, name):
        self.name = name
        self.tasks = {'root': []}
    
    @staticmethod
    def build_tree_from_dict():
        pass
    
    def run_parallel(self):
        # TODO: implement
        pass
    
    def create_dag_viz(self):
        # TODO: implement
        print(self.name)
        pass
            
    def __rshift__(self, next_task):
        """
        Called for DAG >> Task or Task >> DAG, return DAG
        """
        # TODO: implement
        return self
    
    def __str__(self):
        return self.create_dag_viz()
        
    def __repr__(self):
        return self.name

class Task:

    def __init__(self, dag, name, process=None, process_kwargs={}):
        self.dag = dag
        self.name = name
        self.process = process
        self.process_kwargs = process_kwargs

    def __rshift__(self, next_task):
        """
        Called for Task >> Task or Task >> list, return DAG
        """
        # TODO: implement
        return self.dag
    
    def __rrshift__(self, other):
        """
        Called for list >> Task, return DAG
        """
        for task in other:
            task.__rshift__(self)
        return self.dag
