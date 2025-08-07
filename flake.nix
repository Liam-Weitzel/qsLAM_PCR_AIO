{
  description = "Dev environment";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs, ... }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs {
        inherit system;
      };
    in {
      devShells.${system}.default = pkgs.mkShell {
        packages = [
          pkgs.python312
          pkgs.python312Packages.pyinstaller
          pkgs.python312Packages.pyside6
          pkgs.python312Packages.requests
          pkgs.python312Packages.docker
        ];

        shellHook = ''
        export QT_QPA_PLATFORM=xcb
        '';
      };
    };
}
