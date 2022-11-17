from Xon import Xon 
from datetime import datetime, timedelta

# TODO: Account for fees.
# TODO: Add command-line arguments.
# TODO: Account for XON accelerators.
# TODO: Allow variable reinvestment. For example, right now we reinvest as soon as we have 10 more XETA.
# But we may want to invest every 30 XETA.

# TODO: Allow user to specify cashout vs reinvestment ratios. For example, what will the number of XONs be and what will
# my XETA balance be if cashout half my XETA earnings and keep the rest for XONS.

class XetaSimulation():

    # Change these values depending on your situation
    
    sim_time = 365  # Number of days to run the simulation
    starting_xons = 1  # Number of starting XONs

    def __init__(self) -> None:
        self.starting_day = datetime.today()
        self.current_day = 1
        

        self.xons = []
        self.expired_xons = []
        self.xeta_balance = 0

        for x in range(self.starting_xons):
            self.xons.append(Xon.Xon(self.current_day, date_created=datetime.today() + timedelta(days=self.current_day)))

    """
    Simply advances the simulation day by one day.
    """    
    def advance_day(self):
        self.current_day += 1

    """
    Calculates the number of XONs that can be purchased based
    on the $X3TA balance. It then creates each new XON and adds 
    it to the simulation, while subtracting the appropriate balance.
    """
    def create_xons(self):
        possible_xons = int(self.xeta_balance / 10)

        for x in range(possible_xons):
            new_xon = Xon.Xon(self.current_day, date_created=datetime.today() + timedelta(days=self.current_day))
            self.xons.append(new_xon)
            self.xeta_balance = self.xeta_balance - 10
        
    
    """
    Looks at all created XONs and determines if any of them are expired.
    If they are, it removes them and they no longer produce.
    """
    def clean_expired_xons(self):
        for x in self.xons:
            if x.is_expired(self.starting_day + timedelta(self.current_day)):
                        self.xons.remove(x)
                        self.expired_xons.append(x)

    """
    Calculates the amount of $X3TA generated during
    a day
    """
    def accumulate_xeta(self):
        self.xeta_balance += 0.1 * len(self.xons)
    
    """
    Runs a simulation to determine how many days must pass
    before xon_count number of XONs are reached.

    :param xon_count: the XON target.
    """
    def how_long_until(self, xon_count):
        while(len(self.xons) != xon_count):
            # Cleanup expired XONS
            self.clean_expired_xons()

            # Create XONS
            self.create_xons()
            
            # Accumulate Xeta
            self.accumulate_xeta()
      
            self.advance_day()
        
        return self.current_day

    """
    Starts a standard simulation.
    """
    def start(self):
        for x in range(1, self.sim_time + 1):
            # Cleanup expired XONS
            self.clean_expired_xons()

            # Create XONS
            self.create_xons()
            
            # Accumulate Xeta
            self.accumulate_xeta()
      
            self.advance_day()

        print(f"Starting XONs: {self.starting_xons}")
        print(f"You will have {len(self.xons)} XONs in {self.sim_time} days.")
        print(f"{len(self.expired_xons)} XONs expired.")




sim = XetaSimulation()
sim.start()

