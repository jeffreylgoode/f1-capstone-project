class SingleDriverModel:
    def __init__(self):
        self.model_M = None
        self.model_H = None
        self.fuel_slope = None
        self.fuel_intercept = None

    def train(self, df):
        """
        Train the single-driver Medium and Hard tire models.
        This should reproduce your Module 20 modeling logic.
        """

        # -----------------------------
        # 1. Fuel model (from Block 1.7A)
        # -----------------------------
        X = df["lap_number"].values.reshape(-1, 1)
        y = df["lap_time"].values

        fuel_model = LinearRegression()
        fuel_model.fit(X, y)

        self.fuel_slope = float(fuel_model.coef_[0])
        self.fuel_intercept = float(fuel_model.intercept_)

        # -----------------------------
        # 2. Medium tire model (to be added)
        # -----------------------------

        # -----------------------------
        # 3. Hard tire model (to be added)
        # -----------------------------

        return self


    def predict(self, row):
        """
        Predict lap time for a given row.
        """
        # TODO: implement prediction logic using trained models
        pass
