{ pkgs }: {
  deps = [
    pkgs.python311Full
    pkgs.chromium
    pkgs.chromedriver
    pkgs.selenium
  ];
}
