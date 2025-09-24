## [unreleased]

### 🚀 Features

- *(pytorch)* Support elastic training (kubeflow/trainer#1453)
- *(sdk)* Generate external Kubernetes and JobSet models (kubeflow/trainer#2466)
- *(controller)* Integrate DependsOn API (kubeflow/trainer#2484)
- *(sdk)* Migrate to OpenAPI V3 (kubeflow/trainer#2490)
- *(controller)* Refactor the Initializer APIs of TrainJob (kubeflow/trainer#2523)
- *(sdk)* Support MPI-based TrainJobs  (kubeflow/trainer#2545)
- *(runtimes)* Support DeepSpeed Runtime with OpenMPI (kubeflow/trainer#2559)
- *(runtimes)* Support MLX Distributed Runtime with OpenMPI (kubeflow/trainer#2565)
- *(sdk)* Get namespace from the provided context (kubeflow/trainer#2593)
- *(ci)* Add GitHub action to verify PR titles (#42)
- *(trainer)* Add `wait_for_job_status()` API (#52)
- *(trainer)* Add environment variables argument to CustomTrainer (#54)
- *(trainer)* Support Framework Labels in Runtimes (#56)
- *(trainer)* Add `get_runtime_packages()` API (#57)
- *(docs)* Add ROADMAP of Kubeflow SDK (#44)
- Implement Kubernetes Backend (#68)
- *(trainer)* Refactor get_job_logs() API with Iterator (#83)
- Support multiple pip index URLs in CustomTrainer (#79)
- *(trainer)* Add support for param unpacking in the training function call
- KEP-2 Local Execution Mode Proposal (#34)
- Implement TrainerClient Backends & Local Process (#33)
- *(ci)* Add automated release CI job (#65)
- Added git cliff git eg for changelog

### 🐛 Bug Fixes

- Add missing retrying package that failed the import (kubeflow/trainer#1439)
- *(sdk)* Resolve errors in deserialization (kubeflow/trainer#2457)
- *(sdk)* Add missing import type Initializer. (kubeflow/trainer#2541)
- *(sdk)* Using correct entrypoint for mpirun (kubeflow/trainer#2552)
- *(sdk)* Add missing import types. (kubeflow/trainer#2566)
- *(sdk)* Fix type annotation for `train` method's `trainer` parameter (kubeflow/trainer#2646)
- *(sdk)* Fix bad arg passed to `get_args_using_torchtune_config` (kubeflow/trainer#2647)
- Expose BuiltinTrainer API to users (#28)
- *(trainer)* Fix __all__ import. (#43)
- *(trainer)* Keep the original runtime command in get_runtime_packages() API (#64)
- Trainer client backend public (#78)
- *(docs)* Update links before SDK release (#98)
- *(scripts)* Use previous stable tag for changelog (#103)

### 💼 Other

- The "follow" of TFJobClient.get_logs (kubeflow/trainer#1254)
- Upgrade the minimum required Kubernetes version to v1.27.2 (kubeflow/trainer#2066)
- Replace outdated images with latest ones (kubeflow/trainer#2083)
- [SDK] Initial implementation of the Kubeflow Training V2 Python SDK (kubeflow/trainer#2324)
- Fix versions in HuggingFace dataset initializer (kubeflow/trainer#2369)
- Implement MPI Plugin for Kubeflow Trainer (kubeflow/trainer#2394)
- Add validation to Torch `numProcPerNode` field (kubeflow/trainer#2409)
- Refactor current `train()` API (kubeflow/trainer#2513)
- Add `TorchTuneConfig` to `train()` API (kubeflow/trainer#2522)
- Complement torch plugin to support torchtune config mutation (kubeflow/trainer#2587)
- Support mutating dataset preprocessing config in SDK (kubeflow/trainer#2638)
- Github default format
- Github format

### ⚙️ Miscellaneous Tasks

- *(test)* Add E2E tests for Kubeflow Trainer (kubeflow/trainer#2470)
- *(trainer)* Remove accelerator label from the runtimes (#51)
- *(docs)* Add Coveralls Badge to the README (#53)
- *(ci)* Add dev tests with master dependencies (#55)
- *(ci)* Align Kubernetes versions from Trainer for e2e tests (#58)
- Move pyproject.toml to root (#61)
- Update README.md (#67)
- Move dev extras to dependency-groups (#71)
- Remove tool.hatch.build.targets from pyproject (#73)
- Enable parallel builds for coveralls (#81)
- Nominate @kramaranya and @szaher as Kubeflow SDK reviewers (#76)
- *(trainer)* Use explicit exception chaining (#80)
- Add welcome new contributors CI (#82)
- Update CONTRIBUTING.md to use uv (#41)
- Add proper ruff configuration (#69)
- Ignore PRs titles with area/release labels in CI (#101)
