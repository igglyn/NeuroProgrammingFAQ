{ pkgs, lib, config, inputs, ... }:

{
  packages = with pkgs.python313Packages; [
    numpy
    beautifulsoup4
    jinja2
    markdown
    pyyaml
    pypandoc
  ];

  languages.python = {
    enable = true;
    package = pkgs.python313;
    #venv.enable = true;
    #uv.enable = true;
  };
}
