from core.base import Base

class Test(Base):
    def initialize(self):
        print("Initializing program...")

    def update(self):
        pass


# instancia essa classe e executa o programa
Test().run()