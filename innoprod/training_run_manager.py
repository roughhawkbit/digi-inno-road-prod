import os

from .path_tools import find_highest_numbered_subdir

class TrainingRunManager:
    def __init__(self, base_dir, model_task_name):
        self.base_dir = base_dir
        self.model_task_name = model_task_name
        base_dir_exists = os.path.exists(base_dir)
        if base_dir_exists:
            print("Base directory already exists: proceeding...")
        else:
            print("Base directory does not exist! Exiting...")
            return
        model_task_dir_exists = os.path.exists(self.model_task_dir())
        if model_task_dir_exists:
            print("Model task directory already exists: resuming training...")
        else:
            print("Model task directory does not exist: creating directory and starting training from scratch...")
            os.makedirs(self.model_task_dir())
    

    def model_task_dir(self):
        return os.path.join(self.base_dir, self.model_task_name)


    def get_next_run_dir(self):
        highest_run_dir = find_highest_numbered_subdir(self.model_task_dir())
        if highest_run_dir is None:
            next_run_num = 1
        else:
            next_run_num = int(highest_run_dir.split('-')[-1]) + 1
        next_run_dir = os.path.join(self.model_task_dir(), f"run-{next_run_num}")
        if not os.path.exists(next_run_dir):
            os.makedirs(next_run_dir)
        return next_run_dir
    

    def get_highest_checkpoint_dir(self):
        highest_run_dir = find_highest_numbered_subdir(self.model_task_dir())
        if highest_run_dir is None:
            return None
        else:
            run_dir = os.path.join(self.model_task_dir(), highest_run_dir)
            highest_checkpoint_dir = find_highest_numbered_subdir(run_dir)
            if highest_checkpoint_dir is None:
                return None
            else:
                return os.path.join(run_dir, highest_checkpoint_dir)

