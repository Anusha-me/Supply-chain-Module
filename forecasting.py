# Class for Forecasting Model (Exponential Smoothing)
class ForecastingModel:
    def __init__(self, time_series_data):
        self.time_series_data = time_series_data  # Historical demand or time series data
        
    def simple_moving_average(self, window_size):
        # Implementing simple moving average from scratch
        return [sum(self.time_series_data[i:i+window_size])/window_size for i in range(len(self.time_series_data) - window_size + 1)]
    
    def exponential_smoothing(self, alpha=0.2):
        # Implementing exponential smoothing from scratch
        forecast = [self.time_series_data[0]]  # The first forecast is just the first data point
        for t in range(1, len(self.time_series_data)):
            forecast.append(alpha * self.time_series_data[t] + (1 - alpha) * forecast[t-1])
        return forecast
