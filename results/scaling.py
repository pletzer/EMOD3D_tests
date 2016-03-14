from matplotlib import pylab

nprocs = [32, 16, 8, 4, 2, 1]
times = [6*60+43., 13*60+27., 29*60+28., 41*60+31., 48*60+31., 95*60+19.]
speedups = [times[-1]/times[i] for i in range(len(nprocs))]

pylab.plot(nprocs, speedups, nprocs, speedups, 'kx', nprocs, nprocs, 'r--')
pylab.title('QuakeCORE speedup (FitzRoy)')
pylab.xlabel('nprocs')
pylab.show()
