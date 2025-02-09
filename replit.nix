{pkgs}: {
  deps = [
    pkgs.plan9port
    pkgs.python311Packages.pytest
    pkgs.python312Packages.pylint
    pkgs.python312Packages.flake8
  ];
}
