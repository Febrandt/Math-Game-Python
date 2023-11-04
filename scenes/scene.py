class Scene:
  def __init__(self, name, description, choices=None):
      self.name = name
      self.description = description
      self.choices = choices if choices else {}

  def add_choice(self, choice, callback_function):
      self.choices[choice] = callback_function