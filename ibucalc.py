# coding: utf-8
import math

#Calculate IBU using imperial units
def ibuimp(mo, aap, vg, og, t):
    
    #mo = hop mass in ounces
    #aa = alpha-acid% of hop as percentage
    #vg = volume of batch in gallons
    #og = original gravity of wort
    #t = boil time of hop addition in mins
    
    #conversions
    aad = aap/100
    vl = vg * 3.785412
    mmg = mo * 28349.5
    
    #og and t are used to determine hop utilization%
    #bf = Bigness factor to account for wort gravity
    #btf = Boil Time factor to account for boil time
    #source: https://realbeer.com/hops/research.html
    bf = 1.65 * 0.000125**(og - 1)
    btf = (1 - math.exp(-0.04 * t))/4.15
    u = bf * btf
    
    ibu = (mmg * aad * u)/vl
    ibur = round(ibu, 0)
    return ibur, ibu
    
#Calculate IBU using metric units
def ibumet(mg, aap, vl, og, t):
    
    #mg = hop mass in grams
    #aa = alpha-acid% of hop as percentage
    #vl = volume of batch in liters
    #og = original gravity of wort
    #t = boil time of hop addition in mins
    
    #conversions
    aad = aap/100
    mmg = mg * 1000
    
    #og and t are used to determine hop utilization%
    #source: https://realbeer.com/hops/research.html
    bf = 1.65 * 0.000125**(og - 1)
    btf = (1 - math.exp(-0.04 * t))/4.15
    u = bf * btf
    
    ibu = (mmg * aad * u)/vl
    ibur = round(ibu, 0)
    return ibur, ibu

#calculate ABV%
def abv(og, fg):

  #og = original gravity
  #fg = final gravity
    
  abv = (og - fg) * 131
  abvr = round(abv, 1)
  abvp = str(abv) + "%"
  abvrp = str(abvr) + "%"
  return abvrp, abvp
