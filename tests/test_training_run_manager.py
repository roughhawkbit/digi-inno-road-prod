import os
import tempfile
import unittest

from innoprod import training_run_manager

class TestTrainingRunManager(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.base_dir = self.temp_dir.name
        self.model_task_name = "test_model_task"
        self.manager = training_run_manager.TrainingRunManager(self.base_dir, self.model_task_name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_model_task_dir_creation(self):
        expected_dir = f"{self.base_dir}/{self.model_task_name}"
        self.assertTrue(os.path.exists(expected_dir))
        self.assertTrue(os.path.isdir(expected_dir))

    def test_get_next_run_dir(self):
        run_dir_1 = self.manager.get_next_run_dir()
        run_dir_2 = self.manager.get_next_run_dir()
        self.assertNotEqual(run_dir_1, run_dir_2)
        self.assertTrue(os.path.exists(run_dir_1))
        self.assertTrue(os.path.exists(run_dir_2))