{pkgs}: {
  deps = [
    pkgs.python312Packages.pylint
    pkgs.python312Packages.flake8
  ];
}
