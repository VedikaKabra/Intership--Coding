capacity=256e100
water_hold=199.5e85
rain_off=25/100*25e8
remaining=25e8-rain_off
water_hold+=remaining
increase=15/100*water_hold
water_hold+=increase
ground=5/100*water_hold
water_hold+=ground
evaporated=5/100*water_hold
water_hold-=evaporated
irrigation=15/100*water_hold
water_hold-=irrigation
print("The current water level is ",water_hold)

