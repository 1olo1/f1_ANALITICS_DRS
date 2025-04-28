
import fastf1
schedule = list(fastf1.get_event_schedule(2024))
print(schedule)
driverss=["SAR","BOT","GAS","OCO",'HUL',
         'ALB','TSU','RIC','MAG','ZHO','STR','ALO','PIA','HAM',
        'NOR','RUS','LEC','SAI','PER','VER']
schedule =schedule[1:]
fdrspg=[]
Nobgpg=[]
for dat in range(0,20):
    print(dat)
    session11 = fastf1.get_session(2024, str(schedule[dat]+' Grand Prix'), 'Race')
    session11.load()
    tot_lap=(session11.total_laps)
    for drv in session11.drivers:
        drv_laps = session11.laps.pick_drivers(drv)
        for _ in driverss:
            lp = list(drv_laps.get_car_data()['DRS'])
            drs_each = 0
            for j, pos in enumerate(drv_laps.get_car_data()['DRS']):
                if lp[j] == 8:
                    if not (lp[j] == lp[j - 1]): drs_each += 1
        drs_each=drs_each/tot_lap
        fdrspg.append(drs_each)

    for drv in session11.drivers:
        drv_laps = session11.laps.pick_drivers(drv)
        for _ in driverss:
            lp = list(drv_laps['Position'])
            pos_each = 0
            for j, pos in enumerate(drv_laps['Position']):
                if lp[j] - lp[j - 1] > 0:
                    pos_each += lp[j] - lp[j - 1]
        Nobgpg.append(pos_each)

print("получилось")
print("частота использования DRS",fdrspg)
print('Суммарное кол-во успешных обгонов',Nobgpg)


print(len(fdrspg),len(Nobgpg))
sp_fdrspg = sum(fdrspg)/len(fdrspg)
sp_Nobgpg = sum(Nobgpg)/len(Nobgpg)
cov=[]
for i in range(0,399):
    cov.append(fdrspg[i]-sp_fdrspg*Nobgpg[i]-sp_Nobgpg)

cov_whole=sum(cov)/len(cov)
print("получилось")
print("частота использования DRS",fdrspg)
print('Суммарное кол-во успешных обгонов',Nobgpg)
print(cov_whole)