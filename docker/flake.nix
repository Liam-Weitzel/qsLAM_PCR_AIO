{
  description = "Dependencies for LVIS pipeline";

  nixConfig = {
    allow-impure = true;
    allow-unfree = true;
  };

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };

  outputs = { self , nixpkgs ,... }: let
    system = "x86_64-linux";
  in {
    devShells."${system}".default = let
      pkgs = import nixpkgs {
        inherit system;
        config = {
          allowUnfree = true;
          allowUnfreePredicate = pkg: builtins.elem (pkgs.lib.getName pkg) [
            # Explicitly allow unfree packages here
          ];
        };
      };
    in pkgs.mkShell {
      packages = [
        pkgs.util-linux
        pkgs.fastqc
        pkgs.samtools
        pkgs.bwa
        pkgs.krb5
        pkgs.kent
        pkgs.bedtools
        pkgs.perl
        pkgs.bash
        pkgs.python312
        pkgs.python312Packages.flask-api
        pkgs.pipx
        pkgs.R
        pkgs.rPackages.ggplot2
        pkgs.rPackages.xlsx
        pkgs.rPackages.GenomicRanges
        pkgs.rPackages.BiocGenerics
        pkgs.rPackages.S4Vectors
        pkgs.rPackages.GenomeInfoDb
        pkgs.rPackages.XVector

        pkgs.rPackages.ChIPpeakAnno
        pkgs.rPackages.biomaRt
        pkgs.rPackages.BSgenome
        pkgs.rPackages.Biostrings
        pkgs.rPackages.GenomicFeatures
        pkgs.rPackages.AnnotationDbi
        pkgs.rPackages.org_Hs_eg_db
        pkgs.rPackages.TxDb_Hsapiens_UCSC_hg19_knownGene
        pkgs.rPackages.BSgenome_Hsapiens_UCSC_hg19
        pkgs.rPackages.openxlsx
        pkgs.rPackages.bedr

        pkgs.htslib
        pkgs.bedops
      ];
      
      shellHook = ''
        # Create a directory for local binaries if it doesn't exist
        mkdir -p $HOME/.local/bin
        
        # Create symlink for bedops
        ln -sf $(which bedops-typical) $HOME/.local/bin/bedops

        pipx install cutadapt
        export PATH="$PATH:$HOME/.local/bin"
      '';
    };
  };
}
