# coding: utf-8
def abv(og, fg):

  #og = original gravity
  #fg = final gravity

  abv = (og - fg) * 131
  abvr = round(abv, 1)
  return abvr, abv
