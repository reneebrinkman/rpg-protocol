class Game:
    def __init__(self):
        self.running = True
        self.mainloop()
    
    def mainloop(self):
        self.initialize()
        while self.running:
            self.update()
            self.draw()
    
    def stop(self):
        self.running = False