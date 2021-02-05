if(!require(devtools))
    install.packages(pkgs = 'devtools', Ncpus = 1, repos='https://cran.ma.imperial.ac.uk/')

# install packages from DESCRIPTION
devtools::install()
