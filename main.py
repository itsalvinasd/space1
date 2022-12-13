from webull import webull
import sys 
sys.path.insert(1,'g:/My Drive/settings')
import config as cfg

#try trade token again if error...?
wb = webull()
try:
    wb.login(cfg.user, cfg.pswd)
    print(f'Logged in with: {cfg.user}')
except: 
    print("Wrong password, try again.")
    cfg.pswd
