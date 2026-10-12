
import networkx as nx
from ortools.sat.python import cp_model

# Part A: a simple circuit dependency graph
graph = nx.DiGraph()
graph.add_edges_from([
    ("A", "N1"),
    ("B", "N1"),
    ("N1", "OUT")
])

print("Graph nodes:", list(graph.nodes()))
print("Graph edges:", list(graph.edges()))
print("Is acyclic:", nx.is_directed_acyclic_graph(graph))

# Part B: a tiny integer optimization problem
model = cp_model.CpModel()

x = model.new_int_var(0, 10, "x")
y = model.new_int_var(0, 10, "y")

model.add(x + y <= 10)
model.maximize(3 * x + 2 * y)

solver = cp_model.CpSolver()
status = solver.solve(model)

if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
    print("x =", solver.value(x))
    print("y =", solver.value(y))
    print("Objective =", solver.objective_value)
else:
    print("No feasible solution found.")
