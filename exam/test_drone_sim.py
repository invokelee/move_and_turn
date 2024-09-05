import unittest
import subprocess
import rospy
import rostest

class TestDroneSim(unittest.TestCase):
    def run_command(self, cmd):
        # Create the shell process
        process = subprocess.Popen(cmd,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
        
        # Get the return code and ensure it exits properly
        return_code = process.wait()
        self.assertEqual(return_code, 0)
        
        # Get the output
        out, err = process.communicate()
        self.assertEqual('', err.decode("utf-8"))

        return out.decode("utf-8"), err.decode("utf-8")

    def test_the_drone_has_a_takeoff(self):
        # run a command
        out, err = self.run_command('rostopic list')       
        self.assertIn('/drone/takeoff', str(out))
    
    def test_the_drone_has_a_gt_pose(self):
        # run a command
        out, err = self.run_command('rostopic list')       
        self.assertIn('/drone/gt_pose', str(out))

    def test_the_drone_has_a_land(self):
        # run a command
        out, err = self.run_command('rostopic list')       
        self.assertIn('/drone/land', str(out))

if __name__ == '__main__':
    rospy.init_node('test_drone_sim')

    # Run the test with rostest
    rostest.rosrun('move_and_turn', 'test_drone_sim',
                   TestDroneSim)