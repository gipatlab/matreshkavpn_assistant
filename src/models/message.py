from src.utils import Model
class Message(Model):
  def __init__(self, message: str):
    self.message = message