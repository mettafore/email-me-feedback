from ._anvil_designer import Form1Template
from anvil import *
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.label_1.role = 'Headline'

    # Any code you write here will run before the form opens.

  def Generate_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def submit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert("You clicked the button!")
    name = self.name_box.text
    email = self.email_box.text
    feedback = self.feedback_area.text
