#tropic = axial tilt
#artic = 90-axial tilt


import random
import math

class WorldGen:
    def __init__(self):
        #creates star for the world
        #habitalbe stars 0.6 - 1.4 solar masses
        self.m = round(random.uniform(0.6,1.4), 2)
        #Lumiocity L=M^3
        self.l = self.m**3
        #Diamiter D = M^0.74
        self.d = self.m**0.74
        #temp  T = M^0.505
        self.t = self.m**0.505
        #lifetime V = M^-2.5
        self.v = self.m**-2.5
        #habitable zone R = sqrt(L)* .95 to 1.37
        self.r = (math.sqrt(self.l)*0.95, math.sqrt(self.l)*1.37)


    def planet(self):
        #creates earth like planet in orbit within the habitable zone, will rerun if not in habitable zone
        while True:
            #eccentricity  0 < e < 0.2
            self.e = round(random.uniform(0,0.2), 2)
            #semi-major axis
            self.a = random.uniform(self.r[0]+self.e,self.r[1]-self.e)
            #periapsis q=a(1-e)
            self.periapsis = self.a*(1-self.e)
            #apoapsis Q=a(1+e)
            self.apoapsis = self.a*(1+self.e)
            #year legnth = sqrt(a^3/M)*365.24
            self.year_length = round(math.sqrt(self.a**3/self.m) * 365.24,2)
            #tilt
            self.tilt=random.choice(list(range(1,81))+list(range(110,181)))
            #Planet's mass
            self.pm = random.uniform(0.4,2.35)
            #check if valid
            if self.periapsis > self.r[0] and self.apoapsis < self.r[1]:
                break

        return([self.e,self.a,self.periapsis,self.apoapsis,self.year_length,self.tilt])

    def moon(self):
        #Moon density
        self.md = round(round(random.uniform(1,6),2)/5.513,2)
        #Moon radius
        self.mr = round(random.uniform(0.15,0.45),4)
        #Moon mass
        self.mm = round(self.mr**3*self.md,5)
        #Hill sphere of planet, inner (Roache Limit) uses the density of earth (1)
        self.mOutter = self.a *((self.pm/self.m)**(1. / 3))*235
        self.mInner = (2.44*(round(1.012*self.pm**0.308,1)*(1/self.md))**(1/3))
        #Moon semi-major axis based on Hill sphere and very low eccentricity of 0.01
        self.ma = random.uniform(self.mInner+0.01,self.mOutter/2)
        #Moon's obital period
        self.mo = 0.0588*math.sqrt((self.ma**3)/(self.pm+self.mm))
        return([self.md,self.mr,self.mm,self.mOutter,self.mInner,self.ma,self.mo])

    def solarCalander(self):
        self.months = int(self.year_length/self.mo)
        self.localYear = int(self.year_length)
        self.leapYear = random.choice(range(0,10))
        self.solar_calander_days = int(self.localYear/self.months)
        self.solar_extra_days = self.localYear-(self.solar_calander_days*self.months)
        self.weeks = []
        self.days_left = self.solar_calander_days
        self.total_weeks = random.choice(range(3,6))
        for i in range(1, self.total_weeks + 1):
            if (i == self.total_weeks):
                self.weeks.append(self.days_left)
                break
            else:
                self.new_week = random.randint(1,(self.days_left - (3 - i))//2)
                self.days_left -= self.new_week
                self.weeks.append(self.new_week)

        return([self.months,self.localYear,self.leapYear,self.solar_calander_days,self.solar_extra_days,self.weeks])

world = WorldGen()
print("Star calculations are based on the sun.")
print("The star has a solar mass of: "+ str(world.m))
print("The star's lumiocity is: "+ str(round(world.l,2)))
print("The star's diamiter is: " +str(round(world.d,2)))
print("The star's temp is: " +str(round(world.t,2)))
print("The world's eccentricity is: "+str(world.planet()[0]))
print("The world's semi-major axis is: "+str(round(world.planet()[1],2)))
print("The world's periapsis is: "  +str(round(world.planet()[2],5))+" and the apoapsis is: "+str(round(world.planet()[3],5)))
print("A year on the worlds is "+str(round(world.planet()[4],5))+" days long.")
print(world.moon())
print(world.solarCalander())
