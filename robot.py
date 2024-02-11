#!/usr/bin/env python3
import wpilib
import wpilib.drive


class Robot(wpilib.TimedRobot):
    def robotInit(self):
        self._motor_left = wpilib.VictorSP(0)

        self._motor_right = wpilib.VictorSP(1)

        self._drive = wpilib.drive.DifferentialDrive(self._motor_left, self._motor_right)
        wpilib.SmartDashboard.putData("Drive", self._drive)

        self.joystick = wpilib.Joystick(0)

    def teleopPeriodic(self) -> None:
        self._drive.arcadeDrive(-1 * self.joystick.getY(), -1 * self.joystick.getX())


if __name__ == "__main__":
    wpilib.run(Robot)