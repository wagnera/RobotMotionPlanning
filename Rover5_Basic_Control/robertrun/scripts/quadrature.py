#!/usr/bin/python
# Object for decoding/estimating Quadrature decodings.
# Framework by: Jason Ziglar <jpz@vt.edu>

class QuadratureEstimator:
  def __init__(self, ticks_per_revolution):
    self.ticks_per_revolution = ticks_per_revolution
    self._position = 0
    self._velocity = 0
    self._Prev_a_state = None
    self._Prev_b_state = None
    self._old_time = None
  def update(self, a_state, b_state, time):
    # Implement decoding here. Note you'll remove the pass statement once you start implementing this
    oldPos = self._position
    oldVel = self._velocity
    #set default newPos as old one in caase position does not change
    newPos = oldPos
    if self._Prev_a_state != None and self._Prev_b_state != None and self._old_time != None:
      #If the old state was both low values
      if self._Prev_a_state == False and self._Prev_b_state == False:
        #indicates foreward direction 
        if b_state == True:
          #move position foreward one tick
          newPos = oldPos + 1
        #indicates reverse direction  
        elif a_state == True:
          newPos = oldPos - 1
        #indicates no change in encoder since previous check
        else:
          #do nothing since nothing happened
          pass
      elif self._Prev_a_state == False and self._Prev_b_state == True:
        #indicates foreward direction 
        if a_state == True:
          #move position foreward one tick
          newPos = oldPos + 1
        #indicates reverse direction  
        elif b_state == False:
          newPos = oldPos - 1
        #indicates no change in encoder since previous check
        else:
          #do nothing since nothing happened
          pass
      elif self._Prev_a_state == True and self._Prev_b_state == True:
        #indicates foreward direction 
        if b_state == False:
          #move position foreward one tick
          newPos = oldPos + 1
        #indicates reverse direction  
        elif a_state == False:
          newPos = oldPos - 1
        #indicates no change in encoder since previous check
        else:
          #do nothing since nothing happened
          pass
      elif self._Prev_a_state == True and self._Prev_b_state == False:
        #indicates foreward direction 
        if a_state == False:
          #move position foreward one tick
          newPos = oldPos + 1
        #indicates reverse direction  
        elif b_state == True:
          newPos = oldPos - 1
        #indicates no change in encoder since previous check
        else:
          #do nothing since nothing happened
          pass
      if self._old_time != time:
        #calculate velocity using distance over time
        self._velocity = -(newPos - oldPos) / (self._old_time - time)
        #set new poiton
        self._position = newPos

       #record the values of a and b state for the next iteration
    self._Prev_a_state = a_state
    self._Prev_b_state = b_state
    self._old_time = time
  @property
  def position(self):
      return self._position
  @property
  def velocity(self):
      return self._velocity

#QuadEdit=QuadratureEstimator(40)


#QuadEdit.update(False,False,0.1)
#QuadEdit.update(False,True,0.2)
#QuadEdit.update(True,True,0.3)
#QuadEdit.update(True,False,0.4)
#QuadEdit.update(True,True,0.5)

#print QuadEdit.position
#print QuadEdit.velocity

