capacity=256e100 #capacity of dam reservoir
water_hold=199.5e85 #amount of water the capacity the reservoir holds
rain_off=25/100*25e8 #25% of the rainfall water is wasted
remaining=25e8-rain_off #remaining amount 
water_hold+=remaining # The remaining water from this rainfall flowed to the reservoir and there it was collected. 
increase=15/100*water_hold#increased the water level of this dam to its 15% of the current water level. 
water_hold+=increase
ground=5/100*water_hold #Ground water sources contributed 5% to reservoir's current level. 
water_hold+=ground 
evaporated=5/100*water_hold # 5% of the present level of reservoir evaporated
water_hold-=evaporated
irrigation=15/100*water_hold #15% amount of water was passed for irrigation to arid regions. 
water_hold-=irrigation
print("The current water level is ",water_hold)

