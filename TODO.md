# TODO

- figure out why `just generate-cwe` fails
- make unit tests not clobber `./ephemeral-data/generated-cwes/` but rather use their own directory
- upload synthetic and hand-picked datasets to OpenML, after I get MongoDB working
- Build a web frontend to MongoDB that lets humans classify the synthetic data
- research white papers on llms and code generation, quality, and vulnerabilities. do they use syntax trees versus tokenizers?
- use mlabonne abliteration on mixtral
- find an abliterated code model
- specifically use these models
  - hf.co/DavidAU/Magistral-Small-2506-Reasoning-24B-NEO-MAX-Imatrix-GGUF:IQ4_XS-imat
  - hf.co/unsloth/Magistral-Small-2506-GGUF:IQ4_XS
