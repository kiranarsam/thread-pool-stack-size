from src.settings.settings import Settings

def hello():
  print("Hello World")

if __name__ == "__main__":
  hello()
  s = Settings()
  s.load_input_data()
  s.display_input_data()