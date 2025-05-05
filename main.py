from optimization import OptimizationProblem
from forecasting import ForecastingModel

# Test the OptimizationProblem (Transportation Problem)
if __name__ == "__main__":
    costs = [[8, 6, 10], [9, 7, 4]]  # Example cost matrix (facilities x demands)
    demand = [20, 15, 10]  # Example demands (for each demand point)
    supply = [25, 20]  # Example supplies (for each facility)

    opt_problem = OptimizationProblem(2, 3, costs, demand, supply)
    solution = opt_problem.solve_transportation_problem()
    print("Optimal Solution for Transportation Problem:")
    print(solution)

    # Test the ForecastingModel (Exponential Smoothing)
    time_series_data = [100, 105, 110, 115, 120, 125, 130]
    forecast_model = ForecastingModel(time_series_data)
    forecast = forecast_model.exponential_smoothing(alpha=0.3)
    print("\nExponential Smoothing Forecast:")
    print(forecast)
