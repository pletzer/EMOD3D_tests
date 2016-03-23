from matplotlib import pylab

nprocs = [32, 16, 8, 4, 2, 1]
times = [6*60+43., 13*60+27., 22*60+4., 31*60+27., 61*60+55., 95*60+21.]
speedups = [times[-1]/times[i] for i in range(len(nprocs))]

pylab.plot(nprocs, speedups, nprocs, speedups, 'kx', nprocs, nprocs, 'r--')
pylab.title('Emod3d LPSim-2010Dec26_m4.7pt_v1_Cant1D_v1-nz01-h0.500_V3.04 (FitzRoy)')
pylab.xlabel('nprocs')
pylab.ylabel('speedup')
pylab.show()
