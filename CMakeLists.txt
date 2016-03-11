cmake_minimum_required(VERSION 2.8)
project(EMOD3D_tests)

set(EMOD3D_EXECUTABLE "${HOME}/EMOD3D/Mpi/Emod3d/V3.0.4/edmod3d-mpi"
	CACHE STRING "Path to emod3d executable")

set(RUN_DIR "${HOME}/EMOD3D_tests/RunFolder"
	CACHE STRING "Directory where model will be run")

set(RUN_NAME "2010Dec26_m4.7pt_v1_Cant1D"
	CACHE STRING "Name of run")

set(LOG_DIR "Rlog"
	CACHE STRING "Directory where log files will be dumped")

set(MAIN_DUMP_DIR "OutBin"
	CACHE STRING "Directory where e3d files will be dumped")

set(FAULT_FILE "/gpfs_external/filesets/nesi/home/pletzera/nesi00213/RupModel/2010Dec26_m4pt7/Srf/2010Dec26_m4pt7.srf"
	CACHE STRING "Fault file")

set(V_MOD_DIR "/gpfs_external/filesets/nesi/home/pletzera/nesi00213/VelocityModel/Mod-1D"
	CACHE STRING "V model directory")

set(SEIS_CORD "/gpfs_external/filesets/nesi/home/pletzera/nesi00213/StationInfo/fd_nz01-h0.500.statcords"
	CACHE STRING "Seismic coordinates?")

set(SEIS_DIR "@RUN_DIR@/temp/@RUN_NAME@/SeismoBin"
	CACHE STRING "Where seismic data are saved?")

set(RESTART_DIR "@RUN_DIR@/@RUN_NAME@/Restart"
	CACHE STRING "Where restart files are saved")

# create input file
configure_file(e3d.par.in e3d.par)

# generate LoadLeveler script
configure_file(e3d.ll.in e3d.ll)

enable_testing()

