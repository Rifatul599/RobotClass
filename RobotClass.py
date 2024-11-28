class Robot:
    def __init__(self):
        self.battery_level=100
        self.task_completed=[]
        self.position=(0,0)

    def move(self,direction,steps):
        if self.battery_level<=0:
            print("Battery is empty. Please charge the robot.")
            return
        if direction.lower()=="left":
            self.position=(self.position[0]-steps,self.position[1])
        elif direction.lower()=="right":
            self.position=(self.position[0]+steps,self.position[1])
        elif direction.lower()=="up":
            self.position=(self.position[0],self.position[1]+steps)
        elif direction.lower()=="down":
            self.position=(self.position[0],self.position[1]-steps)
        else:
            print("Invalid direction. Choose 'left','right','up','down'.")
            return
        self.battery_level-=steps
        print(f"Moved {direction} by {steps} steps. Current position: {self.position}")

    def charge(self,amount):
        if amount<0:
            print("Charge amount must be positive.")
            return
        self.battery_level+=amount
        if self.battery_level>100:
            self.battery_level=100
        print(f"Charged by {amount}. Current battery level: {self.battery_level}")

    def perform_task(self,task):
        if self.battery_level<=0:
            print("Battery is empty.Please charge the robot.")
            return
        self.task_completed.append(task)
        battery_cost = 10
        self.battery_level -= battery_cost
        if self.battery_level < 0:
            self.battery_level = 0
            print("Battery drained while performing a task.")
        print(f"Performed task: {task}. Battery level: {self.battery_level}")


    def get_battery_level(self):
        return self.battery_level


    def reboot(self):
        self.battery_level=100
        self.task_completed=[]
        self.position=(0,0)
        print("Robot rebooted. Battery level reset to 100%,task cleared and position reset.")

    def show_tasks_completed(self):
        if not self.task_completed:
            print("No tasks completed yet.")
        else:
            print("Tasks completed.")
            for task in self.task_completed:
                print(f"- {task}")

robot=Robot()
robot.move("right",5)
robot.charge(20)
robot.perform_task("Clean room")
robot.show_tasks_completed()
print(f"Battery level: {robot.get_battery_level()}")
robot.reboot()


