import matplotlib.pyplot as plt
import numpy as np

# 14:+ sensei_xml=data_binning_sync_host.xml
# 78:+ sensei_xml=data_binning_sync_matched.xml
# 144:+ sensei_xml=data_binning_sync_1dev.xml
# 212:+ sensei_xml=data_binning_sync_2dev.xml
# 
# 71: === newton++ === : total time :  575.445s
# 137: === newton++ === : total time : 577.527s
# 205: === newton++ === : total time : 803.188s
# 273: === newton++ === : total time : 861.756s
# 
# 
# 282:+ sensei_xml=data_binning_async_host.xml
# 348:+ sensei_xml=data_binning_async_matched.xml
# 414:+ sensei_xml=data_binning_async_1dev.xml
# 482:+ sensei_xml=data_binning_async_2dev.xml
# 
# 341: === newton++ === : total time : 346.902s
# 407: === newton++ === : total time : 347.311s
# 475: === newton++ === : total time : 467.769s
# 543: === newton++ === : total time : 500.665s

# 39:  === newton++ === : === initialization === : 57.9833s
# 105: === newton++ === : === initialization === : 57.9419s
# 173: === newton++ === : === initialization === : 79.7747s
# 241: === newton++ === : === initialization === : 81.7166s

# 309: === newton++ === : === initialization === : 27.5118s
# 375: === newton++ === : === initialization === : 27.5077s
# 443: === newton++ === : === initialization === : 39.3075s
# 511: === newton++ === : === initialization === : 37.5077s




cases = ['host', 'same dev.', 'ded. 1', 'ded. 2']
sync_tot = [575.445, 577.527, 803.188, 861.756]
async_tot = [346.902, 347.311, 467.769, 500.665]

x = np.array([1.,2.,3.,4.]) * 3
sync_x = x - 0.5
async_x = x + 0.5

fig = plt.figure()
plt.bar(sync_x, sync_tot, width=0.8, color='crimson', alpha=0.85, linewidth=2, label='lockstep', edgecolor='k',zorder=3)
plt.bar(async_x, async_tot, width=0.8, color='cornflowerblue', alpha=0.85, linewidth=2, label='async.', edgecolor='k', zorder=3)
plt.grid(True)
plt.ylabel('time (s)', fontweight='bold')
plt.title('Total Run Time\n10 Steps 512 GPU 24M Bodies', fontweight='bold')
plt.xticks(x, cases, fontweight='bold')
plt.legend()

plt.savefig('total_run_time_512GPU_24Mp_1rankPerGPU.png', dpi=200)

#
# sync
#

#38:  === newton++ === : sensei upd : 30.2648s
#41:  === newton++ === : sensei upd : 30.2439s
#44:  === newton++ === : sensei upd : 29.9897s
#47:  === newton++ === : sensei upd : 30.0197s
#50:  === newton++ === : sensei upd : 30.1473s
#53:  === newton++ === : sensei upd : 30.0176s
#56:  === newton++ === : sensei upd : 30.1984s
#59:  === newton++ === : sensei upd : 30.1658s
#62:  === newton++ === : sensei upd : 30.1117s
#65:  === newton++ === : sensei upd : 30.1864s
#68:  === newton++ === : sensei upd : 30.0403s
#104: === newton++ === : sensei upd : 30.3836s
#107: === newton++ === : sensei upd : 30.3318s
#110: === newton++ === : sensei upd : 30.4458s
#113: === newton++ === : sensei upd : 30.2288s
#116: === newton++ === : sensei upd : 30.4787s
#119: === newton++ === : sensei upd : 30.6482s
#122: === newton++ === : sensei upd : 30.3143s
#125: === newton++ === : sensei upd : 30.0922s
#128: === newton++ === : sensei upd : 30.2335s
#131: === newton++ === : sensei upd : 30.1994s
#134: === newton++ === : sensei upd : 30.3438s
#172: === newton++ === : sensei upd : 40.5728s
#175: === newton++ === : sensei upd : 37.0174s
#178: === newton++ === : sensei upd : 37.0359s
#181: === newton++ === : sensei upd : 36.9729s
#184: === newton++ === : sensei upd : 37.1218s
#187: === newton++ === : sensei upd : 37.3058s
#190: === newton++ === : sensei upd : 37.1026s
#193: === newton++ === : sensei upd : 37.1902s
#196: === newton++ === : sensei upd : 37.2176s
#199: === newton++ === : sensei upd : 37.2919s
#202: === newton++ === : sensei upd : 37.1129s
#240: === newton++ === : sensei upd : 44.5578s
#243: === newton++ === : sensei upd : 43.595s
#246: === newton++ === : sensei upd : 43.4362s
#249: === newton++ === : sensei upd : 43.4412s
#252: === newton++ === : sensei upd : 43.4507s
#255: === newton++ === : sensei upd : 43.3679s
#258: === newton++ === : sensei upd : 43.5355s
#261: === newton++ === : sensei upd : 43.3216s
#264: === newton++ === : sensei upd : 43.439s
#267: === newton++ === : sensei upd : 43.3316s
#270: === newton++ === : sensei upd : 43.4193s

#40:  === newton++ === : integrate part : 21.6246s
#43:  === newton++ === : integrate part : 21.6619s
#46:  === newton++ === : integrate part : 21.6437s
#49:  === newton++ === : integrate part : 21.6181s
#52:  === newton++ === : integrate part : 21.6095s
#55:  === newton++ === : integrate part : 21.6308s
#58:  === newton++ === : integrate part : 21.6486s
#61:  === newton++ === : integrate part : 21.6266s
#64:  === newton++ === : integrate part : 21.6121s
#67:  === newton++ === : integrate part : 21.659s
#106: === newton++ === : integrate part : 21.6897s
#109: === newton++ === : integrate part : 21.6276s
#112: === newton++ === : integrate part : 21.5819s
#115: === newton++ === : integrate part : 21.5881s
#118: === newton++ === : integrate part : 21.6019s
#121: === newton++ === : integrate part : 21.6439s
#124: === newton++ === : integrate part : 21.6278s
#127: === newton++ === : integrate part : 21.6392s
#130: === newton++ === : integrate part : 21.6611s
#133: === newton++ === : integrate part : 21.6006s
#174: === newton++ === : integrate part : 35.2167s
#177: === newton++ === : integrate part : 35.2042s
#180: === newton++ === : integrate part : 35.291s
#183: === newton++ === : integrate part : 35.22s
#186: === newton++ === : integrate part : 35.1391s
#189: === newton++ === : integrate part : 35.1869s
#192: === newton++ === : integrate part : 35.229s
#195: === newton++ === : integrate part : 35.143s
#198: === newton++ === : integrate part : 35.1768s
#201: === newton++ === : integrate part : 35.2312s
#242: === newton++ === : integrate part : 34.5382s
#245: === newton++ === : integrate part : 34.5605s
#248: === newton++ === : integrate part : 34.5575s
#251: === newton++ === : integrate part : 34.5476s
#254: === newton++ === : integrate part : 34.5721s
#257: === newton++ === : integrate part : 34.6289s
#260: === newton++ === : integrate part : 34.5945s
#263: === newton++ === : integrate part : 34.5738s
#266: === newton++ === : integrate part : 34.5907s
#269: === newton++ === : integrate part : 34.5309s



#
# async
#

#308: === newton++ === : sensei upd : 0.020089s
#311: === newton++ === : sensei upd : 0.075745s
#314: === newton++ === : sensei upd : 0.066729s
#317: === newton++ === : sensei upd : 0.058192s
#320: === newton++ === : sensei upd : 0.049112s
#323: === newton++ === : sensei upd : 0.066702s
#326: === newton++ === : sensei upd : 0.063977s
#329: === newton++ === : sensei upd : 0.051667s
#332: === newton++ === : sensei upd : 0.048449s
#335: === newton++ === : sensei upd : 0.049124s
#338: === newton++ === : sensei upd : 0.047094s
#374: === newton++ === : sensei upd : 0.013238s
#377: === newton++ === : sensei upd : 0.065749s
#380: === newton++ === : sensei upd : 0.079297s
#383: === newton++ === : sensei upd : 0.093602s
#386: === newton++ === : sensei upd : 0.081554s
#389: === newton++ === : sensei upd : 0.090461s
#392: === newton++ === : sensei upd : 0.088945s
#395: === newton++ === : sensei upd : 0.062848s
#398: === newton++ === : sensei upd : 0.057216s
#401: === newton++ === : sensei upd : 0.082618s
#404: === newton++ === : sensei upd : 0.084964s
#442: === newton++ === : sensei upd : 0.234019s
#445: === newton++ === : sensei upd : 0.018817s
#448: === newton++ === : sensei upd : 0.021248s
#451: === newton++ === : sensei upd : 0.018486s
#454: === newton++ === : sensei upd : 0.018677s
#457: === newton++ === : sensei upd : 0.01836s
#460: === newton++ === : sensei upd : 0.018334s
#463: === newton++ === : sensei upd : 0.018191s
#466: === newton++ === : sensei upd : 0.018598s
#469: === newton++ === : sensei upd : 0.018273s
#472: === newton++ === : sensei upd : 0.018504s
#510: === newton++ === : sensei upd : 0.331619s
#513: === newton++ === : sensei upd : 0.018612s
#516: === newton++ === : sensei upd : 0.034477s
#519: === newton++ === : sensei upd : 0.019257s
#522: === newton++ === : sensei upd : 0.018668s
#525: === newton++ === : sensei upd : 0.018344s
#528: === newton++ === : sensei upd : 0.022783s
#531: === newton++ === : sensei upd : 0.018368s
#534: === newton++ === : sensei upd : 0.018801s
#537: === newton++ === : sensei upd : 0.018363s
#540: === newton++ === : sensei upd : 0.018313s

#310: === newton++ === : integrate part : 29.942s
#313: === newton++ === : integrate part : 28.8495s
#316: === newton++ === : integrate part : 28.8664s
#319: === newton++ === : integrate part : 28.8567s
#322: === newton++ === : integrate part : 28.8852s
#325: === newton++ === : integrate part : 28.8629s
#328: === newton++ === : integrate part : 28.8984s
#331: === newton++ === : integrate part : 28.9221s
#334: === newton++ === : integrate part : 28.878s
#337: === newton++ === : integrate part : 28.8726s
#376: === newton++ === : integrate part : 29.7761s
#379: === newton++ === : integrate part : 28.9997s
#382: === newton++ === : integrate part : 29.0195s
#385: === newton++ === : integrate part : 28.8857s
#388: === newton++ === : integrate part : 28.933s
#391: === newton++ === : integrate part : 28.8257s
#394: === newton++ === : integrate part : 28.8347s
#397: === newton++ === : integrate part : 28.9357s
#400: === newton++ === : integrate part : 28.8683s
#403: === newton++ === : integrate part : 28.9209s
#444: === newton++ === : integrate part : 39.8642s
#447: === newton++ === : integrate part : 39.1225s
#450: === newton++ === : integrate part : 39.2581s
#453: === newton++ === : integrate part : 39.143s
#456: === newton++ === : integrate part : 39.1776s
#459: === newton++ === : integrate part : 39.1475s
#462: === newton++ === : integrate part : 39.1875s
#465: === newton++ === : integrate part : 39.144s
#468: === newton++ === : integrate part : 39.1337s
#471: === newton++ === : integrate part : 39.2355s
#512: === newton++ === : integrate part : 43.694s
#515: === newton++ === : integrate part : 41.9594s
#518: === newton++ === : integrate part : 41.9144s
#521: === newton++ === : integrate part : 41.9314s
#524: === newton++ === : integrate part : 42.0575s
#527: === newton++ === : integrate part : 41.9398s
#530: === newton++ === : integrate part : 41.9276s
#533: === newton++ === : integrate part : 41.8847s
#536: === newton++ === : integrate part : 41.9432s
#539: === newton++ === : integrate part : 41.8171s


# sensei has 11 per run, the first can be ignore
# sovler has 10 per run

sensei_sync = np.array([30.2648, 30.2439, 29.9897, 30.0197,
    30.1473, 30.0176, 30.1984, 30.1658, 30.1117, 30.1864, 30.0403, 30.3836,
    30.3318, 30.4458, 30.2288, 30.4787, 30.6482, 30.3143, 30.0922, 30.2335,
    30.1994, 30.3438, 40.5728, 37.0174, 37.0359, 36.9729, 37.1218, 37.3058,
    37.1026, 37.1902, 37.2176, 37.2919, 37.1129, 44.5578, 43.595, 43.4362,
    43.4412, 43.4507, 43.3679, 43.5355, 43.3216, 43.439, 43.3316, 43.4193])

solve_sync = np.array([ 21.6246, 21.6619, 21.6437, 21.6181,
    21.6095, 21.6308, 21.6486, 21.6266, 21.6121, 21.659, 21.6897, 21.6276,
    21.5819, 21.5881, 21.6019, 21.6439, 21.6278, 21.6392, 21.6611, 21.6006,
    35.2167, 35.2042, 35.291, 35.22, 35.1391, 35.1869, 35.229, 35.143, 35.1768,
    35.2312, 34.5382, 34.5605, 34.5575, 34.5476, 34.5721, 34.6289, 34.5945,
    34.5738, 34.5907, 34.5309])

sensei_sync.shape = (4,11)
solve_sync.shape = (4,10)


sensei_async = np.array([0.020089, 0.075745, 0.066729, 0.058192,
    0.049112, 0.066702, 0.063977, 0.051667, 0.048449, 0.049124, 0.047094,
    0.013238, 0.065749, 0.079297, 0.093602, 0.081554, 0.090461, 0.088945,
    0.062848, 0.057216, 0.082618, 0.084964, 0.234019, 0.018817, 0.021248,
    0.018486, 0.018677, 0.01836, 0.018334, 0.018191, 0.018598, 0.018273,
    0.018504, 0.331619, 0.018612, 0.034477, 0.019257, 0.018668, 0.018344,
    0.022783, 0.018368, 0.018801, 0.018363, 0.018313])

solve_async = np.array([ 29.942, 28.8495, 28.8664, 28.8567, 28.8852,
    28.8629, 28.8984, 28.9221, 28.878, 28.8726, 29.7761, 28.9997, 29.0195,
    28.8857, 28.933, 28.8257, 28.8347, 28.9357, 28.8683, 28.9209, 39.8642,
    39.1225, 39.2581, 39.143, 39.1776, 39.1475, 39.1875, 39.144, 39.1337,
    39.2355, 43.694, 41.9594, 41.9144, 41.9314, 42.0575, 41.9398, 41.9276,
    41.8847, 41.9432, 41.8171])

sensei_async.shape = (4,11)
solve_async.shape = (4,10)


it = np.array([1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])

fig2 = plt.figure()

sensei_sync_av = np.array([np.average(sensei_sync[0]), np.average(sensei_sync[1]), np.average(sensei_sync[2]), np.average(sensei_sync[3])])
solve_sync_av = np.array([np.average(solve_sync[0]), np.average(solve_sync[1]), np.average(solve_sync[2]), np.average(solve_sync[3])])

sensei_async_av = np.array([np.average(sensei_async[0]), np.average(sensei_async[1]), np.average(sensei_async[2]), np.average(sensei_async[3])])
solve_async_av = np.array([np.average(solve_async[0]), np.average(solve_async[1]), np.average(solve_async[2]), np.average(solve_async[3])])


plt.bar(sync_x, solve_sync_av, width=0.8, color='c', alpha=0.85, linewidth=2, label='solver lockstep', edgecolor='k',zorder=3, bottom=np.zeros([4]))
plt.bar(sync_x, sensei_sync_av, width=0.8, color='r', alpha=0.85, linewidth=2, label='in situ lockstep', edgecolor='k',zorder=3, bottom=solve_sync_av)

plt.bar(async_x, solve_async_av, width=0.8, color='mediumspringgreen', alpha=0.85, linewidth=2, label='solver async.', edgecolor='k',zorder=3, bottom=np.zeros([4]))
plt.bar(async_x, sensei_async_av, width=0.8, color='cornflowerblue', alpha=0.85, linewidth=3, label='in situ async.', edgecolor='b', zorder=3, bottom=solve_async_av)

plt.grid(True)
plt.ylabel('time (s)', fontweight='bold')
plt.title('Average Time Per Step\n10 Steps 512 GPU 24M Bodies', fontweight='bold')
plt.xticks(x, cases, fontweight='bold')
plt.legend()

plt.savefig('average_time_per_step_512GPU_24Mp_1rankPerGPU.png', dpi=200)

plt.show()

