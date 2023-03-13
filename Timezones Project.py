import datetime as dt
import pytz

# class Worldclock with a constructor which takes input from the user and contains 20 methods which tell us the current time of the timezone they represent.

class Worldclock:
    def __init__(self):
        print("************************************************************************")
        print("------------------------------------------------------------------------\n")
        print("\t\t\t~ TIMEZONE MASTER ~\n")
        print("------------------------------------------------------------------------")
        print("( This program tells you the current time from 20 different cities. )")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

        print("\nWhat's the time in   =>     1. New York, USA")               # America/New_York
        print("                            2. South Pole, Antartica")         # Antarctica/South_Pole
        print("                            3. Kolkata, India")                # Asia/Calcutta
        print("                            4. Johannesburg, South Africa")    # Africa/Johannesburg
        print("                            5. Bangkok, Thailand")             # Asia/Bangkok
        print("                            6. Buenos Aires, Argentina")       # America/Argentina/Buenos_Aires
        print("                            7. Dubai, UAE")                    # Asia/Dubai
        print("                            8. Sydney, Australia")             # Australia/Sydney
        print("                            9. Los Angeles, USA")              # America/Los_Angeles
        print("                            10. Athens, Greece")               # Europe/Athens
        print("                            11. London, UK")                   # Europe/London
        print("                            12. Moscow, Russia")               # Europe/Moscow
        print("                            13. Rome, Italy")                  # Europe/Rome
        print("                            14. Maldives")                     # Indian/Maldives
        print("                            15. Zurich, Switzerland")          # Europe/Zurich
        print("                            16. Kuala Lumpur, Malaysia")       # Asia/Kuala_Lumpur
        print("                            17. Karachi, Pakistan")            # Asia/Karachi
        print("                            18. Toronto, Canada")              # America/Toronto
        print("                            19. Paris, France")                # Europe/Paris
        print("                            20. Berlin, Germany")              # Europe/Berlin
        print("[ Choose the corresponding number to your choice. ]\n")

        user_ch=int(input("Your Choice [1-20] : "))
        if (user_ch<1 or user_ch>20):
            print("Invalid Choice.")
            quit()

        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        user_tz=dt.datetime.now()
        print("\nTime in your timezone  => ",user_tz.strftime("%d/%m/%Y, %H:%M:%S"))

        print("\n__________________________________________________________________________")
        print("--------------------------------------------------------------------------\n")
        if user_ch==1:
            self.newyork()
        if user_ch==2:
            self.southpole()
        if user_ch==3:
            self.kolkata()
        if user_ch==4:
            self.johannesburg()
        if user_ch==5:
            self.bangkok()
        if user_ch==6:
            self.buenosaires()
        if user_ch==7:
            self.dubai()
        if user_ch==8:
            self.sydney()
        if user_ch==9:
            self.losangeles()
        if user_ch==10:
            self.athens()
        if user_ch==11:
            self.london()
        if user_ch==12:
            self.moscow()
        if user_ch==13:
            self.rome()
        if user_ch==14:
            self.maldives()
        if user_ch==15:
            self.zurich()
        if user_ch==16:
            self.kualalumpur()
        if user_ch==17:
            self.karachi()
        if user_ch==18:
            self.toronto()
        if user_ch==19:
            self.paris()
        if user_ch==20:
            self.berlin()

# Time finder functions
    def newyork(self):
        tz=pytz.timezone("America/New_York")
        fin_tz=dt.datetime.now(tz)
        print("Time in New york, USA  => ",fin_tz.strftime("%d/%m/%Y, %H:%M:%S"))

    def southpole(self):
        tz=pytz.timezone("Antarctica/South_Pole")
        fin_tz=dt.datetime.now(tz)
        print("Time in South Pole, Antartica  => ",fin_tz.strftime("%d/%m/%Y, %H:%M:%S"))

    def kolkata(self):
        tz=pytz.timezone("Asia/Calcutta")
        fin_tz=dt.datetime.now(tz)
        print("Time in Kolkata, India  => ",fin_tz.strftime("%d/%m/%Y, %H:%M:%S"))

    def johannesburg(self):
        tz=pytz.timezone("Africa/Johannesburg")
        fin_tz=dt.datetime.now(tz)
        print("Time in Johannesburg, South Africa  => ",fin_tz.strftime("%d/%m/%Y, %H:%M:%S"))

    def bangkok(self):
        tz=pytz.timezone("Asia/Bangkok")
        fin_tz=dt.datetime.now(tz)
        print("Time in Bangkok, Thailand  => ",fin_tz.strftime("%d/%m/%Y, %H:%M:%S"))

    def buenosaires(self):
        tz=pytz.timezone("America/Argentina/Buenos_Aires")
        fin_tz=dt.datetime.now(tz)
        print("Time in Buenos Aires, Argentina  => ",fin_tz.strftime("%d/%m/%Y, %H:%M:%S"))

    def dubai(self):
        tz=pytz.timezone("Asia/Dubai")
        fin_tz=dt.datetime.now(tz)
        print("Time in Dubai, UAE  => ",fin_tz.strftime("%d/%m/%Y, %H:%M:%S"))

    def sydney(self):
        tz=pytz.timezone("Australia/Sydney")
        fin_tz=dt.datetime.now(tz)
        print("Time in Sydney, Australia  => ",fin_tz.strftime("%d/%m/%Y, %H:%M:%S"))

    def losangeles(self):
        tz=pytz.timezone("America/Los_Angeles")
        fin_tz=dt.datetime.now(tz)
        print("Time in Los Angeles, USA  => ",fin_tz.strftime("%d/%m/%Y, %H:%M:%S"))

    def athens(self):
        tz=pytz.timezone("Europe/Athens")
        fin_tz=dt.datetime.now(tz)
        print("Time in Athens, Greece  => ",fin_tz.strftime("%d/%m/%Y, %H:%M:%S"))

    def london(self):
        tz=pytz.timezone("Europe/London")
        fin_tz=dt.datetime.now(tz)
        print("Time in London, UK  => ",fin_tz.strftime("%d/%m/%Y, %H:%M:%S"))

    def moscow(self):
        tz=pytz.timezone("Europe/Moscow")
        fin_tz=dt.datetime.now(tz)
        print("Time in Moscow, Russia  => ",fin_tz.strftime("%d/%m/%Y, %H:%M:%S"))

    def rome(self):
        tz=pytz.timezone("Europe/Rome")
        fin_tz=dt.datetime.now(tz)
        print("Time in Rome, Italy  => ",fin_tz.strftime("%d/%m/%Y, %H:%M:%S"))

    def maldives(self):
        tz=pytz.timezone("Indian/Maldives")
        fin_tz=dt.datetime.now(tz)
        print("Time in Maldives  => ",fin_tz.strftime("%d/%m/%Y, %H:%M:%S"))

    def zurich(self):
        tz=pytz.timezone("Europe/Zurich")
        fin_tz=dt.datetime.now(tz)
        print("Time in Zurich, Switzerland  => ",fin_tz.strftime("%d/%m/%Y, %H:%M:%S"))

    def kualalumpur(self):
        tz=pytz.timezone("Asia/Kuala_Lumpur")
        fin_tz=dt.datetime.now(tz)
        print("Time in Kuala Lumpur, Malaysia  => ",fin_tz.strftime("%d/%m/%Y, %H:%M:%S"))

    def karachi(self):
        tz=pytz.timezone("Asia/Karachi")
        fin_tz=dt.datetime.now(tz)
        print("Time in Karachi, Pakistan  => ",fin_tz.strftime("%d/%m/%Y, %H:%M:%S"))

    def toronto(self):
        tz=pytz.timezone("America/Toronto")
        fin_tz=dt.datetime.now(tz)
        print("Time in Toronto, Canada  => ",fin_tz.strftime("%d/%m/%Y, %H:%M:%S"))

    def paris(self):
        tz=pytz.timezone("Europe/Paris")
        fin_tz=dt.datetime.now(tz)
        print("Time in Paris, France  => ",fin_tz.strftime("%d/%m/%Y, %H:%M:%S"))

    def berlin(self):
        tz=pytz.timezone("Europe/Berlin")
        fin_tz=dt.datetime.now(tz)
        print("Time in Berlin, Germany  =>  ", fin_tz.strftime("%d/%m/%Y, %H:%M:%S"))


# Driver Code OR Main Function
obj1=Worldclock()
print("\n--------------------------------------------------------------------------")
print("**************************************************************************\n")