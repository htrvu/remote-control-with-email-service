import os, sys

app_location = os.getcwd()
checkpoint_file_name = 'checkpoint.yaml'
checkpoint_file_path = os.path.join(app_location, 'configs', checkpoint_file_name)

path_to_shots = 'shots/'