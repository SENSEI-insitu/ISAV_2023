## ISAV '23 Reproducibility Materials
This is a collection information needed to reproduce the work presented in our ISAV 2023 submission.

### Obtaining the software versions:

#### Compilers, MPI, CMake
Compiler, MPI, and CMake versions used are important. See `perlmutter\_modules.sh` for the specifics.

#### Newton++
git clone --depth=1 --branch isav\_perlmutter git@github.com:SENSEI-insitu/newtonpp.git

#### SENSEI
git clone --depth=1 --branch develop git@github.com:SENSEI-insitu/SENSEI.git

### Build, Run, and Data
Find more information in the following dirctories.

| Directory | Description |
| --------- | ----------- |
| environment | scripts that load the requisite Perlmutter modules |
| build | scripts and makefiles used to configure and build SENSEI and newton++ |
| sensei\_xml | the SENSEI XML used in the runs |
| run | SLURM batch scripts used in the runs |
| data | data gathered in the runs |
| analysis | scripts used to analyze the runs |
