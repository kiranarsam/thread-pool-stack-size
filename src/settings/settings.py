import os
import json
import sys
from dataclasses import dataclass

@dataclass
class PoolInfo:
  name: str
  func_proto: str

class Settings:
  def __init__(self):
    self.FUNC_STACK_INPUT_DATA = os.path.join("data", "settings.json")
    self.__data = None
    self.__pool_info : PoolInfo = []

  def load_input_data(self):
    try:
      if os.path.exists(self.FUNC_STACK_INPUT_DATA):
        with open(self.FUNC_STACK_INPUT_DATA, 'r', encoding="utf-8") as file:
            self.__data = json.load(file)
        thread_info = self.__data["thread_info"]
        if len(thread_info) >= 0:
          for item in thread_info:
            if "name" in item and "func_proto" in item:
              self.__pool_info.append(PoolInfo(item["name"].strip(), item["func_proto"].strip()))
    except Exception as e:
      print(f"Error parsing JSON data: {e}")

  def display_input_data(self):
    if len(self.__pool_info) >= 0:
      for pool in self.__pool_info:
        print(f"{pool.name} : {pool.func_proto}")

  def get_len_thread_info(self):
    return len(self.__pool_info)

# s = Settings()
# s.load_input_data()
# print(f"len = ", s.get_len_thread_info())
# s.display_input_data()
