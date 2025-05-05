import pulp

# Class for Optimization Problem -Transportation Problem
class OptimizationProblem:
    def __init__(self, number_of_facilities, number_of_demands, costs, demand, supply):
        self.number_of_facilities = number_of_facilities
        self. number_of_demands =  number_of_demands
        self.costs = costs  # cost matrix for each combination
        self.demand = demand  # demand array
        self.supply = supply  # supply array
        
    def solve_transportation_problem(self):
        # Creating the Linear Programming (LP) problem
        prob = pulp.LpProblem("TransportationProblem", pulp.LpMinimize)

        # Creating decision variables (xkl is the amount to transport from facility i to demand l)
        x = pulp.LpVariable.dicts("x", ((k, l) for k in range(self.number_of_facilities) for l in range(self. number_of_demands)),
                                  lowBound=0, cat='Continuous')

        # Objective function: minimize the total cost
        prob += pulp.lpSum([self.costs[k][l] * x[k, l] for k in range(self.number_of_facilities) for l in range(self. number_of_demands)])

        # Constraints for supply and demand
        for k in range(self.number_of_facilities):
            prob += pulp.lpSum([x[k, l] for l in range(self. number_of_demands)]) <= self.supply[k], f"Supply_Constraint_{k}"
        for l in range(self. number_of_demands):
            prob += pulp.lpSum([x[k, l] for k in range(self.number_of_facilities)]) == self.demand[l], f"Demand_Constraint_{l}"

        # Solve the problem
        prob.solve()

        # Return the solution in a readable format
        solution = {(k, l): pulp.value(x[k, l]) for k in range(self.number_of_facilities) for l in range(self. number_of_demands)}
        return solution
