FROM nixos/nix

EXPOSE 5000

WORKDIR /qsLAM-PCR-AIO

COPY . .

RUN nix-channel --add https://nixos.org/channels/nixpkgs-unstable nixpkgs && \
    nix-channel --update && \
    nix-env -iA nixpkgs.bash

RUN nix develop --impure --extra-experimental-features nix-command --extra-experimental-features flakes --accept-flake-config

CMD ["/root/.nix-profile/bin/bash"]
