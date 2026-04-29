class StrategyEngine:
    def __init__(self, model):
        self.model = model

    def decide(self, stint_state):
        """
        Given the current stint state, return a decision:
        - 'pit'
        - 'extend'
        - 'push'
        - 'conserve'
        """
        pass
