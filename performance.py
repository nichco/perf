import csdl
import python_csdl_backend

class mach(csdl.Model):
    def initialize(self):
        pass
    def define(self):
        
        gamma = self.declare_variable('gamma',val=1.4) # specific heat ratio
        pressure = self.declare_variable('pressure')
        density = self.declare_variable('density')
        velocity = self.declare_variable('velocity')

        a = (gamma*(pressure/density))**0.5 # local speed of sound

        self.register_output('mach',velocity/a)

class rate_of_climb(csdl.Model):
    def initialize(self):
        pass
    def define(self):
        
        total_weight = self.declare_variable('total_weight')
        available_power = self.declare_variable('available_power')
        required_power = self.declare_variable('required_power')

        rate_of_climb = (available_power - required_power)/total_weight

        self.register_output('rate_of_climb',rate_of_climb)


class electric_endurance(csdl.Model):
    def initialize(self):
        pass
    def define(self):
        
        mb = self.declare_variable('battery_mass') # (kg)
        esb = self.declare_variable('battery_specific_energy') # (wh/kg)
        eta_b2s = self.declare_variable('drivetrain_efficiency') # not including prop efficiency
        p_used = self.declare_variable('required_power') # average power used (w)

        endurance = (mb*esb*eta_b2s)/p_used

        self.register_output('endurance',endurance)


class dynamic_pressure(csdl.Model):
    def initialize(self):
        pass
    def define(self):
        
        density = self.declare_variable('density')
        velocity = self.declare_variable('velocity')

        self.register_output('dynamic_pressure',0.5*density*velocity**2)


class max_sustained_turn_load(csdl.Model):
    def initialize(self):
        pass
    def define(self):
        s = self.declare_variable('wing_area')
        q = self.declare_variable('dynamic_pressure')
        cl_max = self.declare_variable('cl_max')
        w = self.declare_variable('total_weight')

        n_max = q*s*cl_max/w

        self.register_output('sustained_turn_load',n_max)
