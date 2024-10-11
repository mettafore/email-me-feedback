from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
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
    recommendation = self.recommend_dropdown.selected_value
    anvil.server.call('send_feedback', name, email, feedback, recommendation)
    Notification("Feedback Submitted!").show()
    self.clear_inputs()

  def clear_inputs(self):
    self.name_box.text = ''
    self.email_box.text = ''
    self.feedback_area.text = ''
    self.recommend_dropdown.selected_value = None