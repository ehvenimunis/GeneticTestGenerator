import networkx as nx
import matplotlib.pyplot as plt

# CFG'yi oluşturma
cfg = nx.DiGraph()

# Düğümleri ekleme
cfg.add_node("Start")
cfg.add_node("Check num > 0")
cfg.add_node("Check num < 0")
cfg.add_node("Positive")
cfg.add_node("Negative")
cfg.add_node("Zero")
cfg.add_node("End")

# Kenarları ekleme
cfg.add_edges_from([
    ("Start", "Check num > 0"),
    ("Check num > 0", "Positive"),
    ("Check num > 0", "Check num < 0"),
    ("Check num < 0", "Negative"),
    ("Check num < 0", "Zero"),
    ("Positive", "End"),
    ("Negative", "End"),
    ("Zero", "End"),
])

# Grafiği çizme
pos = nx.spring_layout(cfg)
nx.draw(cfg, pos, with_labels=True, arrows=True)
plt.title("Control Flow Graph (CFG)")
plt.show()
