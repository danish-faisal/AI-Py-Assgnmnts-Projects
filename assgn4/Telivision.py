class Telivision:
    def __init__(self):
        self.state="off"
        self.volume=0
        self.channel=0

    def toggle_tv(self):
        if(self.state=="off"):
            self.state="on"
        else:
            self.state="off"

    def change_channel(self,number):
        if(self.state=="off"):
            print("The TV is off.Please Switch it on")
        else:
            self.channel=number

    def increase_volume(self):
        if(self.state=="off"):
            print("The TV is off.Please Switch it on")
        else:
            self.volume=self.volume+10

    def decrease_volume(self):
        if(self.state=="off"):
            print("The TV is off.Please Switch it on")
        else:
            self.volume=self.volume-10


tv=Telivision()
tv.change_channel(293)
tv.toggle_tv()
print("TV is:",tv.state)
tv.change_channel(293)
tv.increase_volume()
print("Channel:",tv.channel,"\nVolume:",tv.volume,"\n")
