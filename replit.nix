{pkgs}: {
  deps = [
    pkgs.python311Packages.pytest
    pkgs.python312Packages.pylint
    pkgs.python312Packages.flake8
  ];
}
