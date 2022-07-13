import pandas

class States:
    def __init__(self, file_path):
        self.states_data = pandas.read_csv(file_path, index_col='state')
    
    def get_cords(self, state):
        try:
            return self.states_data.loc[state]
        except:
            return pandas.Series([])