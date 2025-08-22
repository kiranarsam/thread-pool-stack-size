import os

class Constants:
  def __init__(self):
    self.OUTPUT_DIR = os.path.join("output")
    self.SU_DIR = os.path.join(self.OUTPUT_DIR, "su")
    self.GRAPH_DIR = os.path.join(self.OUTPUT_DIR, "graph")
    self.INPUT_SU_DIR = ""
    self.INPUT_GRAPH_DIR = ""