if (length(grep(pattern = "devtools", x = utils::installed.packages()[, 1])) == 0) {
  Sys.setenv(R_PROFILE_USER = "/dev/null")
  utils::install.packages(pkgs = "devtools", Ncpus = 1, repos = "https://CRAN.R-project.org")
  # install packages from DESCRIPTION file
  devtools::install()
  Sys.unsetenv("R_PROFILE_USER")
}
