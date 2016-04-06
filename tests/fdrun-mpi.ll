# Example MPI LoadLeveler Job file
# @ shell = /bin/bash
#
# @ job_name = fdrun-mpi
#
# @ job_type = parallel
#
# @ wall_clock_limit     = 24:00:00
#
## @ group = NZ_merit
# @ account_no = hpcf
#
# @ output               = $(job_name).o
# @ error                = $(job_name).e
# @ notification         = never
# @ class                = General
# @ network.MPI = sn_all,not_shared,US
# @ node = 18
# @ tasks_per_node = 32 
#
# @ queue

home=/gpfs_external/filesets/nesi/home/pletzera
time poe $home/EMOD3D/buildAggressivePower6/Mpi/Emod3d/V3.0.4/edmod3d-mpi -args "par=e3d.par"

