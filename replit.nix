{pkgs}: {
  deps = [
    pkgs.libftdi
    pkgs.imagemagick_light
    pkgs.python312Packages.black
    pkgs.python311Packages.pytest
    pkgs.python312Packages.pylint
    pkgs.python312Packages.flake8
  ];
}
